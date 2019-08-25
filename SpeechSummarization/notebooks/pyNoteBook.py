# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'notebooks'))
	print(os.getcwd())
except:
	pass

#%%
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
 
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
 
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer


#%%
LANGUAGE = "english"
SENTENCES_COUNT = 10
 
 
    
#url="https://en.wikipedia.org/wiki/Deep_learning"
#parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

# or for plain text files
parser = PlaintextParser.from_file("../src/Email.txt", Tokenizer(LANGUAGE))



print ("--LsaSummarizer--")    
summarizer = LsaSummarizer()
summarizer = LsaSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)

print ("--LuhnSummarizer--")     
summarizer = LuhnSummarizer() 
summarizer = LsaSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words = ("I", "am", "the", "you", "are", "me", "is", "than", "that", "this",)
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)

print ("--EdmundsonSummarizer--")     
summarizer = EdmundsonSummarizer() 
words = ("deep", "learning", "neural" )
summarizer.bonus_words = words

words = ("another", "and", "some", "next",)
summarizer.stigma_words = words


words = ("another", "and", "some", "next",)
summarizer.null_words = words
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence) 

#%% [markdown]
# # By Model

#%%
import skipthoughts

# You would need to download pre-trained models first
model = skipthoughts.load_model()

encoder = skipthoughts.Encoder(model)
encoded =  encoder.encode(sentences)


#%%



