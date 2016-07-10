from bs4 import BeautifulSoup
import requests
import sys
import json

from BeautifulSoup import BeautifulSoup

nltk_data_path = "nltk_data.txt"

nltk_data = []
nltk_file = open(nltk_data_path, "r")
for line in nltk_file:
    try:
        word = json.loads(line)
        nltk_data.append(word['text'])
    except:
        continue
queryurl = "https://www.google.com/#q="
for word in nltk_data:
	queryurl = queryurl + word + "%20"

url = queryurl

def compute(url):
	# Computation
	r  = requests.get(url)
	soup = BeautifulSoup(r.text)
	print soup.title
	print soup.title.string

	return soup.title.string