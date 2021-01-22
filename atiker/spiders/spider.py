import re

import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import AtikerItem


class AtikerSpider(scrapy.Spider):
	name = 'atiker'
	start_urls = ['http://www.atiker.bg/news/', 'http://www.atiker.bg/bg/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/']

	def parse(self, response, **kwargs):
		post_links = response.xpath('//div[@class="wp-caption alignleft"]/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		lang_dict = {'BG': 'en', 'EU': 'bg'}
		title = response.xpath('//hgroup/h1/text()').get().strip()
		description = response.xpath('//article/div[@class="entry-main"]/div/p').getall()
		description = ' '.join([remove_tags(re.sub('&lt;&lt;&lt; назад', '', p)) for p in description]).strip()
		lang = response.xpath('(//ul[@id="menu-menu02"]/li/a/span/text())[3]').get()
		lang = lang_dict[lang]

		item = ItemLoader(item=AtikerItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('lang', lang)
		print(title)

		return item.load_item()
