"""Envelope parsing tests."""

import pytest

from xtree._http import _unwrap_envelope
from xtree.exceptions import (
    XTreeInsufficientBalanceError,
    XTreeRateLimitError,
    XTreeServiceError,
    XTreeUpstreamError,
)


def test_unwrap_success():
    resp = _unwrap_envelope(
        {
            "ok": True,
            "data": {"balance_cny": 100.0},
            "meta": {"request_id": "01JTEST", "cost_cny": 0},
            "error": None,
        },
        status_code=200,
    )
    assert resp.data["balance_cny"] == 100.0
    assert resp.meta.request_id == "01JTEST"


def test_unwrap_insufficient_balance():
    with pytest.raises(XTreeInsufficientBalanceError) as exc:
        _unwrap_envelope(
            {
                "ok": False,
                "data": None,
                "meta": {"request_id": "01JFAIL"},
                "error": {"code": "INSUFFICIENT_BALANCE", "message": "余额不足"},
            },
            status_code=402,
        )
    assert exc.value.code == "INSUFFICIENT_BALANCE"
    assert exc.value.request_id == "01JFAIL"


def test_unwrap_internal_delivery_failure():
    with pytest.raises(XTreeServiceError) as exc:
        _unwrap_envelope(
            {
                "ok": False,
                "data": None,
                "meta": {"request_id": "01JERR"},
                "error": {"code": "INTERNAL_ERROR", "message": "接口异常"},
            },
            status_code=502,
        )
    assert exc.value.code == "INTERNAL_ERROR"
    assert isinstance(exc.value, XTreeUpstreamError)


def test_unwrap_rate_limited():
    with pytest.raises(XTreeRateLimitError):
        _unwrap_envelope(
            {
                "ok": False,
                "data": None,
                "meta": {"request_id": "01JRATE"},
                "error": {"code": "RATE_LIMITED", "message": "too many requests"},
            },
            status_code=429,
        )
