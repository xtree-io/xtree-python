"""WeChat 链接工具."""

from __future__ import annotations

from typing import Any

from xtree._http import HTTPClient
from xtree.types import APIResponse
from xtree.wechat._helpers import post


class WechatLinksAPI:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    def convert(self, **body: Any) -> APIResponse[Any]:
        return post(self._http, "/wechat/links/convert", body)
