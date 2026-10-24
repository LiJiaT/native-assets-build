# TEST ONLY — synthetic 流程样例

> 本包仅用于流程验证，**不得安装到生产环境**。已从生产安装点撤出；组件实体移入 `samples/synthetic/`。

# 安装说明 · hbm3e-dft-env-baseline（EA-20261022-07）

- install_target: `test-sandbox`；release_channel: `test-only`

> 本包**未安装**。安装须经组件 owner 评审（`review.md`）通过后由人执行；技能 B 不执行安装，不写项目 memory 目录。
> 命令在 `eng-asset-ai-components` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置（二选一，按 HBM 项目现行 memory 机制选择）

1. **Claude Code 项目作用域 memory（推荐，当前环境文档化载入点）**：
   `~/.claude/projects/<hbm-project-slug>/memory/hbm3e-dft-env-baseline.md`
2. **项目内 `.claude/memory/`（仅当 HBM 项目确实使用该载入点时）**：
   `$HBM_PROJECT/.claude/memory/hbm3e-dft-env-baseline.md`

理由：参数绑定 HBM3E 当前工具链版本与 die 配置，属项目级知识，不应进入用户级全局 memory 或 DFT 领域级 memory。

## 前置条件

- [ ] `review.md` 全部勾选，组件 owner 结论为通过
- [ ] artifact 已合入本仓库（建议 `components/hbm3e-dft-env-baseline.md`）
- [ ] 已确认 `<hbm-project-slug>` 是 `~/.claude/projects/` 下真实存在的 HBM 项目目录名，且无同义条目

## 安装步骤（项目作用域 memory，推荐）

```bash
: "${HBM_PROJECT_SLUG:?请先设置 HBM_PROJECT_SLUG（~/.claude/projects/ 下的 HBM 项目目录名）}"
MEM_DIR="$HOME/.claude/projects/$HBM_PROJECT_SLUG/memory"
NAME="hbm3e-dft-env-baseline.md"

mkdir -p "$MEM_DIR"
if [ -f "$MEM_DIR/$NAME" ]; then
  cp "$MEM_DIR/$NAME" "$MEM_DIR/$NAME.bak-2026-10-22"
fi
cp build/EA-20261022-07/artifacts/memory-entry.md "$MEM_DIR/$NAME"
head -9 "$MEM_DIR/$NAME"
```

## 安装步骤（项目内 .claude/memory，可选）

```bash
: "${HBM_PROJECT:?请先设置 HBM_PROJECT 为 HBM 项目根目录}"
MEM_DIR="$HBM_PROJECT/.claude/memory"
NAME="hbm3e-dft-env-baseline.md"

mkdir -p "$MEM_DIR"
if [ -f "$MEM_DIR/$NAME" ]; then
  cp "$MEM_DIR/$NAME" "$MEM_DIR/$NAME.bak-2026-10-22"
fi
cp build/EA-20261022-07/artifacts/memory-entry.md "$MEM_DIR/$NAME"
head -9 "$MEM_DIR/$NAME"
```

## 生效与验证

- **在 HBM 项目内新开会话**后生效；用户级或其他项目的会话不应加载本条目。
- 抽验（对照 `tests/independent-check.md`）：询问"HBM3E 当前 MBIST 覆盖率评估的环境前提是什么"，回答应给出 V0.9（bist_collars 受限）、2 个 spare row、PHY 修复粒度 1:4，并说明失效需重核。

## 回滚

```bash
# 项目作用域 memory
: "${HBM_PROJECT_SLUG:?请先设置 HBM_PROJECT_SLUG}"
rm -f "$HOME/.claude/projects/$HBM_PROJECT_SLUG/memory/hbm3e-dft-env-baseline.md"
# 如安装前有备份：
# mv "$HOME/.claude/projects/$HBM_PROJECT_SLUG/memory/hbm3e-dft-env-baseline.md.bak-2026-10-22" \
#    "$HOME/.claude/projects/$HBM_PROJECT_SLUG/memory/hbm3e-dft-env-baseline.md"
```

```bash
# 项目内 .claude/memory
: "${HBM_PROJECT:?请先设置 HBM_PROJECT}"
rm -f "$HBM_PROJECT/.claude/memory/hbm3e-dft-env-baseline.md"
```

- 不涉及 `settings.json` 或 hook；回滚后新会话即不再加载。

## 安装记录（由人填写）

- 安装方式：项目作用域 memory / 项目内 .claude/memory（圈选）
- 安装位置：
- 安装日期：
- 执行人：
- owner 批准记录：
- [ ] 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
