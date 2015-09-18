# Scrapy settings for dirbot project

SPIDER_MODULES = ['webtv.spiders']
NEWSPIDER_MODULE = 'webtv.spiders'
DEFAULT_ITEM_CLASS = 'webtv.items.Video'

ITEM_PIPELINES = {'webtv.pipelines.SVTPlayDownload': 1}