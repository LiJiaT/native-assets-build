# synthetic 示例（test-only）

本目录只放由构造材料生成、用于流程验证的组件实现。

- 不得安装到生产环境；`build-manifest.json` 中 `release_channel: test-only`、`install_target: test-sandbox`。
- 最终发布证据（`--release`）要求 `tests/results.json` 与 `review.json`；本目录组件不满足发布条件，默认不发布。
- 真实资产请回到 `eng-knowledge-assets` 重新核验来源并走审批。
