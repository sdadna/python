#!/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import urlparse
import re

class MatchRule(object):
	"""docstring for MatchRule"""
	def __init__(self):
		super(MatchRule, self).__init__()
		

		
class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		super(Parser, self).__init__()	
		self.names = set()

	def _getNewUrls(self, url, soup):
		new_urls = set()
		if url is None:
			return
		#<a href="http://www.zh5000.com/ZHJD/gxjd/gxjd-jb.htm#zhouyi" target="_blank">周易</a>
	# 	catelogues = soup.find_all('div',class_=re.compile(r'gr[B,D]'))
	# #	catelogue = catelogue_soup.find('h2')
	# 	#links = catelogue_soup.find('a',href=re.compile(r'http://www.zh5000.com/ZHJD/gxjd/[\w\.\#]+?'))
		
	# 	for catelogue in catelogues:
	# 		catelog = re.search(r'<h2><.*?>(.*?)<.*?></h2>',str(catelogue))
	# 		if catelog:
	# 			self.catelogue.append(catelog.group(1))
		links = soup.find_all('a',href=re.compile(r"http://www.zh5000.com/ZHJD/gxjd/[-#\.\w]+?"))
		for link in links:
			newURL = link['href']
			name = link.get_text()
			self.names.add(name)
			new_urls.add(newURL)
			#print newURL,name
		return new_urls

	def _getNewTitleUrls(self, url, soup):
		new_urls = set()
		if url is None:
			return None
		#<a href="2006/jb/ssj/gxjd-0002.htm">周易--上经</a>
		links = soup.find_all('a',href=re.compile(r"2006/[-#\.\/\w]+?"))
		for link in links:
			newURL = link['href']
			name = link.get_text()
			new_full_url = urlparse.urljoin(url,newURL)
			new_urls.add(new_full_url)

		return new_urls

	def _getTitle(self, url, soup):
		#<div align="center" class="title">周易--上经</div>
		if url is None:
			return None

		title = soup.find('div',align="center", class_="title")
		if title  is not None:
			return title.get_text()
		return None

	def _getData(self, url, soup):
		#<td id="ArticleBody" valign="top"> 
		if url is None:
			return None

		data = soup.find('td',id="ArticleBody",valign="top")
		if data  is not None:
			#print data.get_text()
			return data.get_text()
		return None

	def parserHtml(self, url, content):
		if url is None or len(content) == 0:
			return

		soup = BeautifulSoup(content, "html.parser",from_encoding="gb18030")
		new_urls = self._getNewTitleUrls(url, soup)
		new_title = self._getTitle(url, soup)
		new_data = self._getData(url, soup)

		return new_urls,new_title,new_data

	def parseFirstHtml(self, url, content):
		if url is None or len(content) == 0:
			return

		soup = BeautifulSoup(content,"html.parser",from_encoding="gb18030")
		new_urls = self._getNewUrls(url, soup)
		return new_urls