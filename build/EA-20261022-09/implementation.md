# TEST ONLY — synthetic 流程样例

> 本包由构造材料生成，仅用于验证 A/B 流程；**不得作为真实工程结论，也不得安装到生产环境**。已从生产安装点撤出，最终组件在 `samples/synthetic/`。

# 实现说明 · EA-20261022-09 · HBM3E 修复层级决策：选 stack-level

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-09 |
| proposal_id | 20261022-1705-hbm3e-dft-meeting |
| ai_form | Memory（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 领域级 / DFT、设计 / HBM |
| record | eng-knowledge-assets `assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-09-stack-level-repair-decision.md`（approved 2026-10-22） |
| 组件 owner | DFT 领域 owner（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/memory-entry.md` → 建议安装名 `hbm3e-stack-level-repair-decision.md`（DFT 领域级 memory 或 HBM 项目 memory） |

## 语义保持对照

record 的 statement 为决策记忆结构（背景 / 选项 / 取舍 / 证据 / 生效条件 / 日期）。下表逐条列出可复用结论及其在 memory 条目中的承载位置；条目按「背景+前提 / 选项+取舍 / 证据+生效条件+日期」压缩为三段。

| # | statement 结论 | memory 条目承载位置 |
|---|---|---|
| 1 | 背景：HBM3E 堆叠 die 的 MBIST 修复覆盖率上不去，团队争论修复动作放哪一层——controller 统一控制各 die 修复资源，还是下沉到 stack 内部 | 第 1 段「背景」句 |
| 2 | 当时环境前提：V0.9 工具链（`bist_collars` 数量受限）、TSV 通道 repair 仅 2 个 spare row、PHY 侧修复粒度 1:4 | 第 1 段末句 |
| 3 | 方案 A（controller-level repair）：controller 统一控制堆叠各 die 的修复资源，测试入口单一、控制集中 | 第 2 段方案 A 句 |
| 4 | 方案 B（stack-level repair）：修复在 stack 内部完成，controller 只发起测试 | 第 2 段方案 B 句 |
| 5 | 取舍结论：最终选方案 B（stack-level） | 第 2 段「最终选方案 B」 |
| 6 | 依据一（可达性）：PHY 侧 spare row 在 controller level 无法访问；方案 A 触达不到这部分资源，PHY 侧可修复单元形成覆盖率天花板，方案 A 在结构上不成立 | 第 2 段「其一，可达性」 |
| 7 | 依据二（协议一致性）：stack-level 与 base die 测试协议一致，不需为 repair 额外引入跨层控制协议 | 第 2 段「其二，协议一致性」 |
| 8 | 依据三（既有证据）：HBM3 项目走过 stack-level，修复覆盖率 98%+ | 第 2 段「其三，既有证据」 |
| 9 | 代价与收益：放弃 controller-level 的集中控制与单一测试入口；换来 PHY 侧 spare row 真实可达性与 base die 测试协议一致性 | 第 2 段末句 |
| 10 | 证据：PHY spare row 在 controller level 不可访问（结构性限制）、与 base die 协议一致、HBM3 实测 98%+ | 第 3 段「证据与生效条件」句 |
| 11 | 生效条件与复核点：建立在「PHY 侧 spare row 必须由 stack 自身修复逻辑访问」的结构前提上；若 PHY 修复资源、修复粒度（当前 1:4）或 controller 访问路径变化，需重新评估前提，不得直接沿用 | 第 3 段复核点句 |
| 12 | 日期：2026-10-20（HBM3E DFT debug 复盘会） | 第 3 段「日期」句 |

## 设计取舍

1. **三段式承载决策记忆六要素**：背景与环境前提合段（前提是决策的比较条件），选项与取舍合段（三条依据紧跟结论），证据与生效条件、日期合段；用加粗行内标签保留要素可识别性。
2. **"方案 A 结构上不成立"照原强度保留**：这是取舍的核心结论，弱化为"较难"会改变语义；同样保留"覆盖率天花板"表述。
3. **环境前提压缩为一句**：V0.9 / 2 个 spare row / 1:4 是决策条件而非本条主体，完整取值保留但不展开机理（机理已在 EA-20261022-07 基线条目中承载，本条引用不复制）。
4. **副标签不改变主形态**：record 副标签为「工程规则 / 知识库」。其中"可达性优先于控制集中度"若要变成强制规则需另立 Rule、PHY spare row 不可达等机理若要独立成知识库条目需回技能 A 提案；本包只按主形态 Memory 实现，不越权扩展（实现备注，不改资产语义）。
5. **去重扫描**：DFT 领域级 memory 与 HBM 项目 memory 当前均无条目，`eng-asset-ai-components/components/` 为空；与 EA-07 条目无重叠（EA-07 承载参数事实，本条承载层级决策并引用同一前提）。

## 独立成立性检查结果

对象：`tests/independent-check.md`。步骤为遮住 record、只读 `artifacts/memory-entry.md`，逐条核对 12 项可复用结论。

- 结果：12/12 项结论可独立复述；选项、三条依据、代价与收益、生效复核条件均无丢失。
- 可独立回答的问题：为什么 repair 放在 stack 侧、controller-level 为何不成立、替代方案是什么、放弃与换取了什么、什么条件下要重评。
- 未通过项：无。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-09
- 来源提案 ID：20261022-1705-hbm3e-dft-meeting
- 目标组件形态：Memory
- 目标层级 / 领域 / 项目：领域级 / DFT、设计 / HBM
- 组件 owner：DFT 领域 owner
- 变更内容：新增领域级 memory 条目 `hbm3e-stack-level-repair-decision.md`（package：`build/EA-20261022-09/`）
- 验收清单：目录与 manifest 对账、record approved 且 proposal/ai_form 一致、frontmatter 含 asset_id 与 ai_form、无敏感信息、无 record 原文结构、语义保持对照通过、独立成立性检查通过
- 回滚方式：从领域级/项目 memory 删除该条目；如合入 repo，revert 合入 PR

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-09 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-09，2026-10-22 approved 入库。record：`assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-09-stack-level-repair-decision.md`。provenance 仅记录于本文件与 artifact 的 HTML 注释，正文不含 record 原文标题结构。
