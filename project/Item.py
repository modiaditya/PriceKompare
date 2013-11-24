'''
Created on Nov 24, 2013

@author: amodi
'''
from HtmlHelper import *

class Item(object):
    
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
    
        