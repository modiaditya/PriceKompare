'''
Created on Nov 24, 2013

@author: amodi
'''
from HtmlHelper import *
from BeautifulSoup import BeautifulSoup
from Item import *


class FlipkartItem(Item):

    def __init__(self, item_url):
        super(FlipkartItem,self).__init__(item_url)
    
    def parseHtmlAndStoreData(self):
        htmlBeautifulSoup = BeautifulSoup(self.get_html())
        htmlBody = htmlBeautifulSoup.body
        self.title = htmlBody.find(itemprop="name").string.strip()
        self.price = htmlBody.find(itemprop="price").get("content")