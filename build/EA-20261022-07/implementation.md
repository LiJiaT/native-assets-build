# 实现说明 · EA-20261022-07 · HBM3E DFT 环境基线：V0.9 工具链与修复资源

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-07 |
| proposal_id | 20261022-1705-hbm3e-dft-meeting |
| ai_form | Memory（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 项目级 / DFT / HBM |
| record | eng-knowledge-assets `assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-07-hbm3e-dft-env-baseline.md`（approved 2026-10-22） |
| 组件 owner | HBM 项目负责人（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/memory-entry.md` → 建议安装名 `<HBM 项目 memory>/hbm3e-dft-env-baseline.md` |

## 语义保持对照

record 的 statement 为知识库型：三个环境参数 + 两条使用约束。下表逐条列出可复用结论及其在 memory 条目中的承载位置；条目按「三参数 / 使用约束 / 失效条件」压缩为三段。

| # | statement 结论 | memory 条目承载位置 |
|---|---|---|
| 1 | HBM3E 项目当前 DFT debug 的环境基线共三个参数（截至 2026-10-20） | 第 1 段首句 |
| 2 | 工具链版本 V0.9；该版本下 `bist_collars` 数量受限——MBIST collar 可用数量由工具链版本决定，不能按理论最大并发规划 MBIST 配置或覆盖率目标 | 第 1 段第 1 个参数句 |
| 3 | TSV 通道修复资源 2 个 spare row；HBM TSV 通道 repair 只有 2 个 spare row，修复能力上限由 spare row 数量决定 | 第 1 段第 2 个参数句 |
| 4 | PHY 侧修复粒度 1:4；修复资源按「1 份修复资源对应 4 个单元」划分，评估 PHY 侧可修复比例必须按该粒度折算，不能按单 lane 粒度估算 | 第 1 段第 3 个参数句 |
| 5 | 使用约束：任何 HBM3E 的 MBIST 覆盖率评估、fault sim 配置、repair 方案讨论都必须以这三个参数为前提；脱离该基线的结论不可比 | 第 2 段 |
| 6 | 失效条件：三个参数均绑定当前工具链版本与当前 die 配置；工具链升级、spare row 数量变化或 PHY 修复粒度调整后需重新核实，旧结论不得直接沿用 | 第 3 段 |

## 设计取舍

1. **参数取值集中在一段**：三个参数是同时使用的前提，合并成一段便于一次加载；用粗体标出参数名与取值（V0.9、2 个 spare row、1:4）作为视觉锚点。
2. **负向边界原样保留**："不能按理论最大并发规划"与"不能按单 lane 粒度估算"是可复用结论的一部分（防误判），不是可省略的修饰语。
3. **使用约束与失效条件分段**：把"何时必须以此为前提"和"何时失效"从参数值中拆出，避免读者把 2026-10-20 的快照当作永久事实。
4. **角色限定为 HBM3E / 项目级**：条目不声明对 DFT 领域其他项目通用；具体 die 型号、工具名与命令 record 未给，不补全（补全即语义增量）。
5. **去重扫描**：HBM 项目 memory 目录当前无任何条目，`~/.claude/memory/` 不存在，`eng-asset-ai-components/components/` 为空，无重复组件。

## 独立成立性检查结果

对象：`tests/independent-check.md`。步骤为遮住 record、只读 `artifacts/memory-entry.md`，逐条核对可复用结论。

- 结果：6/6 项结论可独立复述；三个参数的取值、受限机理与两条使用约束均无丢失。
- 可独立回答的问题：当前基线是哪三个参数、各自约束了什么、什么评估必须以此为前提、何时需要重新核实。
- 未通过项：无。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-07
- 来源提案 ID：20261022-1705-hbm3e-dft-meeting
- 目标组件形态：Memory
- 目标层级 / 领域 / 项目：项目级 / DFT / HBM
- 组件 owner：HBM 项目负责人
- 变更内容：新增 HBM 项目 memory 条目 `hbm3e-dft-env-baseline.md`（package：`build/EA-20261022-07/`）
- 验收清单：目录与 manifest 对账、record approved 且 proposal/ai_form 一致、frontmatter 含 asset_id 与 ai_form、无敏感信息、无 record 原文结构、语义保持对照通过、独立成立性检查通过
- 回滚方式：从 HBM 项目 memory 目录删除该条目；如合入 repo，revert 合入 PR

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-07 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-07，2026-10-22 approved 入库。record：`assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-07-hbm3e-dft-env-baseline.md`。provenance 仅记录于本文件与 artifact 的 HTML 注释，正文不含 record 原文标题结构。
