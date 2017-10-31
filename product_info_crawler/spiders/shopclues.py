# -*- coding: utf-8 -*-
import scrapy
import re
import os

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  raw_html.encode('ascii','ignore')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext=cleantext.strip()
  cleantext=re.sub('\s+',' ',cleantext)
  return cleantext


class ShopcluesSpider(scrapy.Spider):
    name = 'shopclues'
    def __init__(self, product='', domain=None, *args, **kwargs):
        super(ShopcluesSpider, self).__init__(*args, **kwargs)
        self.product_name=product.lower()
        self.product_name=re.sub("[^ a-zA-Z0-9]+", "", self.product_name)
        self.search_url='http://www.shopclues.com/search?q='+self.product_name
        self.allowed_domains = ['www.shopclues.com']
        self.start_urls = [self.search_url]


    
    def parse(self, response):
        print 'Processing...',response.url
        title=[]
        image=[]
        price=[]
        url=[]
        for item in response.css('div#product_list div.row div.column'):
         item_title=item.css('a h3::text').extract_first()
         item_image=item.css('a div.img_section img::attr(data-img)').extract_first()
         item_price=item.css('a span.p_price::text').extract_first()
         item_url=item.css('a::attr(href)').extract_first()
         if(item_title and item_image and item_price and item_url):
          title.append(cleanhtml(item_title))
          image.append(cleanhtml(item_image))
          price.append(cleanhtml(item_price))
          url.append(cleanhtml(item_url))

        print 'Result Counts: ',len(title)

        for item in zip(title,price,image,url):
            scraped_info = {
                'product_name' : item[0],
                'price' : item[1],
                'image_url' : item[2],
                'product_url': item[3],
                'source': 'shopclues.com' 
            }
            yield scraped_info