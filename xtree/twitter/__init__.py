"""AUTO-GENERATED `twitter` platform client (X)."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class TwitterAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/twitter/users/profile", json=body)

    def users_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/twitter/users/posts", json=body)

    def posts_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/twitter/posts/detail", json=body)

    def posts_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/twitter/posts/comments", json=body)

    def search_posts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/twitter/search/posts", json=body)
