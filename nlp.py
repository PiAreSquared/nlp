import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import words

stopwords = set(stopwords.words("english"))
stemmer = PorterStemmer()

pos = set(words.positiveWords())
neg = set(words.negativeWords())

#test = """Today is such a wonderful day. The weather is great and birds are singing. I wish the weather was this amazing everyday."""
#test = """Today is a terrible day. The weather is terrible and its very stormy. I hate rainy days."""
test = str(input("Enter a string: "))


test_filtered = []
test_stemmed = []
test_adjectives = []

positive = 0
negative = 0

for word in word_tokenize(test.lower().replace(".", "").replace("!", "").replace("?", "")):
    if word not in stopwords:
        test_filtered.append(word)


for word in test_filtered:
    test_stemmed.append(stemmer.stem(word))


for tup in nltk.pos_tag(test_filtered):
    if tup[1] == "JJ" or "VB" in tup[1]:
        test_adjectives.append(tup[0])

print("Keywords:")
for word in set(test_adjectives):
    print(word)
    if word in pos:
        positive += 1
    if word in neg:
        negative += 1

print("\n")

if positive > negative:
    print("Positive Tone")
elif positive < negative:
    print("Negative Tone")
else:
    print("Neutral???")
    print()
    print(positive, negative)