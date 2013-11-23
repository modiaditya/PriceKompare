'''
Created on Nov 23, 2013

@author: amodi
'''
from SnapdealItem import * 

if __name__ == '__main__':
    item = SnapdealItem("http://www.snapdeal.com/product/google-nexus-4/1427672")
    print item.parseHtmlAndStoreData()
    print item.title
    print item.price
    print item.delivery_time