# 组件评审清单 · no-auto-external-actions（EA-20261022-03）

> 供组件 owner 评审使用。全部勾选且结论为"通过"后，方可合入 `rules/` 并按 `install.md` 安装。

## 1. 来源与映射

- [ ] build-manifest 的 asset_id / proposal_id / ai_form 与 record 完全一致，record `status: approved`
- [ ] 未修改 record 的 statement / evidence / mapping / 分类结论
- [ ] 目标层级（公共级）与安装范围（用户级 rules）匹配

## 2. 语义保持

- [ ] `implementation.md` 语义保持对照表覆盖 statement 全部 6 条结论
- [ ] 抽查 3 条以上结论，artifact 原文可逐字对应，无遗漏
- [ ] artifact 未新增 record 之外的结论（未列举平台清单、未指定 permission/hook 具体配置、未定义升级规则）
- [ ] 完成判定仍为"执行记录中存在人的明确确认，且无绕过拦截的配置改动"

## 3. 形态质量

- [ ] 全文为祈使句，一条规则一个可判定动作
- [ ] frontmatter 含 `asset_id: EA-20261022-03` 与 `ai_form: Rule`
- [ ] 未设置 `paths`，规则在任意会话均加载
- [ ] "对外动作"按结果判定边界，而非按平台名单

## 4. 安全与合规

- [ ] artifact 无密钥/令牌/凭证；无邮箱等个人信息
- [ ] artifact 不含 record 原文结构（`## 出处与理由`）
- [ ] provenance 仅存在于 `implementation.md`
- [ ] 本包未携带 `settings.json` 或 hook 配置改动

## 5. 去重与挂接

- [ ] 已比对 `~/.claude/rules/auto-mode-classifier.md`：其为拦截超时后的重试策略，与本禁令不重复、不冲突
- [ ] 与权限/hook 双重拦截机制的关系已在 `implementation.md` 说明（规则引用，不实现）

## 6. 测试与回滚

- [ ] `tests/trigger-cases.md` 10 例判定通过，覆盖对外范围/确认/不绕过/结果判定
- [ ] `validate_build.py` exit 0
- [ ] `install.md` 步骤与回滚可执行，且本包未实际安装

## 审批

- 结论：通过 / 修改后通过 / 退回（附意见）
- 组件 owner：
- 日期：
- 意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
