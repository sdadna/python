#!/usr/bin/python
# coding:utf-8

class outputer(object):
	"""docstring for outputer"""
	def __init__(self):
		super(outputer, self).__init__()
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return None

		self.datas.append(data)


	def outputhtml(self, path):
		if path is None:
			return

		fd = open(path,'w')
		fd.write("<html>")
		fd.write("<head>")
		fd.write("<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\">")
		fd.write("</head>")
		fd.write("<body>")
		fd.write("<table>")
		
		for data in self.datas:
			fd.write("<tr>")
			fd.write("<td>%s</td>"% data['url'])
			fd.write("<td>%s</td>"% data['title'].encode('utf-8'))
			fd.write("<td>%s</td>"% data['summary'].encode('utf-8'))
			fd.write("</tr>")

		fd.write("</table>")
		fd.write("</body>")
		fd.write("</html>")