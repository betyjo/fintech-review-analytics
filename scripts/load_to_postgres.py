import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "postgresql://postgres:123456789@localhost:5432/bank_reviews"
)

df = pd.read_csv(
    "data/raw/bank_reviews_processed.csv"
)

# Banks table
banks = pd.DataFrame({
    "bank_name": ["CBE", "BOA", "Dashen"],
    "app_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ]
})

banks.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

df["bank_id"] = df["bank"].map(bank_mapping)

reviews = df[
    [
        "review_id",
        "bank_id",
        "review",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
]

reviews.columns = [
    "review_id",
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]

reviews.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully.")