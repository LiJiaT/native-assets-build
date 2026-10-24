#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对 build/ 下所有实现包运行技能 B 校验。

用法:
  python scripts/validate_packages.py --assets-repo ../eng-knowledge-assets
  python scripts/validate_packages.py --assets-repo ../eng-knowledge-assets --validator ../ai-native-basic-component/skills/asset-ai-ize/scripts/validate_build.py

默认：9 个包结构层必须通过；release_channel=component-library 的包必须通过发布层，
test-only 包必须被发布层拒绝（防止 synthetic 进入发布）。
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

PKG_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VALIDATOR = Path(__file__).resolve().parents[2] / "ai-native-basic-component/skills/asset-ai-ize/scripts/validate_build.py"


def body_after_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) > 2:
            return parts[2].strip()
    return text.strip()


def check_final_rules():
    """最终 rules 必须与其来源实现产物的正文完全一致，防止旧副本回流。"""
    failed = 0
    for rule in sorted((PKG_ROOT / "rules").glob("*.md")):
        matches = sorted((PKG_ROOT / "build").glob(f"*/artifacts/rule-{rule.stem}.md"))
        if not matches:
            print(f"FAIL rule      {rule.name}: 找不到对应实现产物")
            failed += 1
            continue
        expected = body_after_frontmatter(rule.read_text(encoding="utf-8"))
        for artifact in matches:
            actual = body_after_frontmatter(artifact.read_text(encoding="utf-8"))
            if actual != expected:
                print(f"FAIL rule      {rule.name} != {artifact.parent.parent.name}/artifacts/{artifact.name}")
                failed += 1
            else:
                print(f"OK  rule      {rule.name} == {artifact.parent.parent.name}")
    return failed


def run(validator, build, assets, release):
    cmd = [sys.executable, "-X", "utf8", str(validator), str(build),
           "--assets-repo", str(assets)]
    if release:
        cmd.append("--release")
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--assets-repo", required=True)
    ap.add_argument("--validator", default=str(DEFAULT_VALIDATOR))
    args = ap.parse_args()
    assets = Path(args.assets_repo).resolve()
    validator = Path(args.validator).resolve()
    if not (assets / "registry.json").is_file():
        print(f"✗ assets repo 无效: {assets}")
        return 2
    if not validator.is_file():
        print(f"✗ validator 不存在: {validator}")
        return 2
    failed = 0
    for build in sorted(PKG_ROOT.glob("build/EA-*")):
        manifest = json.load(open(build / "build-manifest.json", encoding="utf-8"))
        channel = manifest.get("release_channel")
        r = run(validator, build, assets, release=False)
        ok = r.returncode == 0
        print(f"{'OK ' if ok else 'FAIL'} structure {build.name} ({channel})")
        if not ok:
            failed += 1
            print(r.stdout[-1200:])
        if channel == "component-library":
            r = run(validator, build, assets, release=True)
            ok = r.returncode == 0
            print(f"{'OK ' if ok else 'FAIL'} release   {build.name}")
            if not ok:
                failed += 1
                print(r.stdout[-1600:])
        else:
            r = run(validator, build, assets, release=True)
            if r.returncode == 0:
                print(f"FAIL release   {build.name}: test-only 包不得通过发布层")
                failed += 1
            else:
                print(f"OK  release   {build.name}: test-only 包按预期拒绝")
    failed += check_final_rules()
    if failed:
        print(f"✗ {failed} 项失败")
        return 1
    print("✅ 所有实现包结构/发布边界与最终规则一致性通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
