import urllib2
page = urllib2.urlopen("http://www1.folha.uol.com.br/poder/2016/05/1767117-governo-libera-verba-orcamentaria-a-deputados-e-senadores.shtml")
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page)
from pprint import pprint
import json


def getBody(string):
	idxA =  string.find('<p>')
	idxB =  string.find('</p>')
	# print idx
	substring = string[idxA +3 : idxB ]
	return substring


data = dict()

numberOfArticles = 0
for index, x in enumerate(soup.findAll('p')):
	numberOfArticles += 1

count = 0
for index, x in enumerate(soup.findAll('p')):
	if count == numberOfArticles - 3:
		break
	count += 1

	#print x
	pBodyText = str(x)
	body = getBody(pBodyText);
	#print body

	body_paragraph_list = list()
	body_paragraph_list.append(body)



	data[index] = body_paragraph_list
	print body
	#print index
#pprint(data)
with open('folhaArticle.json', 'w') as outfile:
    json.dump(data, outfile)