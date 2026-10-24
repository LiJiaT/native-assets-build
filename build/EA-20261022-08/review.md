# TEST ONLY — synthetic 流程样例

> 本包由构造材料生成，仅用于验证 A/B 流程；**不得作为真实工程结论，也不得安装到生产环境**。已从生产安装点撤出，最终组件在 `samples/synthetic/`。

# 组件评审清单 · bist-scan-same-cycle-exclusion（EA-20261022-08）

> 供组件 owner 评审使用。全部勾选且结论为"通过"后，方可合入 `rules/` 并按 `install.md` 安装。

## 1. 来源与映射

- [ ] build-manifest 的 asset_id / proposal_id / ai_form 与 record 完全一致，record `status: approved`
- [ ] 未修改 record 的 statement / evidence / mapping / 分类结论
- [ ] 目标层级（领域级，DFT / 时序）与安装范围匹配：推荐用户级 rules（跨 DFT 项目生效），或按 owner 指定装单个 DFT 项目级
- [ ] project 仅作来源记录（HBM），安装范围按领域计，未按项目收窄

## 2. 语义保持

- [ ] `implementation.md` 语义保持对照表覆盖 statement 全部 5 条结论
- [ ] 抽查 3 条以上结论，artifact 原文可逐条对应，无遗漏
- [ ] artifact 未新增 record 之外的时序约束（未引入额外使能信号、未规定切换周期数）
- [ ] "边界"仍为"只约束同周期拉高，不禁止时间上分段使用"，未扩大为禁止交替使用

## 3. 形态质量

- [ ] 规则与检查方式为祈使句，每条一句可判定动作
- [ ] frontmatter 含 `asset_id: EA-20261022-08` 与 `ai_form: Rule`
- [ ] `paths` 处理已在 `implementation.md` 说明（按设计范围而非文件类型生效）
- [ ] "同周期高电平重叠"可逐周期判定，不依赖主观判断

## 4. 安全与合规

- [ ] artifact 无密钥/令牌/凭证；无邮箱等个人信息
- [ ] artifact 不含 record 原文结构（`## 出处与理由`）
- [ ] artifact 不含会议纪要原文或逐字稿
- [ ] provenance 仅存在于 `implementation.md`

## 5. 去重与挂接

- [ ] 已比对 `~/.claude/rules/` 现有规则与目标 DFT 项目 `.claude/rules/`，无 bist/scan 时序互斥重复实现
- [ ] 副标签（知识库）的机理内容承载方式已在 `implementation.md` 说明：由「违反后果」节承载，未另造 memory 组件

## 6. 测试与回滚

- [ ] `tests/trigger-cases.md` 10 例判定通过，覆盖同周期违规、波形重叠、约束评审、误诊拦截、领域范围、分段使用边界
- [ ] `validate_build.py` exit 0
- [ ] `install.md` 步骤与回滚可执行，且本包未实际安装

## 审批

- 结论：通过 / 修改后通过 / 退回（附意见）
- 组件 owner（DFT 领域 owner）：
- 日期：
- 意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
