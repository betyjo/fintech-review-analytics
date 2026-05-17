import pandas as pd

df = pd.read_csv("data/raw/bank_reviews_processed.csv")

# -----------------------------------
# Average Ratings
# -----------------------------------

print("\nAverage Ratings Per Bank\n")

print(
    df.groupby("bank")["rating"]
    .mean()
    .sort_values(ascending=False)
)

# -----------------------------------
# Sentiment Distribution
# -----------------------------------

print("\nSentiment Distribution\n")

print(
    pd.crosstab(
        df["bank"],
        df["sentiment_label"]
    )
)

# -----------------------------------
# Common Themes
# -----------------------------------

print("\nTop Themes\n")

print(
    df["identified_theme"]
    .value_counts()
    .head(10)
)

# -----------------------------------
# Negative Reviews
# -----------------------------------

negative_reviews = df[
    df["sentiment_label"] == "negative"
]

print("\nMost Common Negative Themes\n")

print(
    negative_reviews["identified_theme"]
    .value_counts()
    .head(10)
)