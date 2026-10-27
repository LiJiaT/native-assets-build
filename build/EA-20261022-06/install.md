# 安装说明 · no-raw-records-in-memory（EA-20261022-06）

- install_target: `user-global`；release_channel: `component-library`

> 本包**未安装**。安装须经组件 owner 评审通过后由人执行；技能 B 不执行安装。
> 命令在 `native-assets-build` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置

- 用户级（建议，公共级规则）：`~/.claude/rules/no-raw-records-in-memory.md`
- 项目级：`<project>/.claude/rules/no-raw-records-in-memory.md`（仅当该项目有独立的知识资产写入流程时需要；与用户级重复时只装用户级）

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库 `rules/no-raw-records-in-memory.md`
- [ ] 确认项目已有的 memory 写入流程不需要修改（本规则只约束写入形态，不提供脚本）

## 安装步骤

```bash
# 1) 备份同名文件（如存在）
if [ -f ~/.claude/rules/no-raw-records-in-memory.md ]; then
  cp ~/.claude/rules/no-raw-records-in-memory.md ~/.claude/rules/no-raw-records-in-memory.md.bak-2026-10-22
fi

# 2) 创建目录并复制实现物
mkdir -p ~/.claude/rules
cp build/EA-20261022-06/artifacts/rule-no-raw-records-in-memory.md ~/.claude/rules/no-raw-records-in-memory.md

# 3) 校验文件头（应看到 asset_id: EA-20261022-06 与 ai_form: Rule）
head -6 ~/.claude/rules/no-raw-records-in-memory.md
```

## 生效与验证

- Claude Code 用户级 rules 自动加载，无 `paths` 限制，**新开会话**后对四类长期记忆载体的写入生效。
- 按 `tests/trigger-cases.md` 抽验：H2（聊天记录原文粘进 CLAUDE.md 应判违规）与 N1（当次会话内引用原文不应被禁止）。
- 该规则是行为约束而非自动拦截；若后续要求强拦截，应另行走 Hook 形态的映射提案，不在本包扩展。

## 回滚

```bash
rm -f ~/.claude/rules/no-raw-records-in-memory.md
# 如安装前有备份，用备份恢复：
# mv ~/.claude/rules/no-raw-records-in-memory.md.bak-2026-10-22 ~/.claude/rules/no-raw-records-in-memory.md
```

- 回滚只移除规则文件，无 settings 或 hook 改动；新会话即不再加载。

## 安装记录（由人填写）

- 安装日期：
- 执行人：
- owner 批准记录：
- 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
