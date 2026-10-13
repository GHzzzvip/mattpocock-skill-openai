#!/usr/bin/env python3
"""Validate packaging and resource integrity. Does not evaluate model behavior."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit('PyYAML is required. Install it in a virtual environment: python -m pip install PyYAML')


def prose(text):
    """Discard fenced examples before checking actual Markdown links."""
    fence = None
    kept = []
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            kept.append(line)
    return '\n'.join(kept)


def validate(root, official=None):
    errors = []
    notes = []
    mapping = json.loads((root / 'migration-map.json').read_text())['skills']
    entries = {x['name']: x for x in mapping}
    if len(entries) != len(mapping):
        errors.append('Duplicate destination names in migration map')
    if len({x['source'] for x in mapping}) != len(mapping):
        errors.append('Duplicate source paths in migration map')
    folders = sorted((root / 'skills').iterdir())
    if {p.name for p in folders if p.is_dir()} != set(entries):
        errors.append('Skill folders differ from migration map')
    linked = set()
    official_count = 0
    for folder in folders:
        if not folder.is_dir():
            continue
        name = folder.name
        entrypoint = folder / 'SKILL.md'
        try:
            text = entrypoint.read_text()
            match = re.match(r'\A---\n(.*?)\n---\n(.+)', text, re.S)
            if not match:
                raise ValueError('Missing YAML frontmatter or body')
            meta = yaml.safe_load(match.group(1))
            if not isinstance(meta, dict):
                raise ValueError('Frontmatter must be an object')
            if meta.get('name') != name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) >= 64:
                errors.append(f'{name}: invalid or mismatched name')
            if set(meta) - {'name', 'description', 'license', 'metadata', 'allowed-tools'}:
                errors.append(f'{name}: unsupported frontmatter fields')
            desc = meta.get('description')
            if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
                errors.append(f'{name}: invalid description')
            ui = yaml.safe_load((folder / 'agents/openai.yaml').read_text())
            for key in ('display_name', 'short_description'):
                if not isinstance(ui.get('interface', {}).get(key), str):
                    errors.append(f'{name}: missing UI {key}')
            short = ui['interface']['short_description']
            if not 25 <= len(short) <= 64:
                errors.append(f'{name}: UI description length {len(short)}')
            implicit = ui.get('policy', {}).get('allow_implicit_invocation', True)
            if not isinstance(implicit, bool) or implicit != entries[name]['implicit']:
                errors.append(f'{name}: invocation policy differs from migration map')
            if not (folder / 'LICENSE').is_file():
                errors.append(f'{name}: missing standalone license')
            for unsupported in ('Call the Skill tool', 'claude --bg', 'PreToolUse', 'disable-model-invocation:'):
                if unsupported in text:
                    errors.append(f'{name}: obsolete runtime assumption: {unsupported}')
            if official:
                result = subprocess.run([sys.executable, str(official), str(folder)], capture_output=True, text=True)
                if result.returncode:
                    errors.append(f'{name}: official validator: {result.stdout.strip()} {result.stderr.strip()}')
                else:
                    official_count += 1
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f'{name}: {exc}')

    graph = {}
    for file in sorted(root.rglob('*.md')):
        graph[file.resolve()] = set()
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\n)]+)\)', prose(file.read_text())):
            target = target.strip().split(' "', 1)[0].strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            path = (file.parent / unquote(target.split('#', 1)[0])).resolve()
            if root.resolve() not in path.parents and path != root.resolve():
                errors.append(f'{file.relative_to(root)}: link escapes package: {target}')
            elif not path.exists():
                errors.append(f'{file.relative_to(root)}: missing link target: {target}')
            else:
                graph[file.resolve()].add(path)
                linked.add(path)
    for folder in folders:
        if not folder.is_dir():
            continue
        reachable = set()
        stack = [(folder / 'SKILL.md').resolve()]
        while stack:
            path = stack.pop()
            if path in reachable:
                continue
            reachable.add(path)
            stack.extend(graph.get(path, ()))
        for kind in ('references', 'assets', 'scripts'):
            for resource in (folder / kind).rglob('*'):
                if resource.is_file() and resource.resolve() not in reachable:
                    errors.append(f'{resource.relative_to(root)}: not reachable from SKILL.md')

    cases = [json.loads(line) for line in (root / 'evals/cases.jsonl').read_text().splitlines() if line.strip()]
    seen = set()
    for case in cases:
        if case['id'] in seen:
            errors.append('Duplicate eval case: ' + case['id'])
        seen.add(case['id'])
        if case['skill'] not in entries or not case.get('prompt') or not case.get('expected'):
            errors.append('Incomplete eval case: ' + case['id'])
    for asset in root.rglob('*.sh'):
        result = subprocess.run(['bash', '-n', str(asset)], capture_output=True, text=True)
        if result.returncode:
            errors.append(f'{asset.relative_to(root)}: {result.stderr.strip()}')
    notes.append(f'{len(entries)} skills; {len(cases)} eval cases defined (behavior not executed by this validator)')
    notes.append(f'{len(linked)} local link targets checked; all skill resources checked for reachability')
    if official:
        notes.append(f'{official_count}/{len(entries)} passed the supplied OpenAI skill-creator validator')
    for note in notes:
        print(note)
    for error in errors:
        print('ERROR: ' + error, file=sys.stderr)
    if not errors:
        print('PASS: static packaging checks. This is not a behavioral benchmark.')
    return 1 if errors else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--official-validator', type=Path)
    args = parser.parse_args()
    sys.exit(validate(args.root.resolve(), args.official_validator))
