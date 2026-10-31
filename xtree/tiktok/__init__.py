"""AUTO-GENERATED `tiktok` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class TiktokAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def videos_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/tiktok/videos/detail", json=body)

    def videos_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/tiktok/videos/comments", json=body)

    def videos_sub_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/tiktok/videos/sub-comments", json=body)

    def search_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/tiktok/search/videos", json=body)

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/tiktok/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/tiktok/users/posts", json=body)
