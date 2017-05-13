#!/usr/bin/python
# coding:utf-8
import urlManager,download,output,parseHtml

import traceback

class spider(object):
	"""docstring for spider"""
	def __init__(self):
		super(spider, self).__init__()
		#self.arg = arg
		self.urls = urlManager.urlManager()
		self.download = download.downloader()
		self.parse = parseHtml.parseHtml()
		self.outputer = output.outputer()
		self.count = 0

	def crawl(self,url,path):
		
		self.urls.addNewURL(url)
		while self.urls.existNewURL():
			try:
				url = self.urls.getNewURL()
				print "count %d :%s" %(self.count,url)
				content = self.download.downloadHTML(url)
				newURLs,data = self.parse.parse(url,content)
			
				self.urls.addNewURLs(newURLs)
				self.outputer.collect_data(data)

			
				if (self.count == 10):
					break
				self.count += 1
			except:
				print "crawl failed"
				traceback.print_exc()

		self.outputer.outputhtml(path)


if __name__ == "__main__":
	root_url = "http://baike.baidu.com/item/Python"
	path = "output.html"
	spiderMain = spider()
	spiderMain.crawl(root_url,path)