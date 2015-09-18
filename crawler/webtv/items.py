from scrapy.item import Item, Field

class Video(Item):
    name = Field()
    url = Field()
