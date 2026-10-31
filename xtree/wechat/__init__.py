"""WeChat platform endpoints."""

from xtree.wechat.accounts import WechatAccountsAPI
from xtree.wechat.articles import WechatArticlesAPI
from xtree.wechat.channels import WechatChannelsAPI
from xtree.wechat.library import WechatLibraryAPI
from xtree.wechat.links import WechatLinksAPI
from xtree.wechat.search import WechatSearchAPI


class WechatAPI:
    def __init__(self, http) -> None:
        self.search = WechatSearchAPI(http)
        self.channels = WechatChannelsAPI(http)
        self.accounts = WechatAccountsAPI(http)
        self.articles = WechatArticlesAPI(http)
        self.library = WechatLibraryAPI(http)
        self.links = WechatLinksAPI(http)
