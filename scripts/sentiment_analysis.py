import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

nltk.download("stopwords")

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "data/raw/bank_reviews_clean.csv"
)

# -----------------------------
# Text Cleaning
# -----------------------------

stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [
        w for w in words
        if w not in stop_words
    ]

    return " ".join(words)

df["clean_review"] = df["review"].apply(clean_text)

# -----------------------------
# Sentiment Analysis
# -----------------------------

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

labels = []
scores = []

for text in df["clean_review"]:

    try:

        result = classifier(text[:512])[0]

        label = result["label"]
        score = result["score"]

        if label == "POSITIVE":
            labels.append("positive")
        else:
            labels.append("negative")

        scores.append(score)

    except:

        labels.append("neutral")
        scores.append(0.5)

df["sentiment_label"] = labels
df["sentiment_score"] = scores

# -----------------------------
# Theme Extraction
# -----------------------------

vectorizer = TfidfVectorizer(
    max_features=1000,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(
    df["clean_review"]
)

kmeans = KMeans(
    n_clusters=5,
    random_state=42
)

df["theme_cluster"] = kmeans.fit_predict(X)

terms = vectorizer.get_feature_names_out()

theme_map = {}

for i in range(5):

    center = (
        kmeans.cluster_centers_[i]
        .argsort()[-10:]
    )

    keywords = [
        terms[idx]
        for idx in center
    ]

    theme_map[i] = ", ".join(
        keywords[:5]
    )

df["identified_theme"] = (
    df["theme_cluster"]
    .map(theme_map)
)

# -----------------------------
# Save Results
# -----------------------------

df.reset_index(inplace=True)

df.rename(
    columns={"index":"review_id"},
    inplace=True
)

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

print("\nSentiment Counts:\n")

print(
    final_df["sentiment_label"]
    .value_counts()
)