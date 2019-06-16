import random
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stopwords = set(stopwords.words("english"))
stemmer = PorterStemmer()
questions_list = ["when", "who", "what", "where", "when", "why", "how", "can", "did", "will"]
yes = ["sure", "of course", "definitely", "yes"]
no = ["sorry", "nope", "no"]
compliments = ["great job", "keep it up", "great work", "nice job", "doing great"]

test = str(input("Enter a string: ")).lower()

test_filtered = []
test_stemmed = []
test_adjectives = []
test_verbs = ""
personal_pronoun = ""
mod_aux = ""
adverb = ""
additions = ""
finalstatement = ""
determiner = ""
negative = ""
question = ""
returns = []

if "you" in test.lower():
    test = test.replace("you", "I")

pos_tags = nltk.pos_tag(word_tokenize(test.replace(".", "").replace("!", "").replace("?", "").replace("please", "")))

if pos_tags[0][0] in questions_list:
    question = pos_tags[0][0]

for tup in pos_tags:
    if not "JJ" in tup[1] and "please" not in tup[0]:
        test_filtered.append(tup[0])
        
for i in range(len(nltk.pos_tag(test_filtered))):
    tup = pos_tags[i]
    if "that" in tup[0]:
        tup = ("that", "DT")
    if "did" in tup[0]:
        tup = ("did", "MD")
    if not "n't" in tup[0]:
        if "VB" in tup[1]:
            if tup[0] == "going":
                test_verbs += tup[0] + " to "
            else:
                test_verbs += tup[0] + " "
        if "PRP" in tup[1] and not personal_pronoun:
            personal_pronoun = tup[0]
        elif "NN" in tup[1] and not personal_pronoun:
            personal_pronoun = tup[0]
        if "MD" in tup[1]:
            mod_aux = tup[0]
        if "RB" == tup[1]:
            adverb += tup[0] + " "
        if "DT" == tup[1] and personal_pronoun:
            determiner = tup[0]
            if determiner=="the":
                determiner = "it"
        elif "DT" == tup[1]:
            personal_pronoun = tup[0]
        if "why" in tup[0]:
            additions = "because"
    else:
        if "n't" in tup[0] or "not" in tup[0]:
            negative = "not"
    
negative = "not"
if "it" in test and not determiner and personal_pronoun != "it":
    determiner = "it"

finalstatement = ".."
for i in range(2):
    if question == "did" or question == "will" or question == "can":
        if negative:
            begining = no[random.randint(0, len(no)-1)]
            if "can" in question:
                mod_aux += negative
                negative = ""
        else:
            begining = yes[random.randint(0, len(yes)-1)]
            if "will" in question:
                mod_aux = "will"
            if "can" in question:
                mod_aux = "can"
            if "did" in question:
                temp = ""
                lookout = True
                for i in test_verbs.split():
                    if lookout:
                        if i[-1] == "e":
                            temp += i + "d "
                        else:
                            temp += i + "ed "
                        lookout = False
                    else:
                        temp += i + " "
                test_verbs = temp
                adverb = ""
                mod_aux = ""
        return_sentance = begining + ", " + personal_pronoun + " " + mod_aux + " " + negative + " " + test_verbs[:-1] + " " + determiner + " " + adverb[:-1] + " " + additions + " " + finalstatement
        return_sentance = return_sentance[0].upper() + return_sentance[1:] + "."
        while '  ' in return_sentance:
            return_sentance = return_sentance.replace('  ', ' ')
        returns.append(return_sentance)
        negative = ""
        mod_aux = ""
    elif question == "what":
        returns.append("I haven't learned this yet :(")

if returns == []:
    negative = ""
    return_sentance = personal_pronoun + " " + mod_aux + " " + negative + " " + test_verbs[:-1] + " " + determiner + " " + adverb[:-1] + " " + additions + " " + finalstatement
    return_sentance = return_sentance[0].upper() + return_sentance[1:] + "."
    while '  ' in return_sentance:
        return_sentance = return_sentance.replace('  ', ' ')
    returns.append(return_sentance)

for compliment in compliments:
    if compliment in test:
        returns = ["Thank you!!!"]

for sentance in returns:
    print(sentance)
