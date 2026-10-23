# 组件评审清单 · no-raw-records-in-memory（EA-20261022-06）

> 供组件 owner 评审使用。全部勾选且结论为"通过"后，方可合入 `rules/` 并按 `install.md` 安装。

## 1. 来源与映射

- [ ] build-manifest 的 asset_id / proposal_id / ai_form 与 record 完全一致，record `status: approved`
- [ ] 未修改 record 的 statement / evidence / mapping / 分类结论
- [ ] 目标层级（公共级）与建议安装范围（用户级 rules）匹配

## 2. 语义保持

- [ ] `implementation.md` 语义保持对照表覆盖 statement 全部 7 条结论
- [ ] 抽查 3 条以上结论，artifact 原文可逐条对应，无遗漏
- [ ] artifact 未新增 record 之外的载体类型、原始记录类型或豁免情形
- [ ] 完成判定仍为"每段内容都能回答'这是提炼后的结论吗'，原始记录仅以出处引用形式出现"

## 3. 形态质量

- [ ] 全文为祈使句，每条一句可判定动作
- [ ] frontmatter 含 `asset_id: EA-20261022-06` 与 `ai_form: Rule`
- [ ] 未设置 `paths`，规则覆盖 CLAUDE.md、rules 文件、memory 条目与知识资产正文
- [ ] "先粘贴再补结论""只摘一小段""当次使用可豁免"三个边界可逐项判定

## 4. 安全与合规

- [ ] artifact 无密钥/令牌/凭证；无邮箱等个人信息
- [ ] artifact 不含 record 原文结构（`## 出处与理由`）
- [ ] provenance 仅存在于 `implementation.md`

## 5. 自身合规（本条规则的特殊检查）

- [ ] artifact 正文为提炼后的规则文本，不粘贴任何会议、聊天或日志原文（不违反自身规则）
- [ ] artifact 未把原始记录当作示例内联（示例仅以类型名指称，如"逐字稿""调试日志"）
- [ ] `tests/trigger-cases.md` 的样例描述同样不含原始记录内容

## 6. 去重与挂接

- [ ] 已比对 `~/.claude/rules/` 现有规则，无长期记忆写入形态语义重复
- [ ] 与 `~/.claude/skills/` 中 memory 相关组件的挂接在 `implementation.md` 说明（本规则不另造 memory 组件）

## 7. 测试与回滚

- [ ] `tests/trigger-cases.md` 11 例判定通过，覆盖载体范围/原始记录范围/两个边界/当次使用
- [ ] `validate_build.py` exit 0
- [ ] `install.md` 步骤与回滚可执行，且本包未实际安装

## 审批

- 结论：通过 / 修改后通过 / 退回（附意见）
- 组件 owner：
- 日期：
- 意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
