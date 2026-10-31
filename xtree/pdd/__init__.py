"""AUTO-GENERATED `pdd` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class PddAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def items_comments_submit(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/pdd/items/comments/submit", json=body)

    def items_comments_status(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/pdd/items/comments/status", json=body)

    def items_comments_fetch(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/pdd/items/comments/fetch", json=body)
