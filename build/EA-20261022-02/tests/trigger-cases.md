# 触发样例 · verilog-filelist-sync（EA-20261022-02）

被测实现物：`artifacts/rule-verilog-filelist-sync.md`

## 判定方法

1. 对每条样例，由复核者只读规则全文（不看 asset record），判定是否命中规则，并写出命中后应执行的动作。
2. 判定与下表"期望判定 / 期望行为"一致记 PASS；出现"命中但无动作"或"不命中却要求改 filelist"记 FAIL。
3. 规则只对特定文件类型生效（`paths: ["**/*.v"]`），样例均按用户级 rules 加载后的人工/模型判定执行。

## 应命中

| 编号 | 触发样例（变更描述） | 期望判定 | 期望行为 |
|---|---|---|---|
| H1 | 在 `rtl/uart/` 新增 `uart_rx.v`，未改该模块 filelist | 命中 | 判为违规：要求在同一次变更中把 `uart_rx.v` 登记进该模块 filelist |
| H2 | 修改 `rtl/spi/spi_top.v` 的内部逻辑，目录文件集合未变 | 命中 | 确认 filelist 与目录实际文件集合一致，并在提交前执行 hook 一致性校验 |
| H3 | 新增 `rtl/dma/dma_ch.v` 且已更新 filelist，但未运行 hook 校验 | 命中 | 判为变更未完成：先跑 hook 一致性校验，通过后再提交 |
| H4 | 目录中已无 `dma_old.v`，filelist 仍保留其条目；本次变更新增了一个 `.v` | 命中 | 判为清单不一致：删除 `dma_old.v` 残留条目、登记新增文件后再提交 |
| H5 | 先单独提交 `.v` 代码变更，再另起一次提交补 filelist | 命中 | 判为违规：要求 filelist 更新与代码变更合并为同一次变更 |

## 不应命中

| 编号 | 触发样例（变更描述） | 期望判定 | 期望行为 |
|---|---|---|---|
| N1 | 只修改 `docs/uart_spec.md` | 不命中 | 不要求改 filelist，不提及本规则 |
| N2 | 只修改 `scripts/gen_filelist.py` 的日志格式 | 不命中 | 不要求改 filelist |
| N3 | 只修改 CI 配置 `.github/workflows/ci.yml` | 不命中 | 不要求改 filelist |
| N4 | 只修改 filelist（本次没有任何 `.v` 文件新增或更新） | 不命中 | 不触发本规则；按 filelist 自身变更流程处理 |

## 执行结果

- 逐例对照规则文本判定：9/9 与期望一致（H1-H5 均命中并给出对应动作；N1-N4 均不命中）。
- 结论：触发边界与规则第 1、5 条一致；完成判定与 hook 校验条款一致。

## 独立复核
- 2026-10-22：独立审计 agent 复核样例覆盖与期望判定；主会话复跑 `validate_build.py` exit 0。
