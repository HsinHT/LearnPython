# cd 磁碟槽:\LearnPython\crawler\scrapy\tutorialscrapy\
# 用法：scrapy crawl dmoz -o 檔名.json -t json
# ex: scrapy crawl dmoz -o items.json -t json

import scrapy

from tutorialscrapy.items import DmozItem
from itertools import zip_longest

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz-odp.org']
    start_urls = [
        'https://dmoz-odp.org/Computers/Programming/Languages/Python/Books/',
        'https://dmoz-odp.org/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites_title = sel.xpath('//div[@class="site-title"]')
        sites_link = sel.xpath('//div[@class="title-and-desc"]')
        sites_desc = sel.xpath('//div[@class="site-descr "]')

        items_title = []
        items_link = []
        items_desc = []
        items = []

        for site_title in sites_title:
            get_title = site_title.xpath('text()').extract()
            items_title.append(get_title)

        for site_link in sites_link:
            get_link = site_link.xpath('a/@href').extract()
            items_link.append(get_link)

        for site_desc in sites_desc:
            get_desc = site_desc.xpath('text()').extract()
            items_desc.append(get_desc)

        for title, link, desc in zip_longest(items_title, items_link, items_desc):
            item = DmozItem()
            item['title'] = title
            item['link'] = link
            item['desc'] = desc
            items.append(item)

        return items

