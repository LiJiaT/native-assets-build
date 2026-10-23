# 实现说明 · EA-20261022-04 · 任何产出交付前必须验证或评审

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-04 |
| proposal_id | 20261022-1705-ai-public-rules |
| ai_form | Rule（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 公共级 / 无 / 无 |
| record | eng-knowledge-assets `assets/20261022-1705-ai-public-rules/EA-20261022-04-verify-or-review-before-delivery.md`（approved 2026-10-22） |
| 组件 owner | AI 平台团队（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/rule-verify-or-review-before-delivery.md` → 安装名 `~/.claude/rules/verify-or-review-before-delivery.md` |

## 语义保持对照

statement 的每条结论逐条落到 artifact，未增删语义。

| # | statement 结论（原文） | artifact 承载位置 |
|---|---|---|
| 1 | 任何产出在交付前必须经过验证或评审，二者至少完成其一，不得省略。 | `artifacts/rule-verify-or-review-before-delivery.md` ›「## 规则」 |
| 2 | 适用范围：AI 或人产出的代码、文档、配置、资产提案与结论，交付前一律适用。 | 「## 执行要求」第 1 条「确认适用范围」 |
| 3 | 自查：执行方必须先按验收清单逐项自查，并给出可复核的检查结果（检查项 + 结论），不得只写"已检查"。 | 「## 执行要求」第 2 条「逐项自查」 |
| 4 | 独立复核：执行方自查不能替代独立复核；交付前须由未参与执行的另一方（人，或与执行上下文独立的 AI 复核者）按同一验收清单复核。 | 「## 执行要求」第 3 条「独立复核」 |
| 5 | 不可验证时：确实无法自动验证的产出，必须转为评审，并在交付说明中写明未能验证的部分与原因。 | 「## 执行要求」第 4 条「不可验证时转评审」 |
| 6 | 判定边界：自查与复核均未完成的产出，不得标记为完成或已交付。 | 「## 执行要求」第 5 条「不提前标记完成」 |
| 7 | 完成判定：存在可逐项追溯的自查记录与独立复核记录，或存在与交付物对应的评审结论。 | 「## 完成标准」 |

## 设计取舍

1. **不加 `paths:`**：适用范围覆盖所有产出类型（代码、文档、配置、资产提案与结论），不能按文件类型收敛，保持全局加载。
2. **不内置验收清单模板**：record 要求"按验收清单"，但未给出统一清单内容，本包不发明检查项清单，只规定自查/复核的可复核形式（检查项 + 结论、"同一验收清单"）；具体清单由项目或组件 owner 提供（实现备注，不改资产语义）。
3. **"独立"严格按 record 口径**：未参与执行的人，或与执行上下文独立的 AI 复核者；不额外定义独立性等级或工具要求。
4. **与交付动作绑定**：把"标记完成/已交付"作为规则的可判定落点（第 5 条），使规则在交付环节可检查，而不只是倡导。
5. **去重扫描**：`~/.claude/rules/` 现有 4 条均不涉及交付前自查与独立复核，无重叠；`eng-asset-ai-components/rules/` 当前为空。

## 测试结果

- 触发样例：`tests/trigger-cases.md` 共 9 例（H1-H6 应命中、N1-N3 不应命中），逐例对照规则全文判定，9/9 与期望一致；自查形式、独立复核、不可验证转评审、未完成不得标记完成四条边界均被覆盖。
- 确定性校验：见下方「校验记录」。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-04
- 来源提案 ID：20261022-1705-ai-public-rules
- 目标组件形态：Rule
- 目标层级 / 领域 / 项目：公共级 / 无 / 无
- 组件 owner：AI 平台团队
- 变更内容：新增 `rules/verify-or-review-before-delivery.md`（package：`build/EA-20261022-04/`）
- 验收清单：目录与 manifest 对账、record approved 与 proposal/ai_form 一致、frontmatter 含 asset_id、无敏感信息、无 record 原文混入、语义保持对照通过、触发样例通过
- 回滚方式：revert 合入 PR；已安装环境删除 `~/.claude/rules/verify-or-review-before-delivery.md`

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-04 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-04，2026-10-22 approved 入库。record：`assets/20261022-1705-ai-public-rules/EA-20261022-04-verify-or-review-before-delivery.md`。provenance 仅记录于本文件，artifact 不含。
