# TEST ONLY — synthetic 流程样例

> 本包由构造材料生成，仅用于验证 A/B 流程；**不得作为真实工程结论，也不得安装到生产环境**。已从生产安装点撤出，最终组件在 `samples/synthetic/`。

# 组件 owner 评审清单 · EA-20261022-09（Memory）

- 评审对象：`build/EA-20261022-09/`（领域级 memory 条目 `hbm3e-stack-level-repair-decision.md`）
- 建议评审人：DFT 领域 owner / HBM 项目负责人
- 评审日期：待填

## A. 对账与合法性

- [ ] `build-manifest.json` 的 asset_id / proposal_id / ai_form 与 record 一致（EA-20261022-09 / 20261022-1705-hbm3e-dft-meeting / Memory）
- [ ] record 状态为 approved（2026-10-22），未被本包修改
- [ ] `validate_build.py --assets-repo D:\Project\eng-knowledge-assets` exit 0，无 fail、无 warn

## B. 语义保持

- [ ] 语义保持对照表覆盖 statement 全部 12 项结论
- [ ] 方案 A / B 定义、三条依据、代价与收益、生效复核条件逐项保留
- [ ] "方案 A 在结构上不成立""覆盖率天花板"等强结论未被弱化
- [ ] 环境前提数值（V0.9 / 2 spare row / 1:4）与 record 一致
- [ ] 副标签内容未被擅自实现为 Rule 或独立知识条目
- [ ] 不含 record 的「出处与理由」原文结构

## C. 独立成立性

- [ ] 遮住 record 只读条目，可回答"为何 stack-level""A 为何不成立""何时重评"（`tests/independent-check.md` 12/12）
- [ ] frontmatter 含 asset_id 与 `ai_form: Memory`，provenance 注释在文末

## D. 落位与环境

- [ ] 安装位置认可：`~/.claude/projects/<project-slug>/memory/`（默认可验证载入点）或 owner 指定的 DFT 领域级载体；不自建 `~/.claude/memory/domains/`
- [ ] 条目保留 HBM3E/98%+ 等来源证据，不做无授权的泛化改写；项目级安装时确认与 EA-07 基线条目无重复
- [ ] 领域级共享范围符合 record 的 layer 结论（领域级）

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
