"""XTREE API errors mapped from envelope.error.code."""

from __future__ import annotations

from typing import Any


class XTreeError(Exception):
    """Base error for failed API calls."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "UNKNOWN",
        status_code: int | None = None,
        request_id: str | None = None,
        details: Any = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.status_code = status_code
        self.request_id = request_id
        self.details = details

    def __str__(self) -> str:
        parts = [self.code, str(self.args[0])]
        if self.request_id:
            parts.append(f"request_id={self.request_id}")
        return ": ".join(parts)


class XTreeAuthError(XTreeError):
    """401 UNAUTHORIZED or 403 FORBIDDEN."""


class XTreeValidationError(XTreeError):
    """400 VALIDATION_ERROR."""


class XTreeInsufficientBalanceError(XTreeError):
    """402 INSUFFICIENT_BALANCE."""


class XTreeRateLimitError(XTreeError):
    """429 RATE_LIMITED."""


class XTreeUpstreamError(XTreeError):
    """502 UPSTREAM_ERROR or 503 EDGE_UNAVAILABLE."""


_ERROR_MAP: dict[str, type[XTreeError]] = {
    "UNAUTHORIZED": XTreeAuthError,
    "FORBIDDEN": XTreeAuthError,
    "VALIDATION_ERROR": XTreeValidationError,
    "INSUFFICIENT_BALANCE": XTreeInsufficientBalanceError,
    "RATE_LIMITED": XTreeRateLimitError,
    "UPSTREAM_ERROR": XTreeUpstreamError,
    "EDGE_UNAVAILABLE": XTreeUpstreamError,
    "INTERNAL_ERROR": XTreeError,
    "NOT_FOUND": XTreeError,
}


def error_from_envelope(
    payload: dict[str, Any],
    *,
    status_code: int | None = None,
) -> XTreeError:
    err = payload.get("error") or {}
    code = str(err.get("code") or "UNKNOWN")
    message = str(err.get("message") or "API request failed")
    meta = payload.get("meta") or {}
    request_id = meta.get("request_id")
    details = err.get("details")
    cls = _ERROR_MAP.get(code, XTreeError)
    return cls(
        message,
        code=code,
        status_code=status_code,
        request_id=request_id,
        details=details,
    )
