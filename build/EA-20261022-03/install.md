# 安装说明 · no-auto-external-actions（EA-20261022-03）

- install_target: `user-global`；release_channel: `component-library`

> 本包**未安装**。安装须经组件 owner 评审通过后由人执行；技能 B 不执行安装、不改权限配置。
> 命令在 `eng-asset-ai-components` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置

- 用户级（建议）：`~/.claude/rules/no-auto-external-actions.md`
- 项目级：`<project>/.claude/rules/no-auto-external-actions.md`（与用户级重复时只装用户级）

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库 `rules/no-auto-external-actions.md`
- [ ] 目标环境的权限与 hook 双重拦截已开启（本规则要求保持开启，自身不提供拦截实现）；未开启时先由 owner 完成拦截落位，再安装本规则

## 安装步骤

```bash
# 1) 备份同名文件（如存在）
if [ -f ~/.claude/rules/no-auto-external-actions.md ]; then
  cp ~/.claude/rules/no-auto-external-actions.md ~/.claude/rules/no-auto-external-actions.md.bak-2026-10-22
fi

# 2) 创建目录并复制实现物
mkdir -p ~/.claude/rules
cp build/EA-20261022-03/artifacts/rule-no-auto-external-actions.md ~/.claude/rules/no-auto-external-actions.md

# 3) 校验文件头（应看到 asset_id: EA-20261022-03 与 ai_form: Rule）
head -8 ~/.claude/rules/no-auto-external-actions.md
```

## 生效与验证

- Claude Code 用户级 rules 自动加载，无 `paths` 限制，**新开会话**后在所有项目中生效。
- 按 `tests/trigger-cases.md` 抽验：H1（"直接 push 到对外仓库"应先请求确认而非执行）与 N1（本地 commit 不应被阻塞）。
- 本步骤不写入任何 `settings.json` 内容；权限与 hook 配置保持安装前状态。

## 回滚

```bash
rm -f ~/.claude/rules/no-auto-external-actions.md
# 如安装前有备份，用备份恢复：
# mv ~/.claude/rules/no-auto-external-actions.md.bak-2026-10-22 ~/.claude/rules/no-auto-external-actions.md
```

- 回滚只移除规则文件，不触碰权限/hook 配置；新会话即不再加载。

## 安装记录（由人填写）

- 安装日期：
- 执行人：
- owner 批准记录：
- 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
