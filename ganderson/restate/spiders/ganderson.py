import scrapy


class GandersonSpider(scrapy.Spider):
    name = 'ganderson'
    allowed_domains = ['ganderson.com']
    start_urls = ['http://ganderson.com/rent-long-beach-island-homes//']

    def parse(self, response):
        
        data = response.xpath('//div[@class="property-listing-detail"]')
        for property in data:
            town1 = property.xpath('.//h3/text()').get().strip()  
            town2 = property.xpath('.//h3/span[2]/text()').get().strip() 
            address = property.xpath('.//h4/a/text()').get()
            id= property.xpath('.//div[2]/p[1]/text()').get()[13:]
            yield {
                'town1': town1,
                'town2': town2,
                'address': address,
                'id': id
            }
        next_page = response.xpath('//a[@class="next page-numbers"]/@href').get() 
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        
