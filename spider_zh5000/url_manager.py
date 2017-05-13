#!/usr/bin/python
# coding:utf-8

class UrlManager(object):
	"""docstring for UrlManager"""
	def __init__(self):
		super(UrlManager, self).__init__()
		self.new_urls = set()
		self.old_urls = set()

	def addURL(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def addURLs(self,urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.addURL(url)

	def existURL(self):
		return len(self.new_urls)

	def getURL(self):
		url = self.new_urls.pop()
		self.old_urls.add(url)
		return url

	def outputURL(self):
		try:
			fd = open('accessed_urls','w+')
			for url in old_urls:
				fd.write(str(url))
			fd.close()
		except IOError as e:
			if hasattr(e,'errno'):
				print e.errno

