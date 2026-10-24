# TEST ONLY — synthetic 流程样例

> 本包由构造材料生成，仅用于验证 A/B 流程；**不得作为真实工程结论，也不得安装到生产环境**。已从生产安装点撤出，最终组件在 `samples/synthetic/`。

# 组件 owner 评审清单 · EA-20261022-07（Memory）

- 评审对象：`build/EA-20261022-07/`（HBM 项目 memory 条目 `hbm3e-dft-env-baseline.md`）
- 建议评审人：HBM 项目负责人 / DFT 领域 owner
- 评审日期：待填

## A. 对账与合法性

- [ ] `build-manifest.json` 的 asset_id / proposal_id / ai_form 与 record 一致（EA-20261022-07 / 20261022-1705-hbm3e-dft-meeting / Memory）
- [ ] record 状态为 approved（2026-10-22），未被本包修改
- [ ] `validate_build.py --assets-repo D:\Project\eng-knowledge-assets` exit 0，无 fail、无 warn

## B. 语义保持

- [ ] 语义保持对照表覆盖 statement 全部 6 项结论
- [ ] 三参数取值 V0.9 / 2 个 spare row / 1:4 与 record 一致，未换算或补充
- [ ] 两条使用约束（评估前提、失效重核）完整保留
- [ ] 条目未扩写成 DFT 领域通用结论，仍限定 HBM3E 项目
- [ ] 不含 record 的「出处与理由」原文结构

## C. 独立成立性

- [ ] 遮住 record 只读条目，可回答三参数、约束对象与复核条件（`tests/independent-check.md` 6/6）
- [ ] frontmatter 含 asset_id 与 `ai_form: Memory`，provenance 注释在文末

## D. 落位与环境

- [ ] 安装位置认可：`~/.claude/projects/<hbm-project-slug>/memory/`（推荐，文档化载入点）或项目内 `.claude/memory/`（仅当项目实际使用该载入点）
- [ ] 确认 HBM 项目 memory 无同义条目、无与项目 CLAUDE.md 重复的表述
- [ ] 条目含项目内环境信息，确认不含保密受限内容、可写入项目 memory

## E. 发布与回滚

- [ ] 安装由人执行，未由技能 B 自动落盘
- [ ] `install.md` 的回滚步骤可用
- [ ] 同意合入 `components/` 后写回 record 的 `implementation` 字段（仅该字段）

## 结论

- [ ] 通过
- [ ] 需修改（问题记录在下方）

评审意见：

## 独立复核记录
- 2026-10-22：主会话复跑 `validate_build.py`，9/9 exit 0；独立审计 agent 复核语义保持、测试覆盖与安装/回滚，无 FAIL；本包未实际安装，record 未修改。
