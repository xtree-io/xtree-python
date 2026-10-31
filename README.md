# XTREE Python SDK

Python client for the [XTREE](https://www.xtree.io) social media data API. Scripts and backends call REST through `XTreeClient`. Agent hosts that want tools should use [xtree-mcp](https://github.com/xtree-io/xtree-mcp) (WeChat tools today). **Not** a BI or analytics platform.

Covers the public OpenAPI surface (WeChat, Douyin, Xiaohongshu, and the other live platforms). See [API reference](https://www.xtree.io/docs/apis) and [OpenAPI](https://api.xtree.io/api/openapi.json). Facebook, JD, and PDD client classes exist in the source tree and are not live catalog products.

## Install

PyPI package name for this SDK is not published yet (`xtree` on PyPI is an unrelated project). Install from GitHub:

```bash
pip install "git+https://github.com/xtree-io/xtree-python.git"
```

Requires Python 3.10+.

## Get an API Key

1. Sign up at [www.xtree.io](https://www.xtree.io/login?tab=signup).
2. Copy a key from the account console (`xt_live_...`).
3. Export it:

```bash
export XTREE_API_KEY=xt_live_...
```

## Quickstart

```python
from xtree import XTreeClient

client = XTreeClient()  # reads XTREE_API_KEY

print(client.account.balance().data["balance_cny"])

resp = client.wechat.search.articles(keyword="人民日报", page=1)
print(resp.data)
print(client.last_meta.cost_cny if client.last_meta else None)
```

## CLI

```bash
xtree balance
xtree wechat search videos --keyword "人民日报" --json
xtree call POST /wechat/search/articles --body '{"keyword":"人民日报"}'
```

## Billing

Pay per call from your wallet (CNY). Incomplete delivery is not billed. Unit prices: [API Catalog](https://www.xtree.io/catalog). No volume tiers and no `/pricing` plans page. Bulk / bank transfer / enterprise: [business@xtree.io](mailto:business@xtree.io).

## Docs

- Quick start: https://www.xtree.io/docs
- API reference: https://www.xtree.io/docs/apis
- OpenAPI: https://api.xtree.io/api/openapi.json
- MCP for agents: https://github.com/xtree-io/xtree-mcp
- Examples: https://github.com/xtree-io/xtree-examples

## Environment

| Variable | Required | Default |
|----------|----------|---------|
| `XTREE_API_KEY` | yes | — |
| `XTREE_BASE_URL` | no | `https://api.xtree.io/api` |
| `XTREE_VERIFY_CODE` | no | — |

## Mirror notice

**Do not develop in this repository.** It is a public mirror synced from a private monorepo. Open issues here for SDK / docs feedback. Contact: [business@xtree.io](mailto:business@xtree.io).

## License

MIT.
