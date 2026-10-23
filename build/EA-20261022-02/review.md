# 组件评审清单 · verilog-filelist-sync（EA-20261022-02）

> 供组件 owner 评审使用。全部勾选且结论为"通过"后，方可合入 `rules/` 并按 `install.md` 安装。

## 1. 来源与映射

- [ ] build-manifest 的 asset_id / proposal_id / ai_form 与 record 完全一致，record `status: approved`
- [ ] 未修改 record 的 statement / evidence / mapping / 分类结论
- [ ] 目标层级（公共级）与安装范围（用户级 rules）匹配

## 2. 语义保持

- [ ] `implementation.md` 语义保持对照表覆盖 statement 全部 7 条结论
- [ ] 抽查 3 条以上结论，artifact 原文可逐字对应，无遗漏
- [ ] artifact 未新增 record 之外的结论（filelist 命名/路径、SystemVerilog 等扩展类型、hook 具体命令均未自行补写）
- [ ] 完成判定仍为"hook 一致性校验通过"

## 3. 形态质量

- [ ] 全文为祈使句，一条规则一个可判定动作
- [ ] frontmatter 含 `asset_id: EA-20261022-02` 与 `ai_form: Rule`
- [ ] `paths` 仅 `**/*.v`；owner 需确认团队 SystemVerilog（`.sv`）文件是否也应触发，未确认前不擅自扩展
- [ ] 触发与不触发条款可判定，不存在"视情况"类模糊表述

## 4. 安全与合规

- [ ] artifact 无密钥/令牌/凭证；无邮箱等个人信息
- [ ] artifact 不含 record 原文结构（`## 出处与理由`）
- [ ] provenance 仅存在于 `implementation.md`

## 5. 去重与挂接

- [ ] 已比对 `~/.claude/rules/` 现有 4 条规则，无语义重复
- [ ] 与 filelist 一致性 hook 的关系已在 `implementation.md` 说明；确认目标环境 hook 是否已存在

## 6. 测试与回滚

- [ ] `tests/trigger-cases.md` 9 例判定通过，边界覆盖触发/同次变更/一致/校验/不触发
- [ ] `validate_build.py` exit 0
- [ ] `install.md` 步骤与回滚可执行，且本包未实际安装

## 审批

- 结论：通过 / 修改后通过 / 退回（附意见）
- 组件 owner：
- 日期：
- 意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
