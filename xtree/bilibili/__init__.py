"""AUTO-GENERATED `bilibili` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class BilibiliAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def search_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/search/videos", json=body)

    def videos_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/videos/detail", json=body)

    def videos_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/videos/comments", json=body)

    def videos_sub_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/videos/sub-comments", json=body)

    def videos_download(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/videos/download", json=body)

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/users/posts", json=body)

    def users_videos(self, **body: Any) -> APIResponse[Any]:
        """Same as users_posts (the separate endpoint was merged into it)."""
        return self.users_posts(**body)

    def popular_list(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/popular/list", json=body)

    def rank_list(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/rank/list", json=body)

    def hot_search(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/hot/search", json=body)

    def videos_danmaku(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/videos/danmaku", json=body)

    def videos_transcript(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/bilibili/videos/transcript", json=body)
