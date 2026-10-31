"""AUTO-GENERATED `weibo` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class WeiboAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/users/posts", json=body)

    def users_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/users/videos", json=body)

    def posts_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/posts/detail", json=body)

    def posts_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/posts/comments", json=body)

    def posts_sub_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/posts/sub-comments", json=body)

    def topics_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/topics/detail", json=body)

    def topics_stats(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/topics/stats", json=body)

    def hot_search(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/hot/search", json=body)

    def search_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/weibo/search/posts", json=body)
