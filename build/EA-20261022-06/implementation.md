# 实现说明 · EA-20261022-06 · 原始记录不得写入长期记忆

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-06 |
| proposal_id | 20261022-1705-ai-public-rules |
| ai_form | Rule（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 公共级 / 无 / 无 |
| record | native-assets `assets/20261022-1705-ai-public-rules/EA-20261022-06-no-raw-records-in-memory.md`（approved 2026-10-22） |
| 组件 owner | AI 平台团队（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/rule-no-raw-records-in-memory.md` → 安装名 `~/.claude/rules/no-raw-records-in-memory.md` |

## 语义保持对照

statement 的每条结论逐条落到 artifact，未增删语义。

| # | statement 结论（原文） | artifact 承载位置 |
|---|---|---|
| 1 | 规则：不得把原始记录写入长期记忆。 | `artifacts/rule-no-raw-records-in-memory.md` ›「## 规则」 |
| 2 | 长期记忆的范围：会被长期保留、并能被后续任务读取的载体，包括 CLAUDE.md、rules 文件、memory 条目与知识资产正文。 | 「## 执行要求」第 1 条「认准长期记忆载体」（四类载体逐一列出） |
| 3 | 原始记录的范围：会议原文与逐字稿、聊天记录、调试日志、命令输出、临时文件内容。 | 「## 执行要求」第 2 条「认准原始记录」（五类逐一列出） |
| 4 | 允许写入的形态：只写提炼后的结论（事实、要求、决策及其理由），并注明出处（材料名 + 日期或位置），使结论可回溯到原始记录，而原始记录本身仍留在原载体。 | 「## 执行要求」第 3 条「按"结论 + 出处引用"写」 |
| 5 | 判定边界：先把原始记录粘贴进正文、再补一句结论，同样属于违规；"只摘录一小段"不构成豁免。 | 「## 执行要求」第 4 条「不留"先粘贴再补结论"的口子」（两个边界合写于同一条） |
| 6 | 当次使用：原始记录可以在当前任务或会话内作为工作输入使用，但不得沉淀为长期记忆。 | 「## 执行要求」第 5 条「限定当次使用」 |
| 7 | 完成判定：长期记忆载体的每一段内容都能回答"这是提炼后的结论吗"，原始记录仅以出处引用（材料名 + 日期/位置）形式出现。 | 「## 完成标准」 |

## 设计取舍

1. **不加 `paths:`**：受约束的是四类载体的写入形态，文件类型不限定（CLAUDE.md、rules、memory、知识资产正文都可能命中），保持全局加载。
2. **不内联任何原始记录示例**：artifact 自身是 rules 文件、属本条定义的长期记忆载体，因此正文只写提炼后的要求，示例与反例一律只按类型指称（逐字稿、聊天记录、调试日志），不给出原文片段，避免规则文件本身成为违规样本。测试样例同样只描述场景类型，不含原始记录内容。
3. **自身合规与出处引用**：record 的 evidence 已说明其正文为提炼后的规则文本、不含会议/聊天/日志原文，故不违反本条自身；artifact 沿用同一形态，仅保留"结论 + 出处引用"这一写法要求本身。按包级约定 provenance 只写本文件，artifact 不携带出处行；本文件末尾 provenance 行与上文「来源与理由」记录的材料名与日期，构成该规则文件的出处引用，结论可回溯而原文未被搬运。
4. **只写规则，不造工具**：本条约束的是写入前的心智检查（"这是提炼后的结论吗"），record 未要求自动拦截，因此不配脚本或 hook；若后续要求强拦截，属另一次形态映射，不在本包扩展。
5. **去重扫描**：`~/.claude/rules/` 现有 4 条均不涉及长期记忆写入形态；`native-assets-build/rules/` 当前为空；`~/.claude/skills/` 中无同语义规则型组件。未重复造件。

## 测试结果

- 触发样例：`tests/trigger-cases.md` 共 11 例（H1-H7 应命中、N1-N4 不应命中），逐例对照规则全文判定，11/11 与期望一致；四类载体、五类原始记录、"先粘贴再补结论"与"只摘一小段"两个边界、当次使用豁免均被覆盖。
- 自检：artifact 与 samples 均不含任何会议、聊天或日志原文；仅以类型名指称，满足"不违反自身规则"。
- 确定性校验：见下方「校验记录」。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-06
- 来源提案 ID：20261022-1705-ai-public-rules
- 目标组件形态：Rule
- 目标层级 / 领域 / 项目：公共级 / 无 / 无
- 组件 owner：AI 平台团队
- 变更内容：新增 `rules/no-raw-records-in-memory.md`（package：`build/EA-20261022-06/`）
- 验收清单：目录与 manifest 对账、record approved 与 proposal/ai_form 一致、frontmatter 含 asset_id 与 ai_form、无敏感信息、无 record 原文混入、语义保持对照通过、触发样例通过、artifact 自身不含原始记录
- 回滚方式：revert 合入 PR；已安装环境删除 `~/.claude/rules/no-raw-records-in-memory.md`

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\native-assets-build\build\EA-20261022-06 --assets-repo D:\Project\native-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-06，2026-10-22 approved 入库。record：`assets/20261022-1705-ai-public-rules/EA-20261022-06-no-raw-records-in-memory.md`。provenance 仅记录于本文件，artifact 不含。
