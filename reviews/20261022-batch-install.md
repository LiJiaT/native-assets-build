# 实现评审与安装记录 · 2026-10-22

- 审批人：LiJiaT
- 审批日期：2026-10-22
- 审批结论：9 个实现包全部批准合入并安装
- 质量门：validate_build.py 9/9 exit 0；独立审计无 FAIL

## 明细

| asset_id | 形态 | 合入路径 | 安装位置 |
|---|---|---|---|
| EA-20261022-01 | Memory | components/asset-taxonomy.md | ~/.claude/CLAUDE.md#asset-taxonomy (EA-20261022-01) |
| EA-20261022-02 | Rule | rules/verilog-filelist-sync.md | ~/.claude/rules/verilog-filelist-sync.md |
| EA-20261022-03 | Rule | rules/no-auto-external-actions.md | ~/.claude/rules/no-auto-external-actions.md |
| EA-20261022-04 | Rule | rules/verify-or-review-before-delivery.md | ~/.claude/rules/verify-or-review-before-delivery.md |
| EA-20261022-05 | Rule | rules/subtask-acceptance-checklist.md | ~/.claude/rules/subtask-acceptance-checklist.md |
| EA-20261022-06 | Rule | rules/no-raw-records-in-memory.md | ~/.claude/rules/no-raw-records-in-memory.md |
| EA-20261022-07 | Memory | components/hbm3e-dft-env-baseline.md | ~/.claude/projects/D--Project/memory/hbm3e-dft-env-baseline.md |
| EA-20261022-08 | Rule | rules/bist-scan-same-cycle-exclusion.md | ~/.claude/rules/bist-scan-same-cycle-exclusion.md |
| EA-20261022-09 | Memory | components/hbm3e-stack-level-repair-decision.md | ~/.claude/projects/D--Project/memory/hbm3e-stack-level-repair-decision.md |

## owner 待办

- EA-02：确认 `paths` 是否需覆盖 SystemVerilog（`**/*.sv`）；未确认前保持 `**/*.v`。
- EA-08：当前按用户级 rules 安装；如需限定单个 DFT 项目，按 install.md 改为项目级。
- EA-07/09：HBM 项目目录/DFT 领域级 memory 载体本机不存在，当前落 D--Project 项目 memory；载体建立后迁移。
