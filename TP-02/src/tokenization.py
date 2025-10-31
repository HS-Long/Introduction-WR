from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import nltk

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)
try:
    nltk.download("averaged_perceptron_tagger_eng", quiet=True)
except:
    nltk.download("averaged_perceptron_tagger", quiet=True)

stemmer = SnowballStemmer("english")

def tokenize_text(x):
    if isinstance(x, str):
        return word_tokenize(x)
    return []

def stem_tokens(tokens):
    if isinstance(tokens, list):
        return [stemmer.stem(t) for t in tokens]
    return []
