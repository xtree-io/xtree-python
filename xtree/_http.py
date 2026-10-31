"""HTTP transport with envelope parsing and retries."""

from __future__ import annotations

import time
from typing import Any

import httpx

from xtree.exceptions import XTreeError, error_from_envelope
from xtree.types import APIResponse, ResponseMeta

DEFAULT_BASE_URL = "https://api.xtree.io/api"
API_KEY_HEADER = "X-XTREE-Key"
VERIFY_CODE_HEADER = "X-Verify-Code"
DEFAULT_TIMEOUT = 60.0
RETRY_STATUS = {429, 502, 503}
MAX_RETRIES = 3


class HTTPClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        verify_code: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.Client | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.verify_code = verify_code
        self._owns_client = client is None
        self._client = client or httpx.Client(timeout=timeout)
        self._headers = {
            API_KEY_HEADER: api_key,
            "Accept": "application/json",
            "User-Agent": "xtree-python/0.1.0",
        }
        if verify_code:
            self._headers[VERIFY_CODE_HEADER] = verify_code
        self.last_meta: ResponseMeta | None = None

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def __enter__(self) -> HTTPClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> APIResponse[Any]:
        url = f"{self.base_url}{path}"
        last_exc: Exception | None = None

        for attempt in range(MAX_RETRIES + 1):
            try:
                response = self._client.request(
                    method,
                    url,
                    headers=self._headers,
                    json=json,
                    params=params,
                )
            except httpx.HTTPError as exc:
                last_exc = exc
                if attempt >= MAX_RETRIES:
                    raise XTreeError(str(exc), code="TRANSPORT_ERROR") from exc
                time.sleep(2**attempt * 0.5)
                continue

            payload = _parse_json(response)
            if response.status_code in RETRY_STATUS and attempt < MAX_RETRIES:
                time.sleep(2**attempt * 0.5)
                continue

            return _unwrap_envelope(payload, status_code=response.status_code)

        if last_exc:
            raise XTreeError(str(last_exc), code="TRANSPORT_ERROR") from last_exc
        raise XTreeError("Request failed after retries", code="TRANSPORT_ERROR")


def _parse_json(response: httpx.Response) -> dict[str, Any]:
    try:
        data = response.json()
        if isinstance(data, dict):
            return data
    except ValueError:
        pass
    raise XTreeError(
        f"Non-JSON response (HTTP {response.status_code})",
        code="INVALID_RESPONSE",
        status_code=response.status_code,
    )


def _unwrap_envelope(payload: dict[str, Any], *, status_code: int) -> APIResponse[Any]:
    meta = ResponseMeta.from_dict(payload.get("meta") or {})
    if payload.get("ok") is True:
        return APIResponse(data=payload.get("data"), meta=meta)
    raise error_from_envelope(payload, status_code=status_code)
