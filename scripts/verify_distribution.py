#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""I→G 分发对账：来源指针、版本/hash 与允许的转换说明。

用法:
  python scripts/verify_distribution.py --rules-repo ../ai-native-basic-component \
      --assets-repo ../eng-knowledge-assets
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

PKG_ROOT = Path(__file__).resolve().parents[1]


def split(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        return None, text
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError:
        return {"__parse_error__": True}, ""


def sha(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules-repo", required=True)
    ap.add_argument("--assets-repo", required=True)
    args = ap.parse_args()
    rules_repo, assets_repo = Path(args.rules_repo), Path(args.assets_repo)
    builds = {}
    for man in PKG_ROOT.glob("build/EA-*/build-manifest.json"):
        d = json.loads(man.read_text(encoding="utf-8"))
        if d.get("release_channel") == "component-library":
            builds[d["asset_id"]] = (man.parent, d)
    errors, seen = [], {}
    for gfile in list((rules_repo / "rules").glob("*.md")) + list(
            (rules_repo / "memory").glob("*.md")):
        fm, body = split(gfile.read_text(encoding="utf-8"))
        if not fm or fm.get("__parse_error__") or not fm.get("asset_id"):
            continue
        aid = fm["asset_id"]
        if aid in seen:
            errors.append(f"{aid}: G 分发副本重复 {seen[aid]} / {gfile}")
        seen[aid] = gfile
        if aid not in builds:
            errors.append(f"{aid}: G 有分发副本但 I 无 component-library 构建")
            continue
        bdir, man = builds[aid]
        if fm.get("source_record") != man.get("source_record"):
            errors.append(f"{aid}: source_record 与 I manifest 不一致")
        if fm.get("release_channel") != man.get("release_channel"):
            errors.append(f"{aid}: release_channel 与 I manifest 不一致")
        src_art = fm.get("source_artifact")
        if not src_art:
            errors.append(f"{aid}: 缺 source_artifact")
        else:
            apath = PKG_ROOT / src_art
            if not apath.is_file():
                errors.append(f"{aid}: source_artifact 不存在 {src_art}")
            elif fm.get("source_artifact_sha256") != sha(apath):
                errors.append(f"{aid}: source_artifact hash 与 I 产物不一致")
            elif apath.name not in (man.get("artifacts") or []):
                errors.append(f"{aid}: source_artifact 不在 I manifest artifacts")
        if not fm.get("source_revision"):
            errors.append(f"{aid}: 缺 source_revision")
        elif str(fm.get("source_revision")) != str(man.get("source_revision") or ""):
            errors.append(
                f"{aid}: source_revision 与 I manifest 不一致 "
                f"({fm.get('source_revision')} != {man.get('source_revision')})")
        # 正文可允许适配，但必须写明转换说明
        _, ibody = split((PKG_ROOT / src_art).read_text(encoding="utf-8")) if src_art else (None, "")
        if ibody.strip() != body.strip() and not fm.get("distribution_note"):
            errors.append(f"{aid}: G 正文与 I 产物不同但缺 distribution_note")
    missing = sorted(set(builds) - set(seen))
    for aid in missing:
        errors.append(f"{aid}: I 有 component-library 构建但 G 无分发副本")
    if errors:
        print("❌ 分发对账失败：")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"✅ 分发对账通过（{len(seen)} 份 G 副本，来源/hash/revision/转换说明一致）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
