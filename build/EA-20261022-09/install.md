# TEST ONLY — synthetic 流程样例

> 本包仅用于流程验证，**不得安装到生产环境**。已从生产安装点撤出；组件实体移入 `samples/synthetic/`。

# 安装说明 · hbm3e-stack-level-repair-decision（EA-20261022-09）

- install_target: `test-sandbox`；release_channel: `test-only`

> 本包**未安装**。安装须经组件 owner 评审（`review.md`）通过后由人执行；技能 B 不执行安装，不写 memory 目录。
> 命令在 `eng-asset-ai-components` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置（按 owner 裁决）

1. **当前项目 memory（本机默认可验证的载入点，推荐先落这里）**：
   `~/.claude/projects/<project-slug>/memory/hbm3e-stack-level-repair-decision.md`
2. **领域级共享（需 owner 先指定载体）**：本机当前没有文档化的 DFT 领域级 memory 目录。若 owner 指定了真实存在的载入点（例如某个 DFT 项目的 memory 目录或 CLAUDE.md 受管区块），按该路径安装；**不要自建 `~/.claude/memory/domains/`**——该路径不在当前载入约定内，写了也不会被加载。

理由：决策证据来自 HBM3E，但"修复资源在哪一层可访问，就把 repair 放在哪一层"的取舍原则可迁移到其他堆叠 die 项目，record 判为领域级；在领域级载体未定义前，先落项目 memory 是可验证的过渡方案。

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库（建议 `components/hbm3e-stack-level-repair-decision.md`）
- [ ] 确认目标 memory 无同义条目；若与 EA-07 基线条目同目录，确认两条不互相重复（本条引用前提、不展开参数机理）
- [ ] 确认 `<project-slug>` 是 `~/.claude/projects/` 下真实存在的项目目录名

## 安装步骤（项目 memory）

```bash
: "${PROJECT_SLUG:?请先设置 PROJECT_SLUG（~/.claude/projects/ 下的项目目录名）}"
MEM_DIR="$HOME/.claude/projects/$PROJECT_SLUG/memory"
NAME="hbm3e-stack-level-repair-decision.md"

# 1) 备份同名文件（如存在）
mkdir -p "$MEM_DIR"
if [ -f "$MEM_DIR/$NAME" ]; then
  cp "$MEM_DIR/$NAME" "$MEM_DIR/$NAME.bak-2026-10-22"
fi

# 2) 复制实现物
cp build/EA-20261022-09/artifacts/memory-entry.md "$MEM_DIR/$NAME"

# 3) 校验文件头（应看到 asset_id: EA-20261022-09 与 ai_form: Memory）
head -9 "$MEM_DIR/$NAME"
```

## 生效与验证

- **新开会话**后在对应项目内生效；其他项目会话不加载。
- 抽验（对照 `tests/independent-check.md`）：询问"HBM3E 为什么 repair 放在 stack 侧而不是 controller 侧"，回答应包含 PHY spare row 不可达、覆盖率天花板、与 base die 协议一致、HBM3 98%+ 与复核条件。
- 若后续 owner 定义了 DFT 领域级载体，再把同一条目复制到该载体并删除项目级副本，避免双处维护。

## 回滚

```bash
: "${PROJECT_SLUG:?请先设置 PROJECT_SLUG}"
rm -f "$HOME/.claude/projects/$PROJECT_SLUG/memory/hbm3e-stack-level-repair-decision.md"
# 如安装前有备份：
# mv "$HOME/.claude/projects/$PROJECT_SLUG/memory/hbm3e-stack-level-repair-decision.md.bak-2026-10-22" \
#    "$HOME/.claude/projects/$PROJECT_SLUG/memory/hbm3e-stack-level-repair-decision.md"
```

- 不涉及 `settings.json` 或 hook；回滚后新会话即不再加载。

## 安装记录（由人填写）

- 安装位置：
- 安装日期：
- 执行人：
- owner 批准记录：
- [ ] 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
