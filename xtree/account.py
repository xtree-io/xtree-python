"""Account endpoints."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class AccountAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def balance(self) -> APIResponse[dict[str, Any]]:
        """GET /account/balance — free, returns balance_cny."""
        resp = self._http.request("GET", "/account/balance")
        self._http.last_meta = resp.meta
        return resp
