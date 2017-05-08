#!/usr/bin/python
# coding:utf-8

class urlManager(object):
	"""docstring for urlManager"""
	def __init__(self):
		super(urlManager, self).__init__()
		self.newURLs = set()		
		self.oldURLs = set()

	def addNewURL(self, url):
		if url is None:
			return
		if url not in self.newURLs and url not in self.oldURLs:
			self.newURLs.add(url)

	def addNewURLs(self,urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.addNewURL(url)

	def getNewURL(self):
		url = self.newURLs.pop()
		self.oldURLs.add(url)
		return url

	def existNewURL(self):
		return len(self.newURLs)
		