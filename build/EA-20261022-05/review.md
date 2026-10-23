# 组件评审清单 · subtask-acceptance-checklist（EA-20261022-05）

> 供组件 owner 评审使用。全部勾选且结论为"通过"后，方可合入 `rules/` 并按 `install.md` 安装。

## 1. 来源与映射

- [ ] build-manifest 的 asset_id / proposal_id / ai_form 与 record 完全一致，record `status: approved`
- [ ] 未修改 record 的 statement / evidence / mapping / 分类结论
- [ ] 目标层级（公共级）与建议安装范围（用户级 rules）匹配

## 2. 语义保持

- [ ] `implementation.md` 语义保持对照表覆盖 statement 全部 7 条结论
- [ ] 抽查 3 条以上结论，artifact 原文可逐条对应，无遗漏
- [ ] artifact 未新增 record 之外的验收清单字段（仅交付物、通过条件、验证方式三项最小内容）
- [ ] 完成判定仍为"每个已下发子任务的任务包中都能定位到验收清单，且条目可逐项判定通过或失败"

## 3. 形态质量

- [ ] 全文为祈使句，每条一句可判定动作
- [ ] frontmatter 含 `asset_id: EA-20261022-05` 与 `ai_form: Rule`
- [ ] 未设置 `paths`，规则覆盖全部派单场景
- [ ] "缺少验收清单不得下发/不得执行""校验拦截即不合格""父任务目标不替代子任务清单"可逐项判定

## 4. 安全与合规

- [ ] artifact 无密钥/令牌/凭证；无邮箱等个人信息
- [ ] artifact 不含 record 原文结构（`## 出处与理由`）
- [ ] provenance 仅存在于 `implementation.md`

## 5. 去重与挂接

- [ ] 已比对 `~/.claude/rules/` 现有规则，无子任务验收清单语义重复
- [ ] 与 EA-20261022-04（产出交付前验证或评审）的衔接方式已在 `implementation.md` 说明：本规则提供清单，EA-04 要求按清单自查与独立复核

## 6. 测试与回滚

- [ ] `tests/trigger-cases.md` 10 例判定通过，覆盖最小内容/退回/字段校验/边界/衔接
- [ ] `validate_build.py` exit 0
- [ ] `install.md` 步骤与回滚可执行，且本包未实际安装

## 审批

- 结论：通过 / 修改后通过 / 退回（附意见）
- 组件 owner：
- 日期：
- 意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
