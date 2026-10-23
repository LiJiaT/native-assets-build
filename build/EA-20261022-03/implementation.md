# 实现说明 · EA-20261022-03 · 禁止 AI 自动执行对外上传与提交

| 项 | 值 |
|---|---|
| asset_id | EA-20261022-03 |
| proposal_id | 20261022-1705-ai-public-rules |
| ai_form | Rule（record 映射结论，未改） |
| 目标层级 / 领域 / 项目 | 公共级 / 无 / 无 |
| record | eng-knowledge-assets `assets/20261022-1705-ai-public-rules/EA-20261022-03-no-auto-external-actions.md`（approved 2026-10-22） |
| 组件 owner | AI 平台团队（record owner；实际组件 owner 由评审指定） |
| build 日期 | 2026-10-22 |
| 实现物 | `artifacts/rule-no-auto-external-actions.md` → 安装名 `~/.claude/rules/no-auto-external-actions.md` |

## 语义保持对照

statement 的每条结论逐条落到 artifact，未增删语义。

| # | statement 结论（原文） | artifact 承载位置 |
|---|---|---|
| 1 | AI 不得自动执行任何对外动作；所有对外动作必须由人确认后执行。 | `artifacts/rule-no-auto-external-actions.md` ›「## 规则」 |
| 2 | 对外动作范围：向对外仓库上传、推送或提交（含 git push、创建或合并 PR）、对外发布、向外部系统或外部人员发送材料与数据。 | 「## 执行要求」第 1 条「按范围识别对外动作」 |
| 3 | 人的确认：AI 可以准备变更、命令与说明，但执行对外动作前必须获得人的明确确认；未获确认一律不执行。 | 「## 执行要求」第 2 条「先取得人的确认」 |
| 4 | 不得绕过：权限与 hook 的双重拦截必须保持开启；不得为完成动作而修改权限配置、关闭 hook，或改用其他通道绕过拦截。被拦截时应如实报告并交人处理。 | 「## 执行要求」第 3 条「不绕过拦截」 |
| 5 | 判定边界：凡动作结果会离开本地或团队内部环境（对外仓库、外部系统、外部人员），即属对外动作，不因"只是一次 push""只是同步一下"而降级处理。 | 「## 执行要求」第 4 条「按结果判定边界」 |
| 6 | 完成判定：对外动作的执行记录中存在人的明确确认，且未发生任何绕过拦截的配置改动。 | 「## 完成标准」 |

## 设计取舍

1. **不加 `paths:`**：规则面向所有会话、所有项目，不绑定文件类型，确保在任意工具调用序列中都加载。
2. **保留"权限与 hook 的双重拦截"原表述**：record 未指定具体 permission 规则或 hook 名称，本包不写 `settings.json` 片段、不改权限配置，避免把 Rule 扩成 Hook，也避免安装包携带环境改动。
3. **"准备—确认—执行"写成三步可判定动作**：准备物（变更、命令、说明）与确认点均可在执行记录中核对，对应完成判定"执行记录中存在人的明确确认"。
4. **不列举具体平台或通道**：record 的判定边界是"结果是否离开本地或团队内部环境"，用结果口径而非平台清单，避免名单过时导致漏判。
5. **去重扫描**：`~/.claude/rules/` 现有 4 条与本条无重叠——`auto-mode-classifier.md` 处理分类器超时后的重试策略，不涉及对外动作禁令，也不允许绕过拦截，二者不合并；`eng-asset-ai-components/rules/` 当前为空。

## 测试结果

- 触发样例：`tests/trigger-cases.md` 共 10 例（H1-H6 应命中、N1-N4 不应命中），逐例对照规则全文判定，10/10 与期望一致；对外动作范围、确认点、不得绕过、结果判定四条边界均被覆盖。
- 确定性校验：见下方「校验记录」。

## 实现申请要素（供人提交 issue）

- 资产 ID：EA-20261022-03
- 来源提案 ID：20261022-1705-ai-public-rules
- 目标组件形态：Rule
- 目标层级 / 领域 / 项目：公共级 / 无 / 无
- 组件 owner：AI 平台团队
- 变更内容：新增 `rules/no-auto-external-actions.md`（package：`build/EA-20261022-03/`）
- 验收清单：目录与 manifest 对账、record approved 与 proposal/ai_form 一致、frontmatter 含 asset_id、无敏感信息、无 record 原文混入、语义保持对照通过、触发样例通过
- 回滚方式：revert 合入 PR；已安装环境删除 `~/.claude/rules/no-auto-external-actions.md`（本规则不涉及权限/hook 配置，回滚无需改 settings）

## 校验记录

命令：`python -X utf8 C:\Users\jie.li\.claude\skills\asset-ai-ize\scripts\validate_build.py D:\Project\eng-asset-ai-components\build\EA-20261022-03 --assets-repo D:\Project\eng-knowledge-assets`

退出码：0。输出末两行：

```
[validate_build] 检查 5 项: 通过 5 / 失败 0 / 警告 0
[validate_build] ✅ 校验通过
```

---

来源：asset EA-20261022-03，2026-10-22 approved 入库。record：`assets/20261022-1705-ai-public-rules/EA-20261022-03-no-auto-external-actions.md`。provenance 仅记录于本文件，artifact 不含。
