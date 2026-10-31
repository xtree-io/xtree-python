"""Shared helpers for WeChat API modules."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


def post(http: HTTPClient, path: str, body: dict[str, Any] | None = None) -> APIResponse[Any]:
    resp = http.request("POST", path, json=body or {})
    http.last_meta = resp.meta
    return resp


def get(http: HTTPClient, path: str) -> APIResponse[Any]:
    resp = http.request("GET", path)
    http.last_meta = resp.meta
    return resp


def search_body(
    *,
    keyword: str,
    page: int = 1,
    session: str | None = None,
    **extra: Any,
) -> dict[str, Any]:
    body: dict[str, Any] = {"keyword": keyword, "page": page, **extra}
    if session is not None:
        body["session"] = session
    return body


def page_body(*, page: int = 1, session: str | None = None, **extra: Any) -> dict[str, Any]:
    body: dict[str, Any] = {"page": page, **extra}
    if session is not None:
        body["session"] = session
    return body
