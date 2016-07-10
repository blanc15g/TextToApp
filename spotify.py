import json
import nltk
import string

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import sys
import subprocess
from bs4 import BeautifulSoup
import requests
#import urllib.request

import resource

rsrc = resource.RLIMIT_DATA
soft, hard = resource.getrlimit(rsrc)
resource.setrlimit(rsrc, (1024*1024*500, hard))

keep = set(['CD', 'NN', 'NNP', 'NNPS', 'NNS'])
keywords = ['spotify', 'song', 'album']
WINDOW_SIZE = 8

# # sentence= 'have you heard justin biebers new album'
# sentence = "can you play call me maybe i love that song"
#
#
#
#
# text = sentence.split()  # word_tokenize(sentence)
# parts = pos_tag(text)
# # print(parts)
# text = list(map(lambda x: x[0].upper() + x[1:], text))
# parts = pos_tag(text)

sentence = "have you heard Justin Biebers new album"
parts = pos_tag(sentence.split(" "))
print parts
propernouns = [word for word,pos in parts if pos == 'NNP']
print propernouns

#celebrities or popular songs usually have wikipedia articles
queryurl = "https://www.google.com/search?q=wikipedia+"
for word in propernouns:
    queryurl = queryurl + word + '+' #"%20"
    
if queryurl[-1] == '+':
    queryurl = queryurl[:-1]
print queryurl
r = requests.get(queryurl)
soup = BeautifulSoup(r.text, 'html.parser')
h3 = str(soup('h3')[0])
print(h3.__repr__)
before = 'href="/url?q='
index = h3.find(before)
url = h3[index + len(before):].split('&amp')[0]
print url
newrequest  = requests.get(url)
newsoup = BeautifulSoup(newrequest.text, 'html.parser')
name =  str(newsoup.title.string)
print name
name = name.split(' -')[0]
print name
namearray = name.split(" ");
print namearray
spotifyurl = "https://api.spotify.com/v1/search?query="
for word in namearray:
    spotifyurl = spotifyurl + word + '+' #"%20"
spotifyurl = spotifyurl + "&type=track"
print spotifyurl

spotifyrequest = requests.get(spotifyurl)
spotifysoup = BeautifulSoup(spotifyrequest.text)
#print spotifysoup
spotifystr = str(spotifysoup)
print spotifystr
before = 'https://open.spotify.com/track/'
index = spotifystr.find(before)
print index
trackurl = spotifystr[index + len(before):].split('"')[0]
trackurl = 'https://open.spotify.com/track/' + trackurl
print trackurl
#for the above sentence, we get https://open.spotify.com/track/3eze1OsZ1rqeXkKStNfTmi







