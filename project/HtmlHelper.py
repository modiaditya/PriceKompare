import urllib2
class HtmlHelper(object):

     @staticmethod
     def getHtml(link):
         openwebsite = urllib2.urlopen(link)
         html = openwebsite.read()
         return html