"""AUTO-GENERATED `facebook` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class FacebookAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def search_general(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/facebook/search/general", json=body)

    def search_users(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/facebook/search/users", json=body)
