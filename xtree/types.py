"""Shared response types."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ResponseMeta:
    request_id: str
    cost_cny: float | None = None
    balance_cny: float | None = None
    rate_limit_remaining: int | None = None

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> ResponseMeta:
        return cls(
            request_id=str(raw.get("request_id") or ""),
            cost_cny=_optional_float(raw.get("cost_cny")),
            balance_cny=_optional_float(raw.get("balance_cny")),
            rate_limit_remaining=_optional_int(raw.get("rate_limit_remaining")),
        )


@dataclass(frozen=True)
class APIResponse(Generic[T]):
    data: T
    meta: ResponseMeta


def _optional_float(value: Any) -> float | None:
    if value is None:
        return None
    return float(value)


def _optional_int(value: Any) -> int | None:
    if value is None:
        return None
    return int(value)
