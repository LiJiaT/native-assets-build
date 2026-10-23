# 实现说明 · EA-20261022-02 · Verilog 文件变更必须同步 filelist

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-02 |
| proposal_id | 20261022-1705-ai-public-rules |
| ai_form | Rule（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 公共级 / 无 / 无 |
| record | eng-knowledge-assets `assets/20261022-1705-ai-public-rules/EA-20261022-02-filelist-sync.md`（approved 2026-10-22） |
| 组件 owner | AI 平台团队（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/rule-verilog-filelist-sync.md` → 安装名 `~/.claude/rules/verilog-filelist-sync.md` |

## 语义保持对照

statement 的每条结论逐条落到 artifact，未增删语义。

| # | statement 结论（原文） | artifact 承载位置 |
|---|---|---|
| 1 | 模块的 Verilog 文件发生新增或更新时，必须在同一次变更中同步更新该模块的 filelist。 | `artifacts/rule-verilog-filelist-sync.md` ›「## 规则」 |
| 2 | 触发：本次变更触及模块内任一 Verilog 文件的新增或更新，即触发本规则。 | 同文件 ›「## 执行要求」第 1 条「判定触发」 |
| 3 | 同步：filelist 的更新与代码变更属于同一次变更，不得拆成两次提交，也不得"先提交代码、稍后补 filelist"。 | 「## 执行要求」第 2 条「同一次变更」 |
| 4 | 一致：更新后的 filelist 必须与目录中实际存在的 Verilog 文件集合一致——新增的文件必须被登记，已不存在的文件不得继续保留在清单中。 | 「## 执行要求」第 3 条「清单一致」 |
| 5 | 校验：提交前必须通过 hook 对 filelist 与目录一致性的校验；校验不通过即视为变更未完成，须先补齐 filelist 再提交。 | 「## 执行要求」第 4 条「提交前校验」 |
| 6 | 不触发：本次变更完全不涉及 Verilog 文件时（例如只改文档或脚本），本规则不适用。 | 「## 执行要求」第 5 条「判定不适用」 |
| 7 | 完成判定：hook 一致性校验通过，即为本规则的完成标准。 | 「## 完成标准」 |

## 设计取舍

1. **只做 rule 全文，不做描述**：artifact 是可直接安装的 rules markdown，祈使句逐条对应 statement 结论；标题与分节只为可读性，不引入新约束。
2. **`paths` 只限定 `**/*.v`**：record 的触发条件是"Verilog 文件"，未提 SystemVerilog 或其他扩展名，故不擅自扩大文件类型；filelist 的具体命名与位置 record 未给，正文沿用"该模块的 filelist"表述，不发明目录约定。规则加载按文件类型收敛，避免无关会话常驻上下文。
3. **hook 只作为完成判定，不在本包内联实现**：record 要求"提交前通过 hook 校验"，hook 属另一组件形态；本包不写脚本，避免越权把 Rule 扩成 Hook。若目标环境尚无该 hook，需由 owner 另行立项实现（实现备注，不改资产语义）。
4. **不写 filelist 生成命令或路径**：record 未给出具体命令与命名，任何补全都会造成语义增量，只保留"登记新增、删除已不存在条目"的可判定口径。
5. **去重扫描**：`~/.claude/rules/` 现有 4 条（auto-mode-classifier、editing-fenced-docs、external-ai-plans、telegram-bot-handlers）与本条无重叠；`eng-asset-ai-components/rules/` 当前为空，无重复组件。

## 测试结果

- 触发样例：`tests/trigger-cases.md` 共 9 例（H1-H5 应命中、N1-N4 不应命中），逐例对照规则全文判定，9/9 与期望一致；5 条 statement 动作边界（触发、同次变更、一致、校验、不触发）均被至少一条样例覆盖。
- 确定性校验：见下方「校验记录」。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-02
- 来源提案 ID：20261022-1705-ai-public-rules
- 目标组件形态：Rule
- 目标层级 / 领域 / 项目：公共级 / 无 / 无
- 组件 owner：AI 平台团队
- 变更内容：新增 `rules/verilog-filelist-sync.md`（package：`build/EA-20261022-02/`）
- 验收清单：目录与 manifest 对账、record approved 与 proposal/ai_form 一致、frontmatter 含 asset_id、无敏感信息、无 record 原文混入、语义保持对照通过、触发样例通过
- 回滚方式：revert 合入 PR；已安装环境删除 `~/.claude/rules/verilog-filelist-sync.md`

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-02 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-02，2026-10-22 approved 入库。record：`assets/20261022-1705-ai-public-rules/EA-20261022-02-filelist-sync.md`。provenance 仅记录于本文件，artifact 不含。
