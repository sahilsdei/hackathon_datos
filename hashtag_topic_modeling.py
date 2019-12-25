import gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk.corpus import stopwords
import nltk
stop_words = set(stopwords.words('english'))

arr=['Several experts have given their thoughts on what threats AI poses, and unsurprisingly fake content is the current biggest danger.', 'The experts, who were speaking on Tuesday at the WSJ Pro Cybersecurity Executive Forum in New York, believe that AI-generated content is of pressing concern to our societies.', 'Camille François, chief innovation officer at social media analytics firm Graphika, says that deepfake articles pose the greatest danger.', 'We’ve already seen what human-generated “fake news” and disinformation campaigns can do, so it won’t be of much surprise to many that involving AI in that process is a leading threat.', 'François highlights that fake articles and disinformation campaigns today rely on a lot of manual work to create and spread a false message.', '“When you look at disinformation campaigns, the amount of manual labour that goes into creating fake websites and fake blogs is gigantic,” François said.', '“If you can just simply automate believable and engaging text, then it’s really flooding the internet with garbage in a very automated and scalable way. So that I’m pretty worried about.”', 'The graduates said they do not believe their work currently poses a risk to society and released it to show the world what was possible without being a company or government with huge amounts of resources.', 'Speaking on the same panel as François at the WSJ event, Celeste Fralick, chief data scientist and senior principal engineer at McAfee, recommended that companies partner with firms specialising in detecting deepfakes.', 'Among the scariest AI-related cybersecurity threats is “adversarial machine learning attacks” whereby a hacker finds and exploits a vulnerability in an AI system.', 'Fralick provides the example of an experiment by Dawn Song, a professor at the University of California, Berkeley, in which a driverless car was fooled into believing a stop sign was a 45 MPH speed limit sign just by using stickers.', 'According to Fralick, McAfee itself has performed similar experiments and discovered further vulnerabilities. In one, a 35 MPH speed limit sign was once again modified to fool a driverless car’s AI.', '“We extended the middle portion of the three, so the car didn’t recognise it as 35; it recognised it as 85,” she said.', 'Both panellists believe entire workforces need to be educated about the threats posed by AI in addition to employing strategies for countering attacks.', 'There is “a great urgency to make sure people have basic AI literacy,” François concludes.']
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

for text in arr:
    text=clean_text(text)
    word_tokens = nltk.word_tokenize(text)
    for w in word_tokens:
        if not w.lower() in stop_words:
             new_arr.append(w )
    new_arr_text.append(" ".join(new_arr))



text_data = ' '.join(arr)

bigram = gensim.models.Phrases(new_arr_text)

texts = [line.split() for line in new_arr_text]




dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel = LdaModel(corpus=corpus, num_topics=10, id2word=dictionary)


print(ldamodel.show_topics())