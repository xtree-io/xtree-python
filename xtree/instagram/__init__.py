"""AUTO-GENERATED `instagram` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class InstagramAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/instagram/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/instagram/users/posts", json=body)

    def posts_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/instagram/posts/detail", json=body)

    def posts_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/instagram/posts/comments", json=body)

    def search_users(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/instagram/search/users", json=body)
