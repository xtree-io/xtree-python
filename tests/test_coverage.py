"""Coverage tests — SDK registry vs OpenAPI spec."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from xtree.registry import COVERED_ENDPOINTS, SLUG_BY_PATH

ROOT = Path(__file__).resolve().parents[2]  # sdk/
SPEC = ROOT / "openapi" / "spec" / "openapi.json"


def _openapi_operations(spec: dict) -> set[tuple[str, str]]:
    ops: set[tuple[str, str]] = set()
    for path, item in spec["paths"].items():
        for method in item:
            if method in ("get", "post", "put", "patch", "delete"):
                ops.add((method.upper(), path))
    return ops


@pytest.fixture(scope="module")
def openapi_spec() -> dict:
    return json.loads(SPEC.read_text(encoding="utf-8"))


def test_openapi_has_114_operations(openapi_spec: dict) -> None:
    assert len(_openapi_operations(openapi_spec)) == 120


def test_registry_covers_openapi(openapi_spec: dict) -> None:
    openapi_ops = _openapi_operations(openapi_spec)
    covered = set(COVERED_ENDPOINTS)
    assert openapi_ops == covered


def test_slug_map_covers_all_registry_entries() -> None:
    assert set(SLUG_BY_PATH) == set(COVERED_ENDPOINTS)
    assert len(SLUG_BY_PATH) == 120
