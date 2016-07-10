from bs4 import BeautifulSoup
import requests
import sys
import json

#from BeautifulSoup import BeautifulSoup


url = "https://www.google.com/search?q=cost+uber+googleplex"

def compute(url):
	# Computation
	r  = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	print soup.title
	print soup.title.string
	#print soup.first('p').string
	print soup('h3')[1].extract()
	mystr = str(soup('h3')[1].extract())
	print mystr.split("url?q=")
	#print soup('h3')[0]['class']
	print "hi"

	return soup.title.string

compute(url)