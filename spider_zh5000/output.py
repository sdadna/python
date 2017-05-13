#!/usr/bin/python
# coding:utf-8
import os
from urlparse import urlparse
import re

class Outputer(object):
	"""docstring for Outputer"""
	def __init__(self):
		super(Outputer, self).__init__()
	
	def _generateFilePath(self, url, name, path):
		if url is None or name is None or path is None:
			return 

		split_url = urlparse(url)
		file_dir = re.match(r'/(.*)/.*?.htm',split_url.path)
		file_full_dir = path + '/' + file_dir.group(1) 
		
		try:
			if os.path.isdir(file_full_dir) == False:
				os.makedirs(file_full_dir,0775)
		except OSError as err: 
			print err.errno

		full_path = file_full_dir + '/' + name.strip()

		return full_path

	def organize_data(self,root_url, url, name, data, path):
		if url is None or name is None or data is None or path is None:
			return

		full_path = self._generateFilePath(url,name,path)

		if full_path is not None and os.path.isfile(full_path) == False:
			try:		
				print full_path

				fd = open(full_path,'w')

				fd.write("url:%s\n" %url.encode('utf-8')) #gb18030
				full_data = re.sub(r'[ ]*?\n+[ ]+',"\n ",data.encode('utf-8'))
				fd.write(full_data)
			except IOError as err:
				print err.errno,err.filename
				#print "error"
			finally:
				fd.close()

