# -*- coding: utf-8 -*-
import scrapy


class ImovSpider(scrapy.Spider):
    name = 'imov'
    start_urls = ['https://www.imovirtual.com/arrendar/apartamento/lisboa/?search%5Bfilter_enum_rooms_num%5D%5B0%5D=zero&search%5Bfilter_enum_rooms_num%5D%5B1%5D=1&search%5Bfilter_enum_rooms_num%5D%5B2%5D=2&search%5Bfilter_enum_rooms_num%5D%5B3%5D=3&search%5Bfilter_enum_rooms_num%5D%5B4%5D=4&search%5Bdescription%5D=1']

    def parse(self, response):
    	print('Wait a moment, please. Scraping the site ' + response.url)
    	for immobile in response.css('div.offer-item-details'):
	    	item = {
		    	'title': immobile.css('span.offer-item-title::text').getall(),
		    	'address': immobile.css('p.text-nowrap.hidden-xs::text').getall(),
		    	'tipology': immobile.css('li.offer-item-rooms.hidden-xs::text').getall(),
		    	'area': immobile.css('li.hidden-xs.offer-item-area::text').getall(),
		    	'monthly_cost': immobile.css('li.offer-item-price::text').getall(),
	    	}
	    	yield item
