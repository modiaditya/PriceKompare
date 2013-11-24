'''
Created on Nov 23, 2013

@author: amodi
'''
from HtmlHelper import *
from BeautifulSoup import BeautifulSoup
from Item import *

class SnapdealItem(Item):
    
    def __init__(self, item_url):
        super(SnapdealItem,self).__init__(item_url)
    
    def parseHtmlAndStoreData(self):
        htmlBeautifulSoup = BeautifulSoup(self.get_html())
        htmlBody = htmlBeautifulSoup.body
        self.title = htmlBody.find(itemprop="name").string
        self.price = htmlBody.find(id="selling-price-id").string
        self.delivery_time = htmlBody.find(id="mvShippingDays").string
        