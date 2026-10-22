---
name: 组件实现申请
about: 技能 B（资产AI化）产出 implementation package 后，向本 repo 提交实现入库申请
title: "[实现申请] <资产ID> → <组件形态> · <日期>"
labels: implementation-request
---

# 组件实现申请

> 由技能 B 生成本申请单内容；提交动作由人执行或经人明确授权的自动化执行。批准与安装权限属于组件 owner。

## 必填字段

- **资产 ID**：（来源 asset record，eng-knowledge-assets 中的 approved record）
- **来源提案 ID**：
- **目标组件形态**：Memory / Rule / Skill / Workflow / Hook / Prompt
- **目标层级 / 领域 / 项目**：
- **组件 owner**：
- **变更内容**：（新增/修改哪些实现物，附 implementation package 路径）
- **验收清单**：（- [ ] 项：schema / lint / 测试 / 敏感信息检查 / 语义保持验证）
- **回滚方式**：（revert 此 PR / 移除安装的组件文件）

## 附件

- implementation package 路径（implementation.md、build-manifest.json、artifacts、tests、review 清单、install 说明）：
- 校验与测试结果：

## 审批

- [ ] 组件 owner 评审通过（批准后安装或合入；通过后回写 asset record 的 implementation 字段）
