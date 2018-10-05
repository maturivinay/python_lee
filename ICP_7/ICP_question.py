import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk, ngrams

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
ps = PorterStemmer() # used as a variable to call Porterstemmmer
lemmatizer = WordNetLemmatizer() # used as a variable to call lemmatizer of word

my_list = []  # used to store the links
para =[] # used to store the line which are further stored in txt file
my_link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# our link which we want to print
link = requests.get(my_link)
# requesting the link

# to clear the previous data
f = open("input.txt", "w")
f.write("")
f.close()
obj = BeautifulSoup(link.content, "html.parser")
# print the title of the webpage
print(obj.title)

my_list.append(obj.find_all('a'))
# collecting data/links on to list

# goes through each  'a' to get the reference
for i in obj.find_all('a'):
    #print(i.get('href'))
    f = open("input.txt", "a")
    para = str(i.get('href'))
    f.write(para.replace("/wiki/"," "))
    f.write("\n")
    f.close()

# reading the values from the txt file and reading as a line
f = open("input.txt", "r",encoding="utf-8")
fileread = f.read()


senttokens = sent_tokenize(fileread) # sentence tokenizing
wordtokens = word_tokenize(fileread) # word tokenizing

# sentence tokenized printing
print("sentence  tokenized :")
print(senttokens)

# word tokenized printing
print("word tokenized :")
print(wordtokens)

#stemming of data
print("stemming:")
stemm =[]
for w in wordtokens:
    stemm.append(ps.stem(w))

print(stemm)


#Parts of speech
print("POS:")

def process_content():
    try:
        for i in senttokens[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()

# lemmatizing the data
print("lemmatizing:")

lem=[]
for w in wordtokens:
    lem.append(lemmatizer.lemmatize(w))

print(lem)

#trigram the data
print("trigram")
print("")
sent = " i am studying in umkc which is a good university"
text = word_tokenize(sent)
trigram = ngrams(text,5)
for t in trigram:
    print(t)


#Named Entity Recognition of text
print("Named Entity Recognition:")

NER=[]
NER.append(ne_chunk(pos_tag(fileread)))
print(NER)