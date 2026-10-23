# 实现说明 · EA-20261022-05 · 子任务必须携带可逐项判定的验收清单

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-05 |
| proposal_id | 20261022-1705-ai-public-rules |
| ai_form | Rule（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 公共级 / 无 / 无 |
| record | eng-knowledge-assets `assets/20261022-1705-ai-public-rules/EA-20261022-05-subtask-acceptance-checklist.md`（approved 2026-10-22） |
| 组件 owner | AI 平台团队（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/rule-subtask-acceptance-checklist.md` → 安装名 `~/.claude/rules/subtask-acceptance-checklist.md` |

## 语义保持对照

statement 的每条结论逐条落到 artifact，未增删语义。

| # | statement 结论（原文） | artifact 承载位置 |
|---|---|---|
| 1 | 规则：向下游执行方下发的每一个子任务，必须携带验收清单；缺少验收清单的子任务不得下发，也不得执行。 | `artifacts/rule-subtask-acceptance-checklist.md` ›「## 规则」 |
| 2 | 最小内容：验收清单至少包含交付物、通过条件（可检查、可判定的标准）与验证方式。 | 「## 执行要求」第 1 条「写全最小内容」 |
| 3 | 退回：执行方收到未附验收清单的子任务，应退回要求补全，不得自行推定验收标准后开工。 | 「## 执行要求」第 2 条「执行方退回」 |
| 4 | 字段校验：任务包必须通过字段校验（必填字段齐全）后才可下发；校验拦截即视为任务包不合格，需补全后重新提交。 | 「## 执行要求」第 3 条「先过字段校验」 |
| 5 | 判定边界："子任务"指任何被单独指派、需要独立交付的工作单元；父任务的整体目标不能替代子任务的验收清单，"按需求做完"之类的描述不算验收清单。 | 「## 执行要求」第 4 条「按边界识别子任务」（三点合写于同一条：子任务定义、父任务目标不可替代、口头描述不算清单） |
| 6 | 衔接：验收清单同时是执行方自查与独立复核的依据，与"任何产出交付前必须验证或评审"这一规则配套使用。 | 「## 执行要求」第 5 条「复用为自查与复核依据」 |
| 7 | 完成判定：每个已下发子任务的任务包中都能定位到验收清单，且清单条目可逐项判定通过或失败。 | 「## 完成标准」 |

## 设计取舍

1. **不加 `paths:`**：规则约束的是"下发子任务"这一动作，不绑定文件类型，任何会话都可能发生派单，保持全局加载。
2. **只写 record 给的三项最小内容**：交付物、通过条件、验证方式。未内置更细的字段表或模板，因为 record 只规定"至少包含"，扩展字段属项目事项（实现备注，不改资产语义）；字段校验一节因此只引用"必填字段齐全"这一既有机制，不定义字段清单。
3. **把"不得执行"落成执行方的退回动作**：规则第 2 条与 statement 的"执行方退回"一致，使"不得执行"在会话内可判定，而不只是下游禁令。
4. **与 EA-20261022-04 挂接**：同一提案的 EA-04（任何产出交付前必须验证或评审）要求"按验收清单逐项自查 + 独立复核"，本规则提供该清单，二者互补；本包不复制 EA-04 的自查/复核要求，只做引用。
5. **去重扫描**：`~/.claude/rules/` 现有 4 条（auto-mode-classifier、editing-fenced-docs、external-ai-plans、telegram-bot-handlers）均不涉及子任务验收清单；`eng-asset-ai-components/rules/` 当前为空。无重复实现。

## 测试结果

- 触发样例：`tests/trigger-cases.md` 共 10 例（H1-H7 应命中、N1-N3 不应命中），逐例对照规则全文判定，10/10 与期望一致；最小内容三项、退回义务、字段校验拦截、子任务边界、清单复用为自查复核依据五个判定点均被覆盖。
- 确定性校验：见下方「校验记录」。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-05
- 来源提案 ID：20261022-1705-ai-public-rules
- 目标组件形态：Rule
- 目标层级 / 领域 / 项目：公共级 / 无 / 无
- 组件 owner：AI 平台团队
- 变更内容：新增 `rules/subtask-acceptance-checklist.md`（package：`build/EA-20261022-05/`）
- 验收清单：目录与 manifest 对账、record approved 与 proposal/ai_form 一致、frontmatter 含 asset_id 与 ai_form、无敏感信息、无 record 原文混入、语义保持对照通过、触发样例通过
- 回滚方式：revert 合入 PR；已安装环境删除 `~/.claude/rules/subtask-acceptance-checklist.md`

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-05 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-05，2026-10-22 approved 入库。record：`assets/20261022-1705-ai-public-rules/EA-20261022-05-subtask-acceptance-checklist.md`。provenance 仅记录于本文件，artifact 不含。
