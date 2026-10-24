# TEST ONLY — synthetic 流程样例

> 本包仅用于流程验证，**不得安装到生产环境**。已从生产安装点撤出；组件实体在 `samples/synthetic/`。

# 安装说明 · bist-scan-same-cycle-exclusion（EA-20261022-08）

- install_target: `test-sandbox`；release_channel: `test-only`
- 唯一允许的落点：`~/.claude/test-sandbox/rules/bist-scan-same-cycle-exclusion.md`
- **不提供**用户级 `~/.claude/rules/` 或项目级 `.claude/rules/` 的生产安装命令；本包不得被生产会话加载。

> 本包**未安装**。若未来转为真实资产，须由 owner 重新评审、更新 record/approval 的层级与 release_channel，并生成新的实现包；不能复用本 test-only 包的安装说明。

## 前置条件

- [ ] `review.md` 全部勾选，DFT 领域 owner 结论为通过
- [ ] 仅在隔离测试环境执行；执行前确认 `~/.claude/test-sandbox/` 不存在生产规则
- [ ] 不修改 `settings.json`，不注册 hook

## 安装步骤（仅 test-sandbox）

```bash
SANDBOX="$HOME/.claude/test-sandbox/rules"
NAME="bist-scan-same-cycle-exclusion.md"

mkdir -p "$SANDBOX"
if [ -f "$SANDBOX/$NAME" ]; then
  cp "$SANDBOX/$NAME" "$SANDBOX/$NAME.bak-2026-10-24"
fi
cp build/EA-20261022-08/artifacts/rule-bist-scan-same-cycle.md "$SANDBOX/$NAME"
head -6 "$SANDBOX/$NAME"
```

## 生效与验证

- 该路径不在 Claude Code 的生产载入点（`~/.claude/rules/`、项目 `.claude/rules/`、`MEMORY.md` 受管区块）内，默认不会被生产会话加载。
- 在隔离环境按 `tests/trigger-cases.md` 抽验 H1/N1；验证脚本为 `tests/consumer_check.py`，证据见 `tests/consumer-test.log`。
- 范围判定以"OCC 使能窗口内是否并存 repair/MBIST 与 scan 时钟"为准，不以文件扩展名或项目名为准。

## 回滚

```bash
rm -f "$HOME/.claude/test-sandbox/rules/bist-scan-same-cycle-exclusion.md"
```

- 回滚只移除 sandbox 文件，不涉及 settings、hook 或生产 rules。

## 安装记录（由人填写）

- 安装方式：仅 test-sandbox
- 安装日期：
- 执行人：
- owner 批准记录：
- 若需生产化：另立 record/approval/实现包，不得直接复制本页命令。
