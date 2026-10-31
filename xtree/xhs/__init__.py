"""AUTO-GENERATED `xhs` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class XhsAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def notes_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/notes/detail", json=body)

    def notes_search(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/notes/search", json=body)

    def users_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/users/profile", json=body)

    def users_notes(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/users/notes", json=body)

    def notes_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/notes/comments", json=body)

    def notes_sub_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/notes/sub-comments", json=body)

    def topics_list(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/topics/list", json=body)

    def ids_resolve(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/xhs/ids/resolve", json=body)
