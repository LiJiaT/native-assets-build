# 工程资产转 AI 组件（eng-asset-ai-components）

技能 B「资产AI化」的实现落地仓库。存放公共 **skill / rule / hook / prompt**、组件实现与测试。

对应规范：《AI 公共规范》§2.4（资产化落地）（飞书文档 `SlsGd0bKQo6pVNxxxNAcrF1tnIg`）。上游依赖：[eng-knowledge-assets](https://github.com/LiJiaT/eng-knowledge-assets)（approved asset record 的唯一来源）。

## 链路位置

```
approved asset record（eng-knowledge-assets）
  → 技能B 读取 record + 目标组件 profile
  → 按 ai_form（Memory/Rule/Skill/Workflow/Hook/Prompt）在 build 目录生成实现物
  → 校验（schema/lint/测试/敏感信息/语义保持）
  → 本 repo 实现申请 issue/PR → owner 批准 → 合入/分发
```

## 目录结构

```
skills/        # 公共 skill 组件
rules/         # 公共 rule 组件
hooks/         # 公共 hook 组件
prompts/       # 公共 prompt 组件
components/    # 其他组件实现（Workflow 等）
samples/       # synthetic 示例（test-only，不安装、不发布）
build/         # 技能 B 的构建工作区（不直接合入，评审通过后落位到上面各目录）
reviews/       # 实现评审记录
.github/ISSUE_TEMPLATE/implementation-request.md   # 实现申请 issue 模板
```

> 领域级基础组件（真实资产）统一存放于 [ai-native-basic-component](https://github.com/LiJiaT/ai-native-basic-component) 的 `rules/<domain>/`、`memory/<domain>/`。synthetic 示例（EA-07/08/09）统一放 `samples/synthetic/`，`release_channel=test-only`，不得安装或发布。

## 实现流程

1. 技能 B 读取 approved asset record 与目标组件 profile，按 ai_form 加载对应 playbook 生成实现物；
2. 执行确定性校验：schema v2（record 审批/内容 hash、owner/layer/安装范围、artifact provenance、隐藏文件、语法、敏感信息、原始记录、语义保持）；发布前用 `--release` 额外要求 `tests/results.json`、`review.json` 与产物 hash 绑定；
3. 以本 repo 的 [实现申请 issue 模板](.github/ISSUE_TEMPLATE/implementation-request.md) 提交申请，附 implementation package（implementation.md、build-manifest.json、artifacts、tests、review 清单、install 说明）；
4. **组件 owner 评审通过后**才安装或合入；不自动发布到公共目录。技能不得自行关闭 issue、批准 PR 或合并。评审接口与拒绝返回见 [review-contract](https://github.com/LiJiaT/ai-native-basic-component/blob/main/skills/asset-ai-ize/references/review-contract.md)。

## 当前状态（2026-10-24）

- 9 个 build 包全部升级到 `build-manifest.json` schema v2，携带 `provenance_status`、`release_channel`、`install_target`、record 文件 hash 与不可变正文 hash。
- 七个最终组件中的 01–06 已补 `provenance_status`/`provenance_note`/`release_channel`；01–06 通过 structure + release 两层校验。
- EA-07/08/09 为 synthetic，已从生产安装点撤出，最终组件移入 `samples/synthetic/`，build 包保留为 test-only 历史。
- `tests/results.json` 与 `review.json` 只覆盖确定性检查；语义结论仍由 owner/独立 reviewer 复核。

## 边界纪律

- 技能 B **不重新判断资产是否成立、不修改资产语义**（statement / evidence / mapping）；
- 映射不可行时返回 `mapping_issue`，由技能 A 或 owner 重新映射，不擅自改 record；
- 实现通过后写回 asset record 的 `implementation` 字段（在 eng-knowledge-assets 侧更新）。
