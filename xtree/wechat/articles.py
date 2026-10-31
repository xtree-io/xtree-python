"""WeChat 文章互动 endpoints."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse
from xtree.wechat._helpers import page_body, post


class WechatArticlesAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def metrics(self, *, url: str, **extra: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/articles/metrics", {"url": url, **extra})

    def metrics_pro(self, *, url: str, **extra: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/articles/metrics/pro", {"url": url, **extra})

    def summary(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/articles/summary", body)

    def detail(self, article_id: str) -> APIResponse[Any]:
        return post(self._http, "/wechat/articles/detail", {"article_id": article_id})

    def detail_with_video(self, article_id: str) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/articles/detail-with-video",
            {"article_id": article_id},
        )

    def html(self, *, url: str, **extra: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/articles/html", {"url": url, **extra})

    def comments(
        self,
        article_id: str,
        *,
        page: int = 1,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/articles/comments",
            page_body(page=page, article_id=article_id, **extra),
        )

    def comment_replies(
        self,
        article_id: str,
        comment_id: str,
        *,
        page: int = 1,
        **extra: Any,
    ) -> APIResponse[Any]:
        return post(
            self._http,
            "/wechat/articles/sub-comments",
            page_body(page=page, article_id=article_id, comment_id=comment_id, **extra),
        )
