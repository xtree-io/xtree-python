"""WeChat 视频号 endpoints."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse
from xtree.wechat._helpers import page_body, post, search_body


class WechatChannelsAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def search(
        self,
        *,
        keyword: str,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/channels/search",
            search_body(keyword=keyword, page=page, session=session, **extra),
        )

    def resolve(self, **body: Any) -> APIResponse[Any]:
        """POST /wechat/channels/resolve — username or url."""
        return post(self._http, "/wechat/channels/resolve", body)

    def feeds(
        self,
        channel_id: str,
        *,
        page: int = 1,
        session: str | None = None,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/channels/feeds/list",
            page_body(page=page, session=session, channel_id=channel_id, **extra),
        )

    def feed_download_url(self, feed_id: str, **body: Any) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/channels/feeds/download-url",
            {"feed_id": feed_id, **body},
        )

    def live_replays(
        self,
        channel_id: str,
        *,
        page: int = 1,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/channels/live-replays",
            page_body(page=page, channel_id=channel_id, **extra),
        )

    def comments(
        self,
        feed_id: str,
        *,
        page: int = 1,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/channels/feeds/comments",
            page_body(page=page, feed_id=feed_id, **extra),
        )

    def comment_replies(
        self,
        feed_id: str,
        comment_id: str,
        *,
        page: int = 1,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/channels/feeds/sub-comments",
            page_body(page=page, feed_id=feed_id, comment_id=comment_id, **extra),
        )

    def resolve_url(self, *, url: str, **extra: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/channels/feeds/resolve-url", {"url": url, **extra})

    def feed_title(self, feed_id: str, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/channels/feeds/title", {"feed_id": feed_id, **body})

    def feed_metrics(self, feed_id: str, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/channels/feeds/metrics", {"feed_id": feed_id, **body})

    def feed_convert_id(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/channels/feeds/convert-id", body)

    def feed_short_url(self, feed_id: str, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/channels/feeds/short-url", {"feed_id": feed_id, **body})
