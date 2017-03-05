'''
Created on Mar 2, 2017

@author: Hunter
'''
from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - word tokenizers.... sentence tokenizers
# lexicon and corporas:
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their means

# investor-speak.... regular English-speak

# investor-speak 'bull' = someone who is positive about the market
# English-speak 'bull' = scary animal you dont want running at you

example_text = "Hello Mr. Smith, how are you doing today?  The weather is great and Python is awesome!  The sky is pinkish-blue.  You should not eat cardboard."

sentences = sent_tokenize(example_text)
words = word_tokenize(example_text)

for sentence in sentences:
    print(sentence)

print()

for word in words:
    print(word)