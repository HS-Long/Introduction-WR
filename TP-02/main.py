from src.load_data import load_csv
from src.text_cleaning import (
    remove_punctuation_safe,
    remove_urls,
    remove_stopwords_nltk,
    to_lowercase
)
from src.tokenization import tokenize_text, stem_tokens
import pandas as pd

# Load dataset
df = load_csv("data/elon_musk.csv")

# Ensure expected column
if "Text" not in df.columns:
    raise KeyError("Expected 'Text' column not found!")

# Cleaning pipeline
df["Text_no_punct"] = df["Text"].apply(remove_punctuation_safe)
df["Text_no_urls"] = df["Text_no_punct"].apply(remove_urls)
df["Text_no_stopwords"] = df["Text_no_urls"].apply(remove_stopwords_nltk)
df["Text_lower"] = df["Text_no_urls"].apply(to_lowercase)
df["Text_tokens"] = df["Text_lower"].apply(tokenize_text)
df["Text_stemmed"] = df["Text_tokens"].apply(stem_tokens)

# Save cleaned data
df.to_csv("output/cleaned_preview.csv", index=False)
print("Text preprocessing completed and saved to output/cleaned_preview.csv")
