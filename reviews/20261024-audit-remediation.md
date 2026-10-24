# 审计整改记录 · 2026-10-24

- 执行人：AI 平台团队（owner 授权）
- 依据：`eng-audit-20261023/audit-report.md`（IMPL-01…IMPL-15）

## 变更

1. **synthetic 隔离（IMPL-01/F11）**：`components/hbm3e-dft-env-baseline.md` 移入 `samples/synthetic/`；07/08/09 build 包标 `release_channel=test-only`、`install_target=test-sandbox`，install.md 增加 TEST ONLY 警告。
2. **来源标签（IMPL-02/F12）**：7 个最终组件补齐 `provenance_status`/`provenance_note`/`release_channel`/`source_record`；9 个 build artifact 同步补齐。
3. **manifest schema v2（IMPL-03…IMPL-12/F08–F16）**：增加 `source_record_sha256`、`source_content_sha256`、owner/layer/projects/domains、install_target、release_channel、producer、generated_by、review、validation。校验器会拒绝最小 record、正文篡改、错误来源、范围扩大、synthetic 进生产、隐藏文件、坏 YAML、逐字稿、空评审/FAIL 测试。
4. **发布证据（IMPL-06/F16）**：01–06 生成 `tests/results.json` 与 `review.json`，绑定 artifact hash 与独立 reviewer；`validate_build.py --release` 全通过。
5. **EA-08 范围（IMPL-14/F38）**：build 内推荐范围统一为项目级/领域级消费条件；synthetic 状态下仅 test-only，不再给生产安装二选一。

## 回滚

按 git 历史回退本提交；synthetic 文件不得直接恢复到 `components/` 生产目录。
