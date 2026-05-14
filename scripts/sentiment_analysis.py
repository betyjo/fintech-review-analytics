import pandas as pd
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
import re

nltk.download('stopwords')

from nltk.corpus import stopwords

# Load data
df = pd.read_csv("data/raw/bank_reviews_clean.csv")

# -----------------------------
# Text Cleaning
# -----------------------------

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)

df["clean_review"] = df["review"].apply(clean_text)

# -----------------------------
# Sentiment Analysis
# -----------------------------

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentiments = []

for text in df["clean_review"]:
    try:
        result = classifier(text[:512])[0]

        label = result["label"]
        score = result["score"]

        if label == "POSITIVE":
            sentiment = "positive"
        else:
            sentiment = "negative"

        sentiments.append((sentiment, score))

    except:
        sentiments.append(("neutral", 0.5))

df["sentiment_label"] = [s[0] for s in sentiments]
df["sentiment_score"] = [s[1] for s in sentiments]

# -----------------------------
# TF-IDF Theme Extraction
# -----------------------------

vectorizer = TfidfVectorizer(
    max_features=1000,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(df["clean_review"])

# Cluster reviews into themes
kmeans = KMeans(
    n_clusters=5,
    random_state=42
)

df["theme_cluster"] = kmeans.fit_predict(X)

terms = vectorizer.get_feature_names_out()

theme_names = {}

for i in range(5):
    center_terms = kmeans.cluster_centers_[i].argsort()[-10:]
    keywords = [terms[idx] for idx in center_terms]
    theme_names[i] = ", ".join(keywords[:5])

df["identified_theme"] = df["theme_cluster"].map(theme_names)

# -----------------------------
# Save Processed File
# -----------------------------

df.reset_index(inplace=True)
df.rename(columns={"index": "review_id"}, inplace=True)

final_df = df[
    [
        "review_id",
        "review",
        "rating",
        "date",
        "bank",
        "source",
        "sentiment_label",
        "sentiment_score",
        "identified_theme"
    ]
]

final_df.to_csv(
    "data/raw/bank_reviews_processed.csv",
    index=False
)

print(final_df.head())
print(final_df["sentiment_label"].value_counts())