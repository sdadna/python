#!/usr/bin/python
# coding:utf-8

import output,parse,url_manager,download

class Spider_zh5000(object):
	"""docstring for Spider_zh5000"""
	def __init__(self):
		super(Spider_zh5000, self).__init__()
		self.urls = url_manager.UrlManager()
		self.parser = parse.Parser()
		self.download =  download.Downloader()
		self.output = output.Outputer()

	def spider(self,root_url,path):
		if root_url is None:
			return
		#self.urls.addURL(url)
		content = self.download.downloadHtml(root_url)
		new_urls = self.parser.parseFirstHtml(root_url, content)
		self.urls.addURLs(new_urls)
		while self.urls.existURL():		
			try:

				url = self.urls.getURL()	
				content = self.download.downloadHtml(url)
				new_urls,title,data = self.parser.parserHtml(url,content)
				self.urls.addURLs(new_urls)
				if title is not None and data is not None:
					self.output.organize_data(root_url,url,title,data,path)
			except:
				print "not found"

		self.urls.outputURL()


root_url = 'http://www.zh5000.com/ZHJD/gxjd/'
path = '.'
main_spider = Spider_zh5000()
main_spider.spider(root_url,path)
