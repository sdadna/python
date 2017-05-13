#!/usr/bin/python
# coding:utf-8

import urllib2

class downloader(object):
	"""docstring for downloader"""
	def __init__(self):
		super(downloader, self).__init__()
		
	def downloadHTML(self, url):
		if url is None:
			return None
		try:
			user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
			headers = { 'User-Agent' : user_agent }	
			request = urllib2.Request(url,headers=headers)
			response = urllib2.urlopen(request)
			if response.getcode() != 200:
			return None
		except urllib2.HTTPError,e:
			print e.code
		except urllib2.URLError,e:
			print e.reason

		

		return response.read()
		#.encode('utf-8')
		
