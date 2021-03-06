import re, logging
from urlparse import urlparse, urlunparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from webtv.items import Video

def stripurl(url):
    """
    Strip trailing ;parameters?query=123#fragment from url to normalize it
    """
    return urlunparse(urlparse(url)[0:3] + (None,None,None)).rstrip('/')

class SVTPlaySpider(CrawlSpider):
    name = 'svtplay'
    allowed_domains = ['svtplay.se']
    start_urls = [
        'http://www.svtplay.se/',
    ]

    rules = (
        Rule(LinkExtractor(allow=('svtplay.se/video/\d+/', )), callback='parse_video'),
        Rule(LinkExtractor(allow=('svtplay.se/klipp/\d+/', )), callback='parse_video'),
        Rule(LinkExtractor()),
    )

    def parse_video(self, response):
        sel = Selector(response)
        item = Video()
        item['name'] = sel.xpath('//head/title/text()').extract()
        item['url'] = stripurl(response.url)
        logging.info("Video '%s' at '%s'", item['name'], item['url'])
        return item
