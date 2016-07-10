from bs4 import BeautifulSoup
import requests
import sys

#imput url = first website after google searching nltk query output

url = "http://www.yelp.com/biz/five-guys-burgers-and-fries-alexandria-5"
def compute(url):
	# Computation
	r  = requests.get(url)
	soup = BeautifulSoup(r.text)
	print soup.title
	print soup.title.string

	return soup.title.string