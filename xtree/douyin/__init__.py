"""AUTO-GENERATED `douyin` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class DouyinAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def videos_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/videos/detail", json=body)

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/users/posts", json=body)

    def videos_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/videos/comments", json=body)

    def videos_sub_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/videos/sub-comments", json=body)

    def search_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/search/videos", json=body)

    def search_suggestions(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/search/suggestions", json=body)

    def users_creator_metrics(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/users/creator-metrics", json=body)

    def ids_resolve(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/ids/resolve", json=body)

    def hot_search(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/hot/search", json=body)

    def videos_metrics(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/videos/metrics", json=body)

    def topics_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/topics/detail", json=body)

    def topics_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/douyin/topics/videos", json=body)
