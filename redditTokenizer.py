#Setup Tokenizers and Stopwords
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
#import matplotlib.pyplot as plt
import math

example = "This is an example sentence!  However, it " \
            "is a very informative one,"

print(word_tokenize(example, language='english'))