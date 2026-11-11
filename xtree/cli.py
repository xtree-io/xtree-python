"""xtree CLI — balance, wechat helpers, and raw call."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from xtree.client import XTreeClient
from xtree.exceptions import XTreeError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="xtree", description="XTREE API CLI")
    parser.add_argument("--json", action="store_true", help="Print data as JSON")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print meta to stderr (request_id, cost_cny, balance_cny)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("balance", help="GET /account/balance")

    call = sub.add_parser("call", help="Raw API call (any path)")
    call.add_argument("method", choices=["GET", "POST"])
    call.add_argument("path", help="API path, e.g. /wechat/search/articles")
    call.add_argument("--body", default=None, help="JSON body for POST")
    call.add_argument("--body-file", default=None, help="JSON file for POST body")

    wechat = sub.add_parser("wechat", help="WeChat platform shortcuts")
    wechat_sub = wechat.add_subparsers(dest="wechat_group", required=True)

    search = wechat_sub.add_parser("search", help="搜一搜")
    search_sub = search.add_subparsers(dest="search_action", required=True)
    for name, help_text in [
        ("articles", "POST /wechat/search/articles"),
        ("videos", "POST /wechat/search/videos"),
        ("mixed", "POST /wechat/search/mixed"),
        ("accounts", "POST /wechat/search/accounts"),
        ("suggestions", "POST /wechat/search/suggestions"),
    ]:
        p = search_sub.add_parser(name, help=help_text)
        p.add_argument("--keyword", required=True)
        p.add_argument("--page", type=int, default=1)
        p.add_argument("--session", default=None)

    library = wechat_sub.add_parser("library", help="库搜索 (Phase 2)")
    library_sub = library.add_subparsers(dest="library_action", required=True)
    lib_articles = library_sub.add_parser("articles", help="POST /wechat/library/articles/search")
    lib_articles.add_argument("--keyword", required=True)
    lib_articles.add_argument("--page", type=int, default=1)

    args = parser.parse_args(argv)
    resp = None

    try:
        with XTreeClient() as client:
            resp = _dispatch(client, args, parser)
            if args.verbose and client.last_meta:
                _print_meta(client.last_meta)
    except (XTreeError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.json or args.command != "balance":
        print(json.dumps(resp.data, ensure_ascii=False, indent=2))
    else:
        balance = (resp.data or {}).get("balance_cny")
        print(f"balance_cny: {balance}")

    return 0


def _dispatch(client: XTreeClient, args: argparse.Namespace, parser: argparse.ArgumentParser) -> Any:
    if args.command == "balance":
        return client.account.balance()

    if args.command == "call":
        body = _load_body(args.body, args.body_file)
        return client.request(args.method, args.path, json=body if args.method == "POST" else None)

    if args.command == "wechat" and args.wechat_group == "search":
        kwargs = {"keyword": args.keyword, "page": args.page, "session": args.session}
        actions = {
            "articles": client.wechat.search.articles,
            "videos": client.wechat.search.videos,
            "mixed": client.wechat.search.mixed,
            "accounts": client.wechat.search.accounts,
            "suggestions": client.wechat.search.suggestions,
        }
        fn = actions.get(args.search_action)
        if fn is None:
            parser.error("unknown wechat search action")
        return fn(**kwargs)

    if args.command == "wechat" and args.wechat_group == "library":
        if args.library_action == "articles":
            return client.wechat.library.search_articles(args.keyword, page=args.page)

    parser.error("unknown command")
    return None


def _load_body(body: str | None, body_file: str | None) -> dict[str, Any]:
    if body_file:
        return json.loads(Path(body_file).read_text(encoding="utf-8"))
    if body:
        return json.loads(body)
    return {}


def _print_meta(meta: Any) -> None:
    payload = {
        "request_id": meta.request_id,
        "cost_cny": meta.cost_cny,
        "balance_cny": meta.balance_cny,
        "rate_limit_remaining": meta.rate_limit_remaining,
    }
    for key in (
        "observation_id",
        "observed_at",
        "basis",
        "contract_rev",
        "origin",
        "cache_hit",
        "cache_age_sec",
    ):
        value = getattr(meta, key, None)
        if value is not None:
            payload[key] = value
    print(json.dumps(payload, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
