"""AUTO-GENERATED `youtube` platform client."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse


class YoutubeAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def channels_videos(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/channels/videos", json=body)

    def channels_shorts(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/channels/shorts", json=body)

    def channels_streams(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/channels/streams", json=body)

    def search_channels(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/search/channels", json=body)

    def videos_detail(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/videos/detail", json=body)

    def videos_comments(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/videos/comments", json=body)

    def channels_profile(self, **body: Any) -> APIResponse[Any]:
        return self._http.request("POST", "/youtube/channels/profile", json=body)
