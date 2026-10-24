# 安装说明 · asset-taxonomy（EA-20261022-01）

- install_target: `user-global`；release_channel: `component-library`

> 本包**未安装**。安装须经组件 owner 评审（`review.md`）通过后由人执行；技能 B 不执行安装，不改 CLAUDE.md、不写 `~/.claude/`。
> 命令在 `eng-asset-ai-components` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置（二选一，勿重复安装）

1. **用户级 CLAUDE.md 受管区块（推荐，公共级/全项目生效）**：在 `~/.claude/CLAUDE.md` 末尾追加
   `<!-- BEGIN asset-taxonomy (EA-20261022-01) -->` / `<!-- END asset-taxonomy -->` 包裹的条目正文。
2. **项目 memory（降级方案，仅单项目生效）**：`~/.claude/projects/<project-slug>/memory/asset-taxonomy.md`。
   仅当 owner 不希望修改 CLAUDE.md 时使用；它不满足 record 的公共级共享范围，需在评审中显式接受该限制。

理由：公共级、无领域与项目归属，需要所有项目会话都能看到；CLAUDE.md 是当前环境文档化的全局载入点。

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库（建议 `components/asset-taxonomy.md`）
- [ ] 确认目标环境无同义条目（领域划分 / 资产分类体系）
- [ ] 选择项目 memory 方式时，确认 `<project-slug>` 真实存在且接受"仅单项目生效"

## 安装步骤（CLAUDE.md 受管区块，推荐）

```bash
# 1) 备份
cp "$HOME/.claude/CLAUDE.md" "$HOME/.claude/CLAUDE.md.bak-2026-10-22"

# 2) 追加受管区块（正文去掉 YAML frontmatter 后放入区块内）
{
  printf '\n<!-- BEGIN asset-taxonomy (EA-20261022-01) -->\n'
  sed '1,/^---$/d; 1,/^---$/d' build/EA-20261022-01/artifacts/memory-entry.md
  printf '<!-- END asset-taxonomy -->\n'
} >> "$HOME/.claude/CLAUDE.md"

# 3) 确认区块唯一
grep -c "BEGIN asset-taxonomy" "$HOME/.claude/CLAUDE.md"   # 期望 1
```

## 安装步骤（项目 memory，可选）

```bash
: "${PROJECT_SLUG:?请先设置 PROJECT_SLUG（~/.claude/projects/ 下的项目目录名）}"
MEM_DIR="$HOME/.claude/projects/$PROJECT_SLUG/memory"
mkdir -p "$MEM_DIR"
if [ -f "$MEM_DIR/asset-taxonomy.md" ]; then
  cp "$MEM_DIR/asset-taxonomy.md" "$MEM_DIR/asset-taxonomy.md.bak-2026-10-22"
fi
cp build/EA-20261022-01/artifacts/memory-entry.md "$MEM_DIR/asset-taxonomy.md"
head -8 "$MEM_DIR/asset-taxonomy.md"
```

## 生效与验证

- **新开 Claude Code 会话**后生效；CLAUDE.md 方式对所有项目生效，项目 memory 方式只在对应项目生效。
- 抽验（对照 `tests/independent-check.md`）：询问"我们资产库为什么用 9 领域 + 2 项目而不是外部 72 子标签体系"，回答应包含自建平铺结构、正交关系、维护成本取舍与规范 v0.5 证据。

## 回滚

```bash
# CLAUDE.md 方式：删除受管区块后再用备份覆盖
sed -i '/<!-- BEGIN asset-taxonomy (EA-20261022-01) -->/,/<!-- END asset-taxonomy -->/d' "$HOME/.claude/CLAUDE.md"
# mv "$HOME/.claude/CLAUDE.md.bak-2026-10-22" "$HOME/.claude/CLAUDE.md"
```

```bash
# 项目 memory 方式
: "${PROJECT_SLUG:?请先设置 PROJECT_SLUG}"
rm -f "$HOME/.claude/projects/$PROJECT_SLUG/memory/asset-taxonomy.md"
```

- 本条目不涉及 `settings.json`、权限或 hook 配置；回滚后新会话即不再加载。

## 安装记录（由人填写）

- 安装方式：CLAUDE.md 受管区块 / 项目 memory（圈选）
- 安装日期：
- 执行人：
- owner 批准记录：
- [ ] 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
