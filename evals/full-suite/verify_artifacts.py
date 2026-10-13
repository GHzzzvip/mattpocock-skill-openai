#!/usr/bin/env python3
"""Independent local checks on executed fixture artifacts, not model grading."""
import argparse,hashlib,json,os,subprocess
from pathlib import Path

def snapshot(d):
 return {str(p.relative_to(d)):hashlib.sha256(p.read_bytes()).hexdigest() for p in d.rglob('*') if p.is_file() and not any(x in p.relative_to(d).parts for x in ('.git','__pycache__','node_modules'))}
def run(d,*cmd):
 p=subprocess.run(cmd,cwd=d,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 return {'command':list(cmd),'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def verify(root):
 if not root.is_dir() or not list(root.glob('*.request.json')):
  raise ValueError('Expected a prepared run directory with request manifests')
 results=[]
 readonly={'review-working-tree','teach-one-question','triage-read-only','triage-already-built','retro-no-scope-expansion','router-no-activation'}
 for request in sorted(root.glob('*.request.json')):
  case=json.loads(request.read_text());cid=case['id'];run_id=request.name[:-len('.request.json')];d=Path(case['workspace']);rp=root/(run_id+'.result.json')
  if not rp.exists():continue
  before=json.loads((root/(run_id+'.before.json')).read_text());after=snapshot(d)
  checks={};commands=[]
  if cid in readonly:checks['workspace_content_unchanged']=before['files']==after
  head=run(d,'git','rev-parse','HEAD');commands.append(head)
  if cid!='graph-no-delegation':checks['no_commit_created']=head['stdout'].strip()==before['head']
  for filename in {'implement-no-commit':'user-notes.txt','explicit-policy-respected':'user-notes.txt','shape-source-readonly':'raw.md','precommit-preserve':'user-work.txt','triage-already-built':'.out-of-scope/themes.md'}.get(cid,'').split():
   checks['preserved_'+filename]=after.get(filename)==before['files'].get(filename)
  if cid=='precommit-preserve':
   checks['staged_user_diff_preserved']=run(d,'git','diff','--cached','--','user-work.txt')['stdout'].strip()==before['index'].strip()
   pkg=json.loads((d/'package.json').read_text())
   checks['prepare_behavior_preserved']='node scripts/prepare.cjs' in pkg['scripts'].get('prepare','') and after.get('scripts/prepare.cjs')==before['files'].get('scripts/prepare.cjs') and (d/'.prepare-ran').read_text()=='yes'
   checks['formatter_preferences_preserved']=after.get('.prettierrc')==before['files'].get('.prettierrc')
   checks['compliance_hook_retained']='npm run compliance' in (d/'.husky/pre-commit').read_text()
  if cid in {'implement-no-commit','explicit-policy-respected','tdd-existing-seam','graph-no-delegation','triage-already-built'}:
   t=run(d,'python3','-m','unittest','discover','-v');commands.append(t);checks['tests_pass']=t['returncode']==0
  if cid=='writing-preserve-edits':
   original=run(d,'git','show','HEAD:ideas.md')['stdout'];checks['original_fragments_preserved']=(d/'ideas.md').read_text().startswith(original)
   checks['supplied_fragment_appended']='ten-minute manual check' in (d/'ideas.md').read_text()[len(original):]
  if cid=='prototype-no-production': checks['production_unchanged']=after.get('production/checkout.js')==before['files'].get('production/checkout.js')
  if cid=='normal-edit-no-architecture':checks['only_typo_file_changed']=set(k for k in after if after[k]!=before['files'].get(k))=={'README.md'};checks['typo_fixed']='a simple example' in (d/'README.md').read_text()
  if cid=='normal-test-no-shoehorn':checks['timeout_is_10000']=json.loads((d/'test.config.json').read_text())['timeout']==10000;checks['only_config_changed']=set(k for k in after if after[k]!=before['files'].get(k))=={'test.config.json'}
  if cid=='single-task-no-chief':checks['only_target_changed']=set(k for k in after if after[k]!=before['files'].get(k))=={'total.py'}
  results.append({'id':cid,'run_id':run_id,'checks':checks,'commands':commands,'changed_or_added':[k for k in after if after[k]!=before['files'].get(k)],'removed':[k for k in before['files'] if k not in after]})
 return results
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('run_root',type=Path);p.add_argument('--output',type=Path);a=p.parse_args();data=verify(a.run_root)
 if a.output:a.output.write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps({'cases_with_results':len(data),'failed_checks':{x['id']:[k for k,v in x['checks'].items() if not v] for x in data if not all(x['checks'].values())}},indent=2))
