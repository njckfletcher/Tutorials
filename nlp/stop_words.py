'''
Created on Mar 3, 2017

@author: Hunter
'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = [w for w in words if w not in stop_words]

print(filtered_sentence)