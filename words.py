import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stopwords = set(stopwords.words("english"))
stemmer = PorterStemmer()

files_pos = os.listdir('aclImdb/train/pos')
files_pos = [open('aclImdb/train/pos/'+f, 'r').read() for f in files_pos if int(f.split("_")[1].split(".")[0]) > 9]
files_neg = os.listdir('aclImdb/train/neg')
files_neg = [open('aclImdb/train/neg/'+f, 'r').read() for f in files_neg if int(f.split("_")[1].split(".")[0]) < 2]

def positiveWords():
    data_adjectives = []

    for data in files_pos[:500]:
        data_filtered = []


        for word in word_tokenize(data.lower().replace(".", "").replace("!", "").replace("?", "")):
            if word not in stopwords:
                data_filtered.append(word)

        for tup in nltk.pos_tag(data_filtered):
            if tup[1] == "JJ":
                data_adjectives.append(tup[0])
    return (set(data_adjectives))

def negativeWords():
    data_adjectives = []

    for data in files_neg[:500]:
        data_filtered = []

        for word in word_tokenize(data.lower().replace(".", "").replace("!", "").replace("?", "")):
            if word not in stopwords:
                data_filtered.append(word)

        for tup in nltk.pos_tag(data_filtered):
            if tup[1] == "JJ":
                data_adjectives.append(tup[0])
    return (set(data_adjectives))