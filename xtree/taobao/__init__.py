"""AUTO-GENERATED `taobao` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class TaobaoAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def items_search(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/taobao/items/search", json=body)

    def items_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/taobao/items/detail", json=body)

    def shops_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/taobao/shops/comments", json=body)
