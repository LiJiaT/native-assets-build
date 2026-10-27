# 安装说明 · verify-or-review-before-delivery（EA-20261022-04）

- install_target: `user-global`；release_channel: `component-library`

> 本包**未安装**。安装须经组件 owner 评审通过后由人执行；技能 B 不执行安装。
> 命令在 `native-assets-build` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置

- 用户级（建议）：`~/.claude/rules/verify-or-review-before-delivery.md`
- 项目级：`<project>/.claude/rules/verify-or-review-before-delivery.md`（与用户级重复时只装用户级）

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库 `rules/verify-or-review-before-delivery.md`
- [ ] 项目若已有验收清单，确认其可被引用为"同一验收清单"（规则不内置清单）

## 安装步骤

```bash
# 1) 备份同名文件（如存在）
if [ -f ~/.claude/rules/verify-or-review-before-delivery.md ]; then
  cp ~/.claude/rules/verify-or-review-before-delivery.md ~/.claude/rules/verify-or-review-before-delivery.md.bak-2026-10-22
fi

# 2) 创建目录并复制实现物
mkdir -p ~/.claude/rules
cp build/EA-20261022-04/artifacts/rule-verify-or-review-before-delivery.md ~/.claude/rules/verify-or-review-before-delivery.md

# 3) 校验文件头（应看到 asset_id: EA-20261022-04 与 ai_form: Rule）
head -8 ~/.claude/rules/verify-or-review-before-delivery.md
```

## 生效与验证

- Claude Code 用户级 rules 自动加载，无 `paths` 限制，**新开会话**后对所有产出类型生效。
- 按 `tests/trigger-cases.md` 抽验：H1（只写"已检查"应被判不合规）与 N1（纯讨论不产生交付物不应被要求自查）。
- 该规则要求独立复核；单人会话中可用"与执行上下文独立的 AI 复核者"满足，无需额外安装组件。

## 回滚

```bash
rm -f ~/.claude/rules/verify-or-review-before-delivery.md
# 如安装前有备份，用备份恢复：
# mv ~/.claude/rules/verify-or-review-before-delivery.md.bak-2026-10-22 ~/.claude/rules/verify-or-review-before-delivery.md
```

- 回滚只移除规则文件，无 settings 或 hook 改动；新会话即不再加载。

## 安装记录（由人填写）

- 安装日期：
- 执行人：
- owner 批准记录：
- 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
