import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "data/raw/bank_reviews_processed.csv"
)

# -----------------------------
# Sentiment Distribution
# -----------------------------

plt.figure(figsize=(10,6))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title(
    "Sentiment Distribution by Bank"
)

plt.xlabel("Bank")
plt.ylabel("Review Count")

plt.savefig(
    "data/raw/sentiment_distribution.png"
)

# -----------------------------
# Rating Distribution
# -----------------------------

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title(
    "Rating Distribution by Bank"
)

plt.savefig(
    "data/raw/rating_distribution.png"
)

# -----------------------------
# Theme Frequency
# -----------------------------

theme_counts = (
    df["identified_theme"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12,6))

theme_counts.plot(kind="barh")

plt.title("Top Review Themes")

plt.savefig(
    "data/raw/theme_frequency.png"
)

print("Plots generated.")