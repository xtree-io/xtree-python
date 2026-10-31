"""WeChat library (ES-backed) endpoints — Phase 2."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse
from xtree.wechat._helpers import post


class WechatLibraryAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def search_articles(
        self,
        keyword: str,
        *,
        page: int = 1,
        page_size: int = 20,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/library/articles/search",
            {"keyword": keyword, "page": page, "page_size": page_size, **extra},
        )

    def search_articles_tokenized(
        self,
        keyword: str,
        *,
        page: int = 1,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/library/articles/search/tokenized",
            {"keyword": keyword, "page": page, **extra},
        )

    def search_accounts(
        self,
        keyword: str,
        *,
        page: int = 1,
        page_size: int = 20,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/library/accounts/search",
            {"keyword": keyword, "page": page, "page_size": page_size, **extra},
        )

    def accounts_metrics(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/library/accounts/metrics", body)
