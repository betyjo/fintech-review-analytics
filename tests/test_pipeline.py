import pandas as pd

def test_dataset_exists():
    df = pd.read_csv(
        "data/raw/bank_reviews_processed.csv"
    )

    assert len(df) >= 1000

def test_required_columns():
    df = pd.read_csv(
        "data/raw/bank_reviews_processed.csv"
    )

    required = [
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

    for col in required:
        assert col in df.columns

def test_missing_values():
    df = pd.read_csv(
        "data/raw/bank_reviews_processed.csv"
    )

    assert df["review"].isnull().sum() == 0