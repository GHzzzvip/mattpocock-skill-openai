# mattpocock-skill-openai

基于 [Matt Pocock 的 skills 仓库](https://github.com/mattpocock/skills) 迁移和适配的 38 个独立技能，面向支持文件、工具和 Agent Skills 的 OpenAI / Codex 宿主。

## 来源与致谢

- 原作者： [Matt Pocock](https://github.com/mattpocock)。
- 来源仓库： [mattpocock/skills](https://github.com/mattpocock/skills)。
- 迁移基线： [`49dd158d1076134a641b33efb035946536778336`](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336)。
- 本仓库为独立维护的 OpenAI / Codex 适配版本，并非 Matt Pocock 或 OpenAI 官方发布。迁移映射见 [migration-map.json](migration-map.json)，适配说明见 [MIGRATION.md](MIGRATION.md)。
- 沿用原项目的 [MIT License](LICENSE)，保留 Matt Pocock 的版权声明；每个技能目录也包含可独立分发的许可证。

## 结构

```text
mattpocock-skill-openai/
├── README.md
├── MIGRATION.md
├── VALIDATION.md
├── migration-map.json
├── LICENSE
├── skills/<skill-name>/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── LICENSE
│   └── references/ 或 assets/（按需）
├── scripts/validate.py
└── evals/cases.jsonl
```

技能正文使用英文，交流和产物语言遵循用户需求。技能不绑定某个 GPT 型号，不修改模型或上下文设置。保留原版显式调用策略，避免迁移时偷偷改变工作流入口。实验性技能的状态仍保留在迁移清单里。

## 使用

直接指定文件即可开始，例如：“读取 `mattpocock-skill-openai/skills/tdd/SKILL.md`，按它实现这个行为。”

需要自动发现时，把选定技能的完整目录复制或链接到目标仓库的 `.agents/skills/`。Codex CLI/IDE 可使用 `$tdd` 这样的显式引用；支持的 ChatGPT 界面可通过技能选择器选择。这个任意命名的产物目录本身不代表已经安装。不要同时安装同名原版与新版。[官方技能文档](https://learn.chatgpt.com/docs/build-skills)

每个技能都可独立分发；不要只复制 `SKILL.md` 而漏掉其引用的资源。若已有同名技能，先比较再选择版本，避免覆盖个人修改。

## 推荐起点

- 看整体路线：`ask-matt`。
- 澄清需求：`grill-with-docs`。
- 大功能：`to-spec` → `to-tickets` → `implement` 或 `implement-spec`。
- 小功能：直接 `implement`；测试先行用 `tdd`。
- 排查问题：`diagnosing-bugs`；审查改动：`code-review`。
- 学习编写技能：`writing-for-agents`。

## 全量迁移清单

| 原技能 | 新技能 | 类别 | 调用策略 |
|---|---|---|---|
| `ask-matt` | [ask-matt](skills/ask-matt/SKILL.md) | 工程 | 仅显式 |
| `code-review` | [code-review](skills/code-review/SKILL.md) | 工程 | 自动或显式 |
| `codebase-design` | [codebase-design](skills/codebase-design/SKILL.md) | 工程 | 自动或显式 |
| `diagnosing-bugs` | [diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) | 工程 | 自动或显式 |
| `domain-modeling` | [domain-modeling](skills/domain-modeling/SKILL.md) | 工程 | 自动或显式 |
| `grill-with-docs` | [grill-with-docs](skills/grill-with-docs/SKILL.md) | 工程 | 仅显式 |
| `implement` | [implement](skills/implement/SKILL.md) | 工程 | 仅显式 |
| `implement-spec` | [implement-spec](skills/implement-spec/SKILL.md) | 工程 | 仅显式 |
| `improve-codebase-architecture` | [improve-codebase-architecture](skills/improve-codebase-architecture/SKILL.md) | 工程 | 仅显式 |
| `pr` | [pr](skills/pr/SKILL.md) | 工程 | 自动或显式 |
| `prototype` | [prototype](skills/prototype/SKILL.md) | 工程 | 自动或显式 |
| `research` | [research](skills/research/SKILL.md) | 工程 | 自动或显式 |
| `retro` | [retro](skills/retro/SKILL.md) | 工程 | 仅显式 |
| `setup-matt-pocock-skills` | [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/SKILL.md) | 工程 | 仅显式 |
| `tdd` | [tdd](skills/tdd/SKILL.md) | 工程 | 自动或显式 |
| `to-spec` | [to-spec](skills/to-spec/SKILL.md) | 工程 | 仅显式 |
| `to-tickets` | [to-tickets](skills/to-tickets/SKILL.md) | 工程 | 仅显式 |
| `triage` | [triage](skills/triage/SKILL.md) | 工程 | 仅显式 |
| `wayfinder` | [wayfinder](skills/wayfinder/SKILL.md) | 工程 | 仅显式 |
| `wizard` | [wizard](skills/wizard/SKILL.md) | 工程 | 自动或显式 |
| `chief-of-staff` | [chief-of-staff](skills/chief-of-staff/SKILL.md) | 实验性 | 仅显式 |
| `claude-handoff` | [background-handoff](skills/background-handoff/SKILL.md) | 实验性 | 仅显式 |
| `loop-me` | [loop-me](skills/loop-me/SKILL.md) | 实验性 | 仅显式 |
| `setup-ts-deep-modules` | [setup-ts-deep-modules](skills/setup-ts-deep-modules/SKILL.md) | 实验性 | 仅显式 |
| `writing-beats` | [writing-beats](skills/writing-beats/SKILL.md) | 实验性 | 仅显式 |
| `writing-fragments` | [writing-fragments](skills/writing-fragments/SKILL.md) | 实验性 | 仅显式 |
| `writing-shape` | [writing-shape](skills/writing-shape/SKILL.md) | 实验性 | 仅显式 |
| `git-guardrails-claude-code` | [git-guardrails](skills/git-guardrails/SKILL.md) | 可选工具 | 自动或显式 |
| `migrate-to-shoehorn` | [migrate-to-shoehorn](skills/migrate-to-shoehorn/SKILL.md) | 可选工具 | 自动或显式 |
| `scaffold-exercises` | [scaffold-exercises](skills/scaffold-exercises/SKILL.md) | 可选工具 | 自动或显式 |
| `setup-pre-commit` | [setup-pre-commit](skills/setup-pre-commit/SKILL.md) | 可选工具 | 自动或显式 |
| `grill-me` | [grill-me](skills/grill-me/SKILL.md) | 效率 | 仅显式 |
| `grilling` | [grilling](skills/grilling/SKILL.md) | 效率 | 自动或显式 |
| `handoff` | [handoff](skills/handoff/SKILL.md) | 效率 | 仅显式 |
| `teach` | [teach](skills/teach/SKILL.md) | 效率 | 仅显式 |
| `to-questionnaire` | [to-questionnaire](skills/to-questionnaire/SKILL.md) | 效率 | 仅显式 |
| `wait-what` | [wait-what](skills/wait-what/SKILL.md) | 效率 | 仅显式 |
| `writing-for-agents` | [writing-for-agents](skills/writing-for-agents/SKILL.md) | 效率 | 自动或显式 |

## 校验

使用包含 PyYAML 的 Python 环境：

```bash
python scripts/validate.py
```

可另外传入本机 OpenAI skill-creator 的校验器：

```bash
python scripts/validate.py --official-validator /path/to/skill-creator/scripts/quick_validate.py
```

检查结果与实际执行范围见 [VALIDATION.md](VALIDATION.md)，设计取舍与官方依据见 [MIGRATION.md](MIGRATION.md)。
