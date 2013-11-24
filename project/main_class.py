'''
Created on Nov 23, 2013

@author: amodi
'''
from SnapdealItem import *
from FlipkartItem import * 

if __name__ == '__main__':
    
    #item = SnapdealItem("http://www.snapdeal.com/product/google-nexus-4/1427672")
    item = FlipkartItem("http://www.flipkart.com/google-nexus-4/p/itmdzsgjkemg8mzp")
    print item.parseHtmlAndStoreData()
    print item.title
    print item.price
    print item.delivery_time