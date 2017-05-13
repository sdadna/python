#!/usr/bin/python
# coding:utf-8
import urllib2,traceback

class Downloader(object):
	"""docstring for Downloader"""
	def __init__(self):
		super(Downloader, self).__init__()
	
	def downloadHtml(self,url):
		if url is None:
			return
		try:
			user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
			headers = { 'User-Agent' : user_agent }	
			request = urllib2.Request(url,headers=headers)
			response = urllib2.urlopen(request)
			if response.getcode() != 200:
				return 

			return response.read()
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print "reason:",e.reason
			elif hasattr(e,'code'):
				print "code:",e.code
			#traceback.print_exc()

		
