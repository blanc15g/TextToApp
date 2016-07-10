import json
import nltk

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import sys
import subprocess


# # sentence= 'i want to look up five guys on yelp, oh my phone can'
# sentence = "oh going to san diego. i wonder what the weather is like"
#
#
# keep = set(['CD', 'NN', 'NNP', 'NNPS', 'NNS'])
#
#
# text = sentence.split()  # word_tokenize(sentence)
# parts = pos_tag(text)
# # print(parts)
# text = list(map(lambda x: x[0].upper() + x[1:], text))
# parts = pos_tag(text)

def stripExceptNouns(sentence):
    upper = list(map(lambda x: x[0].upper() + x[1:], sentence.split()))
    parts = pos_tag(upper)
    kept = []
    for part in parts:
        if part[1] in keep:
            kept.append(part)
    return kept
    
sampleFile = open('samplequery.txt','r')
for sample in sampleFile:
    print(stripExceptNouns(sample))


# print()
# print(stripExceptNouns(sentence))
