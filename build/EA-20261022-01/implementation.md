# 实现说明 · EA-20261022-01 · 资产分类体系定为 9 领域平铺 + 2 项目正交

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-01 |
| proposal_id | 20261022-1705-decision-domain-taxonomy |
| ai_form | Memory（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 公共级 / 无 / 无 |
| record | eng-knowledge-assets `assets/20261022-1705-decision-domain-taxonomy/EA-20261022-01-asset-domain-taxonomy.md`（approved 2026-10-22） |
| 组件 owner | AI 平台团队（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/memory-entry.md` → 建议安装到 `~/.claude/CLAUDE.md` 受管区块（项目 memory 为降级方案） |

## 语义保持对照

record 的 statement 为决策记忆结构（决策 / 背景 / 选项 / 取舍 / 证据 / 日期）。下表逐条列出可复用结论及其在 memory 条目中的承载位置；条目按「决策+背景 / 选项+取舍 / 证据+日期」压缩为三段。

| # | statement 结论 | memory 条目承载位置 |
|---|---|---|
| 1 | 决策：分类元数据采用「9 领域平铺 + 2 固定项目 + 四维正交」的自建结构，不引入外部知识收集项目的细粒度标签体系 | 第 1 段首句（加粗「决策」） |
| 2 | 背景：最初方案是复用外部知识收集项目（论文库 / 公众号 / GitHub radar 三项目共享）的统一标签体系——8 个顶层主题 + 72 个子标签，期望收集端与资产治理端共用 | 第 1 段「背景」句 |
| 3 | 选项 1：复刻外部统一标签体系——与收集侧天然一致，检索粒度最细 | 第 2 段「选项一」 |
| 4 | 选项 2：自建平铺结构——9 个专业领域平铺（架构、设计、验证、时序、DFT、后仿、Firmware、模拟、后端）；项目固定为 LPDDR6、HBM 两个；领域与项目正交（项目横跨多个领域，不做父子嵌套）；资产四维正交——形态 ⊥ 领域 ⊥ 项目 ⊥ 层级 | 第 2 段「选项二」 |
| 5 | 取舍：选方案 2；外部体系是知识收集视角而非资产治理视角，照其细分没有意义；72 个子标签粒度过细、维护成本高、owner 难指派；细粒度检索更准但收益不及维护成本；平铺结构 owner 好指派、好演进 | 第 2 段「取舍」句 |
| 6 | 代价：让出细粒度检索精度，换取治理上的可维护与可演进 | 第 2 段末句 |
| 7 | 证据：9 领域划分已写入《AI 公共规范 v0.5》1.2 节，2026-10-22 由团队负责人直接在文档中改定，属团队级既定结构 | 第 3 段「证据」句 |
| 8 | 日期：2026-10-22（评审结论、最终决策与规范落定同日完成） | 第 3 段「日期」句 |

## 设计取舍

1. **三段式承载决策记忆五要素**：第 1 段决策+背景、第 2 段选项+取舍+代价、第 3 段证据+日期；要素用加粗行内标签标识，既满足 playbook「1-3 段」与五要素要求，也不复制 record 的 bullet 结构。
2. **只写 statement，不搬 evidence 的推导**：record「出处与理由」中"后续新增领域/项目/维度的提案需以此为基线"属入库理由中的推论，不是 statement 结论，故不写入条目，避免语义增量；若团队要强制该约束，应另立 Rule。
3. **枚举值完整保留**：9 个领域名与 2 个项目名逐个列出，四维正交用「形态 ⊥ 领域 ⊥ 项目 ⊥ 层级」原式表达——这些是后续资产元数据的合法取值，压缩会损失可执行性。
4. **frontmatter 只留检索与归属字段**：asset_id / ai_form / title / layer / project / domains / approved_date；provenance 以 HTML 注释置于文末，便于溯源而不干扰条目阅读。
5. **去重扫描**：`~/.claude/memory/` 目录不存在，`~/.claude/CLAUDE.md` 无领域划分或分类体系相关条目；`eng-asset-ai-components/components/` 为空，无重复组件。本条为资产治理体系的首条分类记忆，无冲突。

## 独立成立性检查结果

对象：`tests/independent-check.md`。步骤为遮住 record、只读 `artifacts/memory-entry.md`，逐条核对 8 项可复用结论是否可复述。

- 结果：8/8 项结论均可从条目独立复述，无丢失、无改写；条目未出现"见 record / 见上文"等外部依赖表述。
- 可独立回答的问题：分类结构是什么（9 领域+2 项目+四维正交）、为何不用外部 72 子标签体系、放弃了什么、证据落在哪份文档、决策日期。
- 未通过项：无。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-01
- 来源提案 ID：20261022-1705-decision-domain-taxonomy
- 目标组件形态：Memory
- 目标层级 / 领域 / 项目：公共级 / 无 / 无
- 组件 owner：AI 平台团队
- 变更内容：新增 memory 条目 `asset-taxonomy.md`（package：`build/EA-20261022-01/`）
- 验收清单：目录与 manifest 对账、record approved 且 proposal/ai_form 一致、frontmatter 含 asset_id 与 ai_form、无敏感信息、无 record 原文结构、语义保持对照通过、独立成立性检查通过
- 回滚方式：从安装位置删除该 memory 条目；如合入 repo，revert 合入 PR

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-01 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-01，2026-10-22 approved 入库。record：`assets/20261022-1705-decision-domain-taxonomy/EA-20261022-01-asset-domain-taxonomy.md`。provenance 仅记录于本文件与 artifact 的 HTML 注释，正文不含 record 原文标题结构。
