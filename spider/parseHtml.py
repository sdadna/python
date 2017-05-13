#!/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import re,urlparse

class parseHtml(object):
	"""docstring for parseHtml"""
	def __init__(self):
		super(parseHtml, self).__init__()
		

	def _getNewURLs(self,page_url,soup):
		new_urls = set()
		#http://baike.baidu.com/item/GPL
		#/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6
		links = soup.find_all('a',href=re.compile(r'/item/[\w\/\%]+'))

		for link in links:
			newURL = link['href']
			newFullURL = urlparse.urljoin(page_url,newURL)
			new_urls.add(newFullURL)
			
		return new_urls

	def _getNewData(self,page_url,soup):
		#lemmaWgt-lemmaTitle-title
		res_data = {}
		res_data['url'] = page_url
		title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
		if len(title_node) == 0:
			res_data['title'] = ""
		else:
			res_data['title'] = title_node.get_text()
		#<div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div',class_='lemma-summary')
		if summary_node is  None:
			res_data['summary'] = ""
		else:
			res_data['summary'] = summary_node.get_text()
		return res_data
		

	def parse(self,page_url,content):
		if page_url is None or len(content) == 0:
			return None
		soup = BeautifulSoup(content,"html.parser",from_encoding="utf-8")
		new_urls = self._getNewURLs(page_url,soup)
		new_data = self._getNewData(page_url,soup)
		return new_urls,new_data

