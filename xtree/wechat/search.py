"""WeChat 搜一搜 endpoints."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse
from xtree.wechat._helpers import post, search_body


class WechatSearchAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def articles(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/articles",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def articles_categories(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/articles/categories",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def videos(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/videos",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def videos_tab(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/videos/tab",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def videos_categories(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/videos/categories",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def mixed(
        self,
        *,
        keyword: str | None = None,
        mode: int | None = None,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        body: dict[str, Any] = {"page": page, **extra}
        if keyword is not None:
            body["keyword"] = keyword
        if mode is not None:
            body["mode"] = mode
        if session is not None:
            body["session"] = session
        return post(self._http, "/wechat/search/mixed", body)

    def accounts(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/accounts",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def suggestions(
        self,
        *,
        keyword: str,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(self._http, "/wechat/search/suggestions", {"keyword": keyword, **extra})

    def miniprograms_categories(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/miniprograms/categories",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def index_categories(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/index/categories",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def channels_accounts_categories(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/search/channels/accounts/categories",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )
