import re
import unicodedata
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))

def remove_punctuation_safe(x):
    if isinstance(x, str):
        return "".join(ch for ch in x if not unicodedata.category(ch).startswith("P"))
    return x

def remove_urls(x):
    if isinstance(x, str):
        return re.sub(r"http\S+|www\S+|https\S+", "", x)
    return x

def remove_stopwords_nltk(x):
    if isinstance(x, str):
        tokens = word_tokenize(x.lower())
        filtered = [word for word in tokens if word.isalpha() and word not in stop_words]
        return " ".join(filtered)
    return x

def to_lowercase(x):
    if isinstance(x, str):
        return x.lower()
    return x
