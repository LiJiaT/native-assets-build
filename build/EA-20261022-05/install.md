# 安装说明 · subtask-acceptance-checklist（EA-20261022-05）

> 本包**未安装**。安装须经组件 owner 评审通过后由人执行；技能 B 不执行安装。
> 命令在 `eng-asset-ai-components` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置

- 用户级（建议，公共级规则）：`~/.claude/rules/subtask-acceptance-checklist.md`
- 项目级：`<project>/.claude/rules/subtask-acceptance-checklist.md`（仅当该项目需要更严格或带项目字段的任务包校验时加装；与用户级重复时只装用户级）

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库 `rules/subtask-acceptance-checklist.md`
- [ ] 项目若已有任务包模板与字段校验脚本，确认"必填字段"清单与模板一致（规则只要求通过校验，不定义字段表）

## 安装步骤

```bash
# 1) 备份同名文件（如存在）
if [ -f ~/.claude/rules/subtask-acceptance-checklist.md ]; then
  cp ~/.claude/rules/subtask-acceptance-checklist.md ~/.claude/rules/subtask-acceptance-checklist.md.bak-2026-10-22
fi

# 2) 创建目录并复制实现物
mkdir -p ~/.claude/rules
cp build/EA-20261022-05/artifacts/rule-subtask-acceptance-checklist.md ~/.claude/rules/subtask-acceptance-checklist.md

# 3) 校验文件头（应看到 asset_id: EA-20261022-05 与 ai_form: Rule）
head -6 ~/.claude/rules/subtask-acceptance-checklist.md
```

## 生效与验证

- Claude Code 用户级 rules 自动加载，无 `paths` 限制，**新开会话**后对所有派单场景生效。
- 按 `tests/trigger-cases.md` 抽验：H1（"做完告诉我"式派单应被要求补清单）与 N1（只讨论拆分不派单不应被要求清单）。
- 与 EA-20261022-04 配套：本规则给出清单，EA-04 要求按同一清单自查与独立复核；两条同时安装不冲突。

## 回滚

```bash
rm -f ~/.claude/rules/subtask-acceptance-checklist.md
# 如安装前有备份，用备份恢复：
# mv ~/.claude/rules/subtask-acceptance-checklist.md.bak-2026-10-22 ~/.claude/rules/subtask-acceptance-checklist.md
```

- 回滚只移除规则文件，无 settings 或 hook 改动；新会话即不再加载。

## 安装记录（由人填写）

- 安装日期：
- 执行人：
- owner 批准记录：
- 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
