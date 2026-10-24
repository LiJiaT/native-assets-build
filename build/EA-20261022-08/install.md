# TEST ONLY — synthetic 流程样例

> 本包仅用于流程验证，**不得安装到生产环境**。已从生产安装点撤出；组件实体移入 `samples/synthetic/`。

# 安装说明 · bist-scan-same-cycle-exclusion（EA-20261022-08）

- install_target: `test-sandbox`；release_channel: `test-only`

> 本包**未安装**。安装须经组件 owner（DFT 领域 owner）评审通过后由人执行；技能 B 不执行安装。
> 命令在 `eng-asset-ai-components` 仓库根目录执行（Git Bash / macOS 通用）。

## 目标位置（二选一，只装一处）

1. **用户级（推荐）**：`~/.claude/rules/bist-scan-same-cycle-exclusion.md`
   - 理由：record 为领域级（DFT/时序），规则按 DFT 设计范围生效；用户长期跨多个 DFT 项目工作时，用户级能覆盖全部会话。
2. **项目级（可选）**：`$DFT_PROJECT/.claude/rules/bist-scan-same-cycle-exclusion.md`
   - 仅当 owner 希望把规则限定在单个 DFT 项目时使用；无 DFT 工作的项目不装，避免无关规则占用上下文。

## 前置条件

- [ ] `review.md` 全部勾选，DFT 领域 owner 结论为通过
- [ ] artifact 已合入本仓库 `rules/bist-scan-same-cycle-exclusion.md`
- [ ] 目标项目已具备 OCC 使能窗口的波形或时序约束检查手段（本规则只给判定口径，不提供脚本）
- [ ] 确认目标位置无同名或同语义规则；有冲突时先评审，不覆盖

## 安装步骤（用户级）

```bash
RULES_DIR="$HOME/.claude/rules"
NAME="bist-scan-same-cycle-exclusion.md"

# 1) 备份同名文件（如存在）
mkdir -p "$RULES_DIR"
if [ -f "$RULES_DIR/$NAME" ]; then
  cp "$RULES_DIR/$NAME" "$RULES_DIR/$NAME.bak-2026-10-22"
fi

# 2) 复制实现物
cp build/EA-20261022-08/artifacts/rule-bist-scan-same-cycle.md "$RULES_DIR/$NAME"

# 3) 校验文件头（应看到 asset_id: EA-20261022-08 与 ai_form: Rule）
head -6 "$RULES_DIR/$NAME"
```

## 安装步骤（项目级，可选）

```bash
: "${DFT_PROJECT:?请先设置 DFT_PROJECT 为 DFT 项目根目录}"
RULES_DIR="$DFT_PROJECT/.claude/rules"
NAME="bist-scan-same-cycle-exclusion.md"

mkdir -p "$RULES_DIR"
if [ -f "$RULES_DIR/$NAME" ]; then
  cp "$RULES_DIR/$NAME" "$RULES_DIR/$NAME.bak-2026-10-22"
fi
cp build/EA-20261022-08/artifacts/rule-bist-scan-same-cycle.md "$RULES_DIR/$NAME"
head -6 "$RULES_DIR/$NAME"
```

## 生效与验证

- rules 在新开会话后加载；用户级对全部会话生效，项目级只在对应项目会话生效。
- 按 `tests/trigger-cases.md` 抽验：H1（同周期置位两使能应判违规）与 N1（scan-only 设计不应被要求该检查）。
- 范围判定以"OCC 使能窗口内是否并存 repair/MBIST 与 scan 时钟"为准，不以文件扩展名或项目名为准；若团队希望再加 `paths:` 收敛到 `*.sdc` / `*.sv`，属项目本地定制，需在评审中单独裁决（会收窄触发面）。

## 回滚

```bash
# 用户级
rm -f "$HOME/.claude/rules/bist-scan-same-cycle-exclusion.md"
# 如安装前有备份：
# mv "$HOME/.claude/rules/bist-scan-same-cycle-exclusion.md.bak-2026-10-22" \
#    "$HOME/.claude/rules/bist-scan-same-cycle-exclusion.md"
```

```bash
# 项目级
: "${DFT_PROJECT:?请先设置 DFT_PROJECT}"
rm -f "$DFT_PROJECT/.claude/rules/bist-scan-same-cycle-exclusion.md"
```

- 回滚只移除规则文件，无 settings 或 hook 改动；新会话即不再加载。

## 安装记录（由人填写）

- 安装方式：用户级 / 项目级（圈选）
- 安装日期：
- 执行人：
- owner 批准记录：
- 安装后回写 asset record 的 `implementation` 字段（由人执行，仅该字段可写）
