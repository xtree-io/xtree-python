"""AUTO-GENERATED `kuaishou` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class KuaishouAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def videos_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/videos/detail", json=body)

    def videos_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/videos/comments", json=body)

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/users/posts", json=body)

    def search_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/search/videos", json=body)

    def videos_short_link(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/videos/short-link", json=body)

    def hot_board(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/hot/board", json=body)

    def ids_resolve(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/kuaishou/ids/resolve", json=body)
