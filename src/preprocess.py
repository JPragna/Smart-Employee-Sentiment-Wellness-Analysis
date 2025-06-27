import re
import spacy
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text

def lemmatize(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if token.text not in stopwords.words('english')])

def preprocess_dataframe(path):
    df = pd.read_csv(path)
    df['cleaned'] = df['response'].apply(clean_text)
    df['lemmatized'] = df['cleaned'].apply(lemmatize)
    return df
