"""WeChat 公众号 / 历史发文 endpoints."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse
from xtree.wechat._helpers import page_body, post


class WechatAccountsAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def posts_today(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/posts/today", body)

    def posts(
        self,
        account_id: str,
        *,
        page: int = 1,
        cursor: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        """历史发文列表。翻页取上一轮 data.next_cursor 回传 cursor。"""
        body = page_body(page=page, account_id=account_id, **extra)
        if cursor is not None:
            body["cursor"] = cursor
        return post(self._http, "/wechat/accounts/posts/list", body)

    def gh_id_posts(
        self,
        gh_id: str,
        *,
        page: int = 1,
        cursor: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        body = page_body(page=page, gh_id=gh_id, **extra)
        if cursor is not None:
            body["cursor"] = cursor
        return post(self._http, "/wechat/accounts/ghid/posts", body)

    def ghid_posts(
        self,
        gh_id: str,
        *,
        page: int = 1,
        cursor: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        """Deprecated alias for gh_id_posts."""
        return self.gh_id_posts(gh_id, page=page, cursor=cursor, **extra)

    def gh_id_channels(self, gh_id: str, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/ghid/channels", {"gh_id": gh_id, **body})

    def ghid_channels(self, gh_id: str, **body: Any) -> APIResponse[Any]:
        """Deprecated alias for gh_id_channels."""
        return self.gh_id_channels(gh_id, **body)

    def principal(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/principal", body)

    def profile(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/profile", body)

    def search(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/search", body)

    def search_gh(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/search/gh", body)

    def search_by_owner(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/search-by-owner", body)

    def search_by_owner_live(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/accounts/search-by-owner/live", body)
