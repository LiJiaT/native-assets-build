#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""消费者加载检查：按下游方式读取 artifact，核对身份/来源/触发样例。"""
import json
import sys
from pathlib import Path

import yaml

BUILD = Path(__file__).resolve().parents[1]
ERRORS = []


def split(text):
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, text
    try:
        fm = yaml.safe_load("\n".join(lines[1:end])) or {}
    except yaml.YAMLError as exc:
        ERRORS.append(f"frontmatter 解析失败: {exc}")
        return None, text
    return fm, "\n".join(lines[end + 1:])


manifest = json.load(open(BUILD / "build-manifest.json", encoding="utf-8"))
if len(manifest.get("artifacts") or []) != 1:
    ERRORS.append("本消费者检查假设单 artifact 包")
artifact = BUILD / "artifacts" / manifest["artifacts"][0]
fm, body = split(artifact.read_text(encoding="utf-8"))
if fm is None:
    ERRORS.append("artifact 缺 frontmatter")
else:
    expected = {
        "asset_id": manifest["asset_id"],
        "ai_form": manifest["ai_form"],
        "asset_type": manifest["asset_type"],
        "provenance_status": manifest["provenance_status"],
        "release_channel": manifest["release_channel"],
        "source_record": manifest["source_record"],
    }
    for key, value in expected.items():
        if fm.get(key) != value:
            ERRORS.append(f"{key}={fm.get(key)!r} != {value!r}")
    if not str(fm.get("provenance_note") or "").strip():
        ERRORS.append("provenance_note 为空")
if len(str(body).strip()) < 100:
    ERRORS.append("artifact 正文过短，无法作为消费者内容加载")

tests = BUILD / "tests"
if manifest["ai_form"] == "Rule":
    case = tests / "trigger-cases.md"
    if not case.is_file():
        ERRORS.append("Rule 缺 tests/trigger-cases.md")
    else:
        text = case.read_text(encoding="utf-8")
        for marker in ("应命中", "不应命中", "H1", "N1"):
            if marker not in text:
                ERRORS.append(f"触发样例缺 {marker}")
else:
    checks = list(tests.glob("independent-check.md")) + list(tests.glob("trigger-cases.md"))
    if not checks:
        ERRORS.append("Memory 包缺独立检查/触发样例证据")

if ERRORS:
    print("CONSUMER CHECK FAILED")
    for e in ERRORS:
        print(" -", e)
    sys.exit(1)
print(f"CONSUMER CHECK OK: {manifest['asset_id']} {manifest['ai_form']} "
      f"artifact={manifest['artifacts'][0]} source={manifest['source_record']}")
