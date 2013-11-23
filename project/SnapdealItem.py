'''
Created on Nov 23, 2013

@author: amodi
'''
from HtmlHelper import *
from BeautifulSoup import BeautifulSoup

class SnapdealItem(object):
    
    title = ""
    price = ""
    item_url = ""
    rating = ""
    num_ratings = ""
    htmlBeautifulSoup = ""
    delivery_time = ""
    
    def __init__(self, item_url):
        self.item_url = item_url
    
    def get_html(self):
        html =  HtmlHelper.getHtml(self.item_url)
        return html
    
    def parseHtmlAndStoreData(self):
        htmlBeautifulSoup = BeautifulSoup(self.get_html())
        htmlBody = htmlBeautifulSoup.body
        self.title = htmlBody.find(itemprop="name").string
        self.price = htmlBody.find(id="selling-price-id").string
        self.delivery_time = htmlBody.find(id="mvShippingDays").string
        