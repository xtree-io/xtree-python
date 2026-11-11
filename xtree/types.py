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
    observation_id: str | None = None
    observed_at: str | None = None
    basis: str | None = None
    contract_rev: int | None = None
    origin: str | None = None
    cache_hit: bool | None = None
    cache_age_sec: int | None = None

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> ResponseMeta:
        return cls(
            request_id=str(raw.get("request_id") or ""),
            cost_cny=_optional_float(raw.get("cost_cny")),
            balance_cny=_optional_float(raw.get("balance_cny")),
            rate_limit_remaining=_optional_int(raw.get("rate_limit_remaining")),
            observation_id=_optional_str(raw.get("observation_id")),
            observed_at=_optional_str(raw.get("observed_at")),
            basis=_optional_str(raw.get("basis")),
            contract_rev=_optional_int(raw.get("contract_rev")),
            origin=_optional_str(raw.get("origin")),
            cache_hit=_optional_bool(raw.get("cache_hit")),
            cache_age_sec=_optional_int(raw.get("cache_age_sec")),
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


def _optional_str(value: Any) -> str | None:
    if value is None or value == "":
        return None
    return str(value)


def _optional_bool(value: Any) -> bool | None:
    if value is None:
        return None
    return bool(value)
