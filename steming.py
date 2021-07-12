import nltk
 

from nltk.tokenize import sent_tokenize, word_tokenize,PunktSentenceTokenizer

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
 
 #******************************Filtering Stop Words***********************************************************
stop_words_eng = set(stopwords.words("english"))
stop_words_ar = set(stopwords.words("arabic"))

filter_english_text = []
for word in english_text:
    if word.casefold() not in stop_words_eng:
        filter_english_text.append(word)

# Arabic Text using List Comprehension
filter_arabic_text = [
    word for word in arabic_text if word not in stop_words_ar
]

filter_arabic_text

#************************************stemming  English Text****************************************

stem = PorterStemmer()
english_words_stem = [stem.stem(word) for word in filter_english_text]
english_words_stem
