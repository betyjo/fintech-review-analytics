from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for r in result:
        all_reviews.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

# Remove duplicates
df.drop_duplicates(subset=["review"], inplace=True)

# Remove missing
df.dropna(subset=["review", "rating"], inplace=True)

# Save
df.to_csv("data/raw/bank_reviews_clean.csv", index=False)

print(df.head())
print(df.shape)