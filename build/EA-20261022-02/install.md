# 安装说明 · verilog-filelist-sync（EA-20261022-02）

- install_target: `user-global`；release_channel: `component-library`

> 本包**未安装**。安装须经组件 owner 评审通过后由人执行；技能 B 不执行安装、不改 settings.json。
> 命令在 `native-assets-build` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置

- 用户级（建议）：`~/.claude/rules/verilog-filelist-sync.md`
- 项目级（仅该项目需要时）：`<project>/.claude/rules/verilog-filelist-sync.md`

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库 `rules/verilog-filelist-sync.md`
- [ ] 目标环境存在 filelist 与目录一致性 hook（本规则只引用该 hook 作为完成判定，不包含 hook 实现）；若不存在，由 owner 决定 hook 落位后再安装本规则

## 安装步骤

```bash
# 1) 备份同名文件（如存在）
if [ -f ~/.claude/rules/verilog-filelist-sync.md ]; then
  cp ~/.claude/rules/verilog-filelist-sync.md ~/.claude/rules/verilog-filelist-sync.md.bak-2026-10-22
fi

# 2) 创建目录并复制实现物
mkdir -p ~/.claude/rules
cp build/EA-20261022-02/artifacts/rule-verilog-filelist-sync.md ~/.claude/rules/verilog-filelist-sync.md

# 3) 校验文件头（应看到 asset_id: EA-20261022-02 与 ai_form: Rule）
head -8 ~/.claude/rules/verilog-filelist-sync.md
```

## 生效与验证

- Claude Code 用户级 rules 自动加载；本规则带 `paths: ["**/*.v"]`，在会话上下文出现 `.v` 文件时加载。**新开会话**后生效。
- 按 `tests/trigger-cases.md` 抽验：H1（新增 `.v` 未改 filelist 应被要求补齐）与 N1（只改文档不应提及本规则）。

## 回滚

```bash
rm -f ~/.claude/rules/verilog-filelist-sync.md
# 如安装前有备份，用备份恢复：
# mv ~/.claude/rules/verilog-filelist-sync.md.bak-2026-10-22 ~/.claude/rules/verilog-filelist-sync.md
```

- 本规则不涉及 `settings.json`、权限或 hook 配置，回滚只需移除文件，无需重启服务；新会话即不再加载。

## 安装记录（由人填写）

- 安装日期：
- 执行人：
- owner 批准记录：
- 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
