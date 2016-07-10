import json
import nltk
import string

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import sys
import subprocess
from bs4 import BeautifulSoup
import requests
import urllib.request

import resource

rsrc = resource.RLIMIT_DATA
soft, hard = resource.getrlimit(rsrc)
resource.setrlimit(rsrc, (1024*1024*500, hard))

keep = set(['CD', 'NN', 'NNP', 'NNPS', 'NNS'])
keywords = ['yelp']
WINDOW_SIZE = 8

# # sentence= 'i want to look up five guys on yelp, oh my phone can'
# sentence = "oh going to san diego. i wonder what the weather is like"
#
#
#
#
# text = sentence.split()  # word_tokenize(sentence)
# parts = pos_tag(text)
# # print(parts)
# text = list(map(lambda x: x[0].upper() + x[1:], text))
# parts = pos_tag(text)

def stripPunct(sentence):
    exclude = set(string.punctuation) | set(['-',"’"])
    # print(exclude)
    return ''.join(ch for ch in sentence if ch not in exclude)

def stripExceptNouns(sentence):
    sentence = stripPunct(sentence)
    upper = list(map(lambda x: x[0].upper() + x[1:], sentence.split()))
    parts = pos_tag(upper)
    # print(parts)
    kept = []
    for part in parts:
        if part[1]  in keep:
            kept.append(part[0])
    return kept


def getGoogleWords(words):
    queryurl = "https://www.google.com/search?q="
    for word in words:
        queryurl = queryurl + word + '+' #"%20"
    if queryurl[-1] == '+':
        queryurl = queryurl[:-1]
    r = requests.get(queryurl)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        h3 = str(soup('h3')[0])
        # print(h3.__repr__)
        # raise Exception
        before = 'href="/url?q='
        index = h3.find(before)
        url = h3[index + len(before):].split('&amp')[0]
        # print(h3)
        # print(queryurl)
        # print(url)
        return compute(url)
    except:
        h3 = str(soup('h3')[1])
        # print(h3.__repr__)
        # raise Exception
        before = 'href="/url?q='
        index = h3.find(before)
        url = h3[index + len(before):].split('&amp')[0]
        # print(h3)
        # print(queryurl)
        # print(url)
        return compute(url)


def compute(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    # print soup.title.string
    return soup.title.string

def findOverlap(nouns, title):
    a = stripPunct(nouns.lower()).split()
    b = stripPunct(title.lower()).split()
    answer = []
    for word in a:
        if word in b:
            answer.append(word)
    # print('HERE   ',a,b,lcs(a,b))
    return answer
    # return lcs(a,b)

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = [a[x-1]] + result
            x -= 1
            y -= 1
    return result

def getWords(line):
    line = line.replace('eat', 'yelp')
    # print(line)
    words = line.split(' ')
    indexOfKeyword = -1
    for i in reversed(range(len(words))):
        for word in keywords:
            if words[i] == word:
                indexOfKeyword = i
                break
    if indexOfKeyword == -1:
        return ""
    keyword = words[indexOfKeyword]
    first = max(0, indexOfKeyword - WINDOW_SIZE)
    last = min(len(words), indexOfKeyword + WINDOW_SIZE)
    # print(indexOfKeyword, keyword, words[first:last])
    stripped = stripExceptNouns(' '.join(words[first:last]))
    if keyword not in stripped:
        stripped.append(keyword)
    # print(sample)
    # print(stripped)
    g = getGoogleWords(stripped)
    # print(g)
    words = findOverlap(' '.join(stripped),g)
    while keyword in words:
        words.remove(keyword)
    return getUrl(words, keyword)
    # if keyword == 'yelp':
    #     return 'http://www.yelp.com/search?find_desc=' + '+'.join(words)

    # return findOverlap(' '.join(stripped),g)
    # print(sample, stripExceptNouns(sample))

def getUrl(words, keyword):
    if keyword == 'yelp':
        return 'http://www.yelp.com/search?find_desc=' + '+'.join(words)




print(getWords('adding extra words to scrape boo yah i wonder what yelp says about mcdonalds with a lot of extra words'))
print(getWords('I kinda want to eat at five guys today'))

