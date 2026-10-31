"""XTreeClient — entry point for the Python SDK."""

from __future__ import annotations

import os
from typing import Any

from xtree._http import DEFAULT_BASE_URL, HTTPClient
from xtree.account import AccountAPI
from xtree.types import APIResponse, ResponseMeta
from xtree.wechat import WechatAPI
from xtree.douyin import DouyinAPI
from xtree.xhs import XhsAPI
from xtree.kuaishou import KuaishouAPI
from xtree.weibo import WeiboAPI
from xtree.bilibili import BilibiliAPI
from xtree.tiktok import TiktokAPI
from xtree.youtube import YoutubeAPI
from xtree.facebook import FacebookAPI
from xtree.taobao import TaobaoAPI
from xtree.jd import JdAPI
from xtree.pdd import PddAPI


class XTreeClient:
    """HTTP client for https://api.xtree.io/api."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        verify_code: str | None = None,
        timeout: float = 60.0,
        http_client: Any | None = None,
    ) -> None:
        key = api_key or os.environ.get("XTREE_API_KEY")
        if not key:
            raise ValueError(
                "api_key is required (pass api_key= or set XTREE_API_KEY)"
            )
        url = base_url or os.environ.get("XTREE_BASE_URL") or DEFAULT_BASE_URL
        vcode = verify_code or os.environ.get("XTREE_VERIFY_CODE")
        self._http = HTTPClient(
            api_key=key,
            base_url=url,
            verify_code=vcode,
            timeout=timeout,
            client=http_client,
        )
        self.account = AccountAPI(self._http)
        self.wechat = WechatAPI(self._http)
        self.douyin = DouyinAPI(self._http)
        self.xhs = XhsAPI(self._http)
        self.kuaishou = KuaishouAPI(self._http)
        self.weibo = WeiboAPI(self._http)
        self.bilibili = BilibiliAPI(self._http)
        self.tiktok = TiktokAPI(self._http)
        self.youtube = YoutubeAPI(self._http)
        self.facebook = FacebookAPI(self._http)
        self.taobao = TaobaoAPI(self._http)
        self.jd = JdAPI(self._http)
        self.pdd = PddAPI(self._http)

    @property
    def last_meta(self) -> ResponseMeta | None:
        return self._http.last_meta

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> APIResponse[Any]:
        """Low-level API call with envelope parsing."""
        resp = self._http.request(method, path, json=json, params=params)
        self._http.last_meta = resp.meta
        return resp

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> XTreeClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
