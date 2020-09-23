# open txt file and load its text
text_file = open("juventus_rumors.txt",encoding="utf-8")
text = text_file.read()
print("Original text:\n",text)
print("Text length:\n",len(text))

import nltk
#if package:punkt is missing add next line...
#nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize

#sentences tokenizing
sentences = sent_tokenize(text)
print("Sentences count:\n",len(sentences))
print("Sentences:\n",sentences)

# words tokenizing
words = word_tokenize(text)
print("Words count:\n",len(words))
print("Words:\n",words)

# remove punctuation marks and stopwards
from nltk.corpus import stopwords
#if package:punkt is missing add next line...
#nltk.download('stopwords')
stopwords_list = stopwords.words("english")
words_freq = []
for single_word in words:
    if(single_word.isalpha()):
        if(single_word not in stopwords_list):
            words_freq.append(single_word.lower())

# frequency calculate
from nltk.probability import FreqDist
freq = FreqDist(words_freq)
print("Top frequent words:\n",freq.most_common(20))

#frequency plot graph
import matplotlib.pyplot as plt
freq.plot(20)