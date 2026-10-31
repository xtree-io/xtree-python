"""AUTO-GENERATED `jd` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class JdAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def items_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/jd/items/detail", json=body)

    def items_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/jd/items/comments", json=body)

    def items_comments_v2(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/jd/items/comments/v2", json=body)
