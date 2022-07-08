import numpy as np
import pandas as pd

import nltk
import re
import string 

nltk.download("stopwords")   
from nltk.corpus import stopwords  

from bs4 import BeautifulSoup

#Removal of HTML Contents
def remove_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

#Removal of Punctuation Marks
def remove_punctuations(text):
    return re.sub('\[[^]]*\]', '', text)

# Removal of Special Characters
def remove_characters(text):
    return re.sub("[^a-zA-Z]"," ",text)

#Removal of stopwords 
def remove_stopwords_and_lemmatization(text):
    final_text = []
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    for word in text:
        if word not in set(stopwords.words('english')):
            lemma = nltk.WordNetLemmatizer()
            word = lemma.lemmatize(word) 
            final_text.append(word)
    return " ".join(final_text)

#Total function
def cleaning(text):
    try:
        text = remove_html(text)
        text = remove_punctuations(text)
        text = remove_characters(text)
        text = remove_stopwords_and_lemmatization(text)
    except:
        text = None
    return text