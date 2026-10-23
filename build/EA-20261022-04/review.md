# 组件评审清单 · verify-or-review-before-delivery（EA-20261022-04）

> 供组件 owner 评审使用。全部勾选且结论为"通过"后，方可合入 `rules/` 并按 `install.md` 安装。

## 1. 来源与映射

- [ ] build-manifest 的 asset_id / proposal_id / ai_form 与 record 完全一致，record `status: approved`
- [ ] 未修改 record 的 statement / evidence / mapping / 分类结论
- [ ] 目标层级（公共级）与安装范围（用户级 rules）匹配

## 2. 语义保持

- [ ] `implementation.md` 语义保持对照表覆盖 statement 全部 7 条结论
- [ ] 抽查 3 条以上结论，artifact 原文可逐字对应，无遗漏
- [ ] artifact 未新增 record 之外的结论（未内置验收清单模板、未定义独立性等级、未绑定特定工具）
- [ ] 完成判定仍为"可逐项追溯的自查记录与独立复核记录，或对应评审结论"

## 3. 形态质量

- [ ] 全文为祈使句，一条规则一个可判定动作
- [ ] frontmatter 含 `asset_id: EA-20261022-04` 与 `ai_form: Rule`
- [ ] 未设置 `paths`，规则覆盖全部产出类型
- [ ] "自查不替代独立复核""未完成不得标记完成"可逐项判定

## 4. 安全与合规

- [ ] artifact 无密钥/令牌/凭证；无邮箱等个人信息
- [ ] artifact 不含 record 原文结构（`## 出处与理由`）
- [ ] provenance 仅存在于 `implementation.md`

## 5. 去重与挂接

- [ ] 已比对 `~/.claude/rules/` 现有 4 条规则，无交付前自查/复核语义重复
- [ ] 与项目既有验收清单的挂接方式已在 `implementation.md` 说明（规则要求"按验收清单"，不内置清单）

## 6. 测试与回滚

- [ ] `tests/trigger-cases.md` 9 例判定通过，覆盖自查形式/独立复核/转评审/完成标记
- [ ] `validate_build.py` exit 0
- [ ] `install.md` 步骤与回滚可执行，且本包未实际安装

## 审批

- 结论：通过 / 修改后通过 / 退回（附意见）
- 组件 owner：
- 日期：
- 意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
