---
asset_id: EA-20261022-07
ai_form: Memory
title: HBM3E DFT 环境基线：V0.9 工具链与修复资源
layer: 项目级
project: HBM
domains:
- DFT
approved_date: '2026-10-22'
provenance_status: synthetic
provenance_note: 由构造的 HBM3E DFT 会议纪要生成，仅用于验证资产化流程，不代表真实项目结论
release_channel: test-only
source_record: assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-07-hbm3e-dft-env-baseline.md
asset_type: memory
---
**HBM3E 项目当前 DFT debug 所依据的环境基线**，共三个参数（截至 2026-10-20）：工具链版本为 **V0.9**，该版本下 `bist_collars` 数量受限——MBIST collar 的可用数量由工具链版本决定，不能按理论最大并发去规划 MBIST 配置或覆盖率目标；TSV 通道修复资源为 **2 个 spare row**，HBM TSV 通道 repair 只有 2 个 spare row，修复能力上限由 spare row 数量决定；PHY 侧修复粒度为 **1:4**，修复资源按「1 份修复资源对应 4 个单元」的粒度划分，评估 PHY 侧可修复比例时必须按该粒度折算，不能按单 lane 粒度估算。

使用约束：任何针对 HBM3E 的 MBIST 覆盖率评估、fault sim 配置、repair 方案讨论，都必须以这三个参数为前提；脱离该基线的结论不可比。

这三个参数均绑定当前工具链版本与当前 die 配置。工具链升级、spare row 数量变化或 PHY 修复粒度调整后，本基线需重新核实，旧结论不得直接沿用。

<!-- 来源: asset EA-20261022-07, 2026-10-22 入库 -->
