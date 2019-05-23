# import module
import scrapy


class ImovSpider(scrapy.Spider):
	# give a spider name
    name = 'prop'
    # list of url where spider will begin to crawl
    start_urls = ['https://www.imovirtual.com/arrendar/apartamento/lisboa/?search%5Bfilter_enum_rooms_num%5D%5B0%5D=zero&search%5Bfilter_enum_rooms_num%5D%5B1%5D=1&search%5Bfilter_enum_rooms_num%5D%5B2%5D=2&search%5Bfilter_enum_rooms_num%5D%5B3%5D=3&search%5Bfilter_enum_rooms_num%5D%5B4%5D=4&search%5Bdescription%5D=1']

    def parse(self, response):
    	# print what the spider is doing
    	print('Please, wait a moment while we are scraping the site ' + response.url)

    	# loop on each property on page and extract info using css selector
    	for property in response.css('div.offer-item-details'):
    		# create a dictionary to store the scraped info
	    	item = {
		    	# extract property name
		    	'title': property.css('span.offer-item-title::text').getall(),
		    	# extract property address
		    	'address': property.css('p.text-nowrap.hidden-xs::text').getall(),
		    	# extract property typology
		    	'typology': property.css('li.offer-item-rooms.hidden-xs::text').getall(),
		    	# extract property area in square metres
		    	'area': property.css('li.hidden-xs.offer-item-area::text').getall(),
		    	# extract monthly rental cost
		    	'monthly_cost': property.css('li.offer-item-price::text').getall(),
	    	}
	    	# give the scraped info to scrapy
	    	yield item
