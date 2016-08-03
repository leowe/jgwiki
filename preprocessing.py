import re
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize, regexp_tokenize
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict

stop_words = set(stopwords.words('german'))
#stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '=', '-', '|', ])
stop_word_pattern = re.compile(r'''([,\.\?!"'\-+\*\(\)\{\}=:;\[\]|/#]+)''')
stemmer = SnowballStemmer('german', ignore_stopwords=True)


def tokenize_stopword_removal(text, lang='english'):
    text = re.sub(stop_word_pattern, '', text)
    return [i.lower() for i in wordpunct_tokenize(text) if i.lower() not in stop_words if len(i) > 1]


def tokenize_stem(text):
    tokenized = tokenize_stopword_removal(text)
    stemmed = [stemmer.stem(word) for word in tokenized]
    return stemmed


def count_tokens(tokens):
    counter = defaultdict(int)
    for token in tokens:
        counter[token] += 1
    return counter


def max_count_token(token_counts):
    return token_counts[max(token_counts, key=token_counts.get)]

