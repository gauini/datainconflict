import urllib2
topic = raw_input("search for : ")
search = '"{}"'.format(topic)
search = "+".join(search.split(" "))

page = urllib2.urlopen("http://search.folha.uol.com.br/search?q="+search+"&site=online%2Fpaineldoleitor&sd=&ed=")
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page)
from pprint import pprint

import json

def getHeadline(string):
	idx =  string.find("html\">Folha")
	# print idx
	substring = string[idx + 35: -23]
	if substring.find('<b>') != -1:
		idxB = substring.find('<b>')
		substring = substring[:idxB] + substring[idxB+3:]
	if substring.find('</b>') != -1:
		idxB = substring.find('</b>')
		substring = substring[:idxB] + substring[idxB+4:]
	return substring


def getLink(string):
	idxA =  string.find("href")
	idxB =  string.find(".shtml")
	# print idx
	substring = string[idxA + 6: + idxB +6]
	return substring

data = dict()


for index, x in enumerate(soup.findAll('h3')):
	if index < 3:
	# print str(x)
		h3TagAsString = str(x)
		for y in x:
			h3TagAsStringLink = str(y)
	# print y
	# print type(y)
		headline = getHeadline(h3TagAsString);
			#print "HEADLINE"
		print headline
		link = getLink(h3TagAsStringLink);
	#print "LINK"
		print link
	#print ""

		headline_link_list = list()
		headline_link_list.append(headline)
		headline_link_list.append(link)
		#data[index:headline,link]
		data[index] = headline_link_list

with open('folhaSearch.json', 'w') as outfile:
    json.dump(data, outfile)

#pprint(data)
		# print y.find()
		#print data[index]
		# print x
		# print x.index('strong')
		# for link in x:
		# 	print link
		# 	print link.find("<strong")
			# print(link.get('href'))
			# print noticia
			# print ""
article = int(raw_input("article to access : "))

artigo = data[article]


linkArticle = '"{}"'.format(artigo.pop())

print linkArticle
