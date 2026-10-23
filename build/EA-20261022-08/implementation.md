# 实现说明 · EA-20261022-08 · bist_en 与 scan_en 禁止同周期拉高

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-08 |
| proposal_id | 20261022-1705-hbm3e-dft-meeting |
| ai_form | Rule（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 领域级 / DFT、时序 / HBM（project 仅记录来源，共享范围按 DFT 领域计） |
| record | eng-knowledge-assets `assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-08-bist-scan-same-cycle-rule.md`（approved 2026-10-22） |
| 组件 owner | DFT 领域 owner（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/rule-bist-scan-same-cycle.md` → 建议安装名 `~/.claude/rules/bist-scan-same-cycle-exclusion.md`（或项目级 rules） |

## 语义保持对照

statement 的每条结论逐条落到 artifact，未增删语义。

| # | statement 结论（原文） | artifact 承载位置 |
|---|---|---|
| 1 | 规则：在同时包含 MBIST（bist）与 scan 的 DFT 时序约束中，`bist_en` 与 `scan_en` 不得在同一周期同时拉高，二者必须保持周期级互斥。 | `artifacts/rule-bist-scan-same-cycle.md` ›「## 规则」 |
| 2 | 适用范围：所有在 OCC 切换窗口内需要并存 repair/MBIST 时钟与 scan 时钟的 DFT 设计；来源场景是 HBM 堆叠 die 的 MBIST 修复，但机制不依赖具体项目。 | 「## 适用范围」（含"按 DFT 设计范围执行，不要按项目名收窄"） |
| 3 | 违反后果：repair clock 与 scan clock 在 OCC 期间冲突，导致该窗口内 bist 部分失效，表现为 MBIST 结果异常、修复覆盖率上不去；症状与"修复算法有缺陷"高度相似，会把排查引向错误方向，代价是大量无效的 fault sim。 | 「## 违反后果」（冲突机理、两个症状、误诊方向、fault sim 代价四点齐备） |
| 4 | 检查方式：在 OCC 使能窗口内检查 `bist_en` / `scan_en` 波形，确认两者不存在同周期高电平重叠；新增或修改 DFT 时序约束时，把该互斥关系作为必检项逐条确认。 | 「## 检查方式」第 1、2 条（波形检查 / 约束评审必检项） |
| 5 | 边界：规则只约束"同周期拉高"，不禁止 bist 与 scan 在时间上分段使用；需要二者交替工作时，切换边界必须由 OCC 时序保证落在不同周期。 | 「## 边界」 |

## 设计取舍

1. **未加 `paths:`**：record 的生效条件是"OCC 窗口内并存 repair/MBIST 时钟与 scan 时钟的 DFT 设计"，属设计范围而非文件类型；若硬加 `paths: ["**/*.sdc"]` 会漏掉波形检查与约束评审场景（第 4 条结论），造成语义收窄。故适用范围由「## 适用范围」节按设计条件判定，`install.md` 另注明项目本地可按需自定义 `paths`，但那是项目定制、需单独裁决。
2. **安装建议项目级**：规则为领域级且 project 记录为 HBM，建议落到 DFT 项目的 `.claude/rules/`，避免在无 DFT 工作的会话中加载；用户级仅作为跨项目备选（见 `install.md`）。
3. **副标签（知识库）处理**：「违反后果」节承载"为什么不能同周期"的机理知识，供规则解释与培训引用；按主形态 Rule 实现，不另造 memory 组件（技能 B 的"主形态实现、副标签挂接建议写在 implementation.md"口径）。
4. **不扩写时序方案**：record 未给出具体 OCC 时序实现方式（如切换周期数、握手信号），artifact 不发明方案，只规定判定口径与必检项，避免演绎。
5. **去重扫描**：`~/.claude/rules/` 现有 4 条与 `eng-asset-ai-components/rules/` 均无 DFT/MBIST/scan 时序互斥内容，无重复实现。

## 测试结果

- 触发样例：`tests/trigger-cases.md` 用 DFT 时序场景共 10 例（H1-H6 应命中、N1-N4 不应命中），逐例对照规则全文判定，10/10 与期望一致；同周期违规、波形重叠、约束评审必检项、误诊拦截、领域范围、分段使用边界六个判定点均被覆盖。
- 范围判定口径抽验：N1（scan-only）与 N4（不同 OCC 窗口）均正确不命中，未因项目名或文件类型误触发。
- 确定性校验：见下方「校验记录」。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-08
- 来源提案 ID：20261022-1705-hbm3e-dft-meeting
- 目标组件形态：Rule
- 目标层级 / 领域 / 项目：领域级 / DFT、时序 / HBM（安装按 DFT 项目级）
- 组件 owner：DFT 领域 owner
- 变更内容：新增 `rules/bist-scan-same-cycle-exclusion.md`（package：`build/EA-20261022-08/`）
- 验收清单：目录与 manifest 对账、record approved 与 proposal/ai_form 一致、frontmatter 含 asset_id 与 ai_form、无敏感信息、无 record 原文混入、语义保持对照通过、触发样例通过（DFT 时序场景）
- 回滚方式：revert 合入 PR；已安装环境删除项目 `.claude/rules/bist-scan-same-cycle-exclusion.md`

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-08 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-08，2026-10-22 approved 入库。record：`assets/20261022-1705-hbm3e-dft-meeting/EA-20261022-08-bist-scan-same-cycle-rule.md`。provenance 仅记录于本文件，artifact 不含。
