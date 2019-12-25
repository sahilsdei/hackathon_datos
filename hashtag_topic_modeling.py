from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk.corpus import stopwords
from gensim.summarization.summarizer import summarize

import nltk
stop_words = set(stopwords.words('english'))

new_arr=[]
new_arr_text=[]

def clean_text(words):
    if words:
        words = words.replace('\t', ' ')
        words = words.replace(',', ' ')
        words = words.replace(':', ' ')
        words = words.replace(';', ' ')
        words = words.replace('=', ' ')
        words = words.replace('\x08', '\\b')  # \b is being treated as backspace
        words = words.replace('_', ' ')
        words = words.replace('(', ' ')
        words = words.replace(')', ' ')
        words = words.replace('-', ' ')
        words = words.replace('`', ' ')
        words = words.replace('\'', ' ')
        words = words.replace('/', ' ')
        words = words.replace('_', ' ')
        words = words.replace('"', ' ')
        words = words.replace("'", ' ')
        words = words.replace(">", ' ')
        words = words.replace("<", ' ')
        words = words.replace("<", ' ')
        words = words.replace("%", ' ')
        words = words.replace("$", ' ')
        words = words.replace("|", ' ')
        words = words.replace("@", ' ')
        words = words.replace("~", ' ')
        words = words.replace("’", ' ')
        words = words.replace(":", ' ')
        words = words.replace(".", ' ')
        words = words.replace(". ", ' ')
        words = words.replace(" . ", ' ')
        words = words.replace("“", ' ')
        words = words.replace("”", ' ')
        return words.strip()
    return words

def get_hashtag (arr):
    for text in arr:
        text = clean_text(text)
        word_tokens = nltk.word_tokenize(text)
        for w in word_tokens:
            if not w.lower() in stop_words:
                new_arr.append(w)
        new_arr_text.append(" ".join(new_arr))

    texts = [line.split() for line in new_arr_text]

    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    ldamodel = LdaModel(corpus=corpus, num_topics=5, id2word=dictionary)
    return ldamodel.show_topics()

def get_summary(arr):
    return summarize(' '.join(arr),word_count=40)