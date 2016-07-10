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

sentence = "oh by the way, have you heard Justin Biebers new album. i heard its really good"

spotifySentence = "have you heard Justin Biebers new album"

spotifySentence = "spotify " + spotifySentence
queryurl = "https://www.google.com/search?q=" + spotifySentence
if queryurl[-1] == '+':
    queryurl = queryurl[:-1]
print queryurl
r = requests.get(queryurl)
soup = BeautifulSoup(r.text, 'html.parser')
openSpotifyLinkFound = 0
numh3 = 0
while openSpotifyLinkFound ==0:
    h3 = str(soup('h3')[numh3])
    before = 'href="/url?q=https://open.spotify.com'
    index = h3.find(before)
    if index != -1:
        spotifyurl = "https://open.spotify.com" + h3[index + len(before):].split('&amp')[0]
        print spotifyurl
        openSpotifyLinkFound = 1
    numh3 = numh3+1



