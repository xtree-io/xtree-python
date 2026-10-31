"""Client integration tests with httpx mock transport."""

import httpx
import pytest

from xtree.client import XTreeClient


def _envelope(data, **meta):
    return {
        "ok": True,
        "data": data,
        "meta": {"request_id": "01JMOCK", **meta},
        "error": None,
    }


def test_balance():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["X-XTREE-Key"] == "xt_test_key"
        assert request.url.path == "/api/account/balance"
        return httpx.Response(200, json=_envelope({"balance_cny": 42.5}))

    transport = httpx.MockTransport(handler)
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test_key", http_client=http)
    resp = client.account.balance()
    assert resp.data["balance_cny"] == 42.5
    assert client.last_meta is not None
    assert client.last_meta.request_id == "01JMOCK"


def test_search_videos():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["body"] = request.content.decode()
        return httpx.Response(
            200,
            json=_envelope({"items": [], "session": "next"}, cost_cny=0.5),
        )

    transport = httpx.MockTransport(handler)
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test_key", http_client=http)
    resp = client.wechat.search.videos(keyword="test", page=2)
    assert resp.data["session"] == "next"
    assert client.last_meta.cost_cny == 0.5
    assert '"keyword":"test"' in captured["body"]


def test_missing_api_key():
    with pytest.raises(ValueError, match="XTREE_API_KEY"):
        XTreeClient(api_key=None)
