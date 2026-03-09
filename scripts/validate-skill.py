#!/usr/bin/env python3
"""Validate that a SKILL.md file has all required frontmatter fields.

Usage:
    python scripts/validate-skill.py homebrew/SKILL.md

Exits 0 on success, 1 on any validation failure.
"""
import sys
import pathlib
import yaml

REQUIRED_FIELDS = ["name", "description", "argument-hint", "version", "maintainer"]


def load_frontmatter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: file does not start with '---' (no frontmatter)")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: frontmatter block is not closed with '---'")
    return yaml.safe_load(parts[1])


def validate(skill_path_str: str) -> None:
    path = pathlib.Path(skill_path_str).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    fm = load_frontmatter(path)

    errors = []

    # Check required fields are present and non-empty
    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"  Missing or empty field: '{field}'")

    # Check that the 'name' field matches the parent directory name
    # (skill directory name must equal frontmatter name)
    dir_name = path.resolve().parent.name
    if "name" in fm and fm["name"] and fm["name"] != dir_name:
        errors.append(
            f"  Field 'name' value '{fm['name']}' does not match "
            f"directory name '{dir_name}'"
        )

    if errors:
        print(f"FAIL: {path}")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print(f"OK: {path} — all required fields present, name matches directory")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-to-SKILL.md>")
        sys.exit(1)
    validate(sys.argv[1])
