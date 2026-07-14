from google_play_scraper import reviews, Sort
import pandas as pd
import json

APP_ID = "jodii.app"

result, _ = reviews(
    APP_ID,
    sort=Sort.NEWEST,
    count=500
)

mapping = {
    'at':'date',
    'userName':'user',
    'score':'rating',
    'content':'review'
}

df = pd.DataFrame(result)

cols = []

for c in mapping:
    if c in df.columns:
        cols.append(c)

df = (
    df[cols]
    .rename(columns=mapping)
)

df = df[df['review'].notna()]

df = df.drop_duplicates(
    subset=['review']
)

df.to_json(
    "reviews.json",
    orient="records",
    force_ascii=False
)
