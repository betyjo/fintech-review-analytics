# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Applications

## Business Objective

This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store to identify customer satisfaction drivers, pain points, and feature requests.

Banks analyzed:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Technologies Used

- Python
- Pandas
- Transformers (DistilBERT)
- Scikit-learn
- PostgreSQL
- Matplotlib
- Seaborn
- Google Play Scraper

## Methodology

1. Scraped Google Play reviews using google-play-scraper
2. Cleaned and normalized review data
3. Applied DistilBERT sentiment analysis
4. Extracted themes using TF-IDF and KMeans clustering
5. Stored processed data in PostgreSQL
6. Visualized insights for business recommendations

## Key Insights

### Commercial Bank of Ethiopia (CBE)

Strengths:

- Strong transfer reliability
- Positive UI feedback

Pain Points:

- Slow loading times
- OTP delays

Recommendations:

- Improve backend transaction performance
- Optimize login and authentication systems

### Bank of Abyssinia (BOA)

Strengths:

- Easy navigation
- Fast registration

Pain Points:

- App crashes
- Login failures

Recommendations:

- Improve app stability
- Add biometric login support

### Dashen Bank

Strengths:

- Modern design
- Fast transfers

Pain Points:

- Network timeout issues
- Transaction delays

Recommendations:

- Improve API reliability
- Enhance customer support automation

## Ethics and Bias Considerations

Potential biases include:

- Negativity bias:
  users are more likely to leave reviews after bad experiences.

- Sampling bias:
  reviews may not represent the full customer base.

- Language bias:
  English-language reviews may exclude some local users.

## Setup

```bash
pip install -r requirements.txt
python scripts/scrape_reviews.py
python scripts/sentiment_analysis.py
python scripts/visualize.py
```

---

# 36. Final Git Workflow

```bash id="m3w8qk"
git add .
git commit -m "feat: complete analytics pipeline and business insights"
git push
```
