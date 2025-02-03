from google_play_scraper import app, Sort, reviews
import pandas as pd
# Fetch reviews for a specific app (e.g., "com.instagram.android" for Instagram)
result, continuation_token = reviews(
    'com.nautilus.realcricket',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=100, # defaults to 100
    # filter_score_with=3 # defaults to None(means all score)
)

# Convert the reviews into a pandas DataFrame

df = pd.DataFrame(result)
df.to_csv('app_reviews.csv', index=False, encoding='utf-8-sig')
# print(df)

rating_distribution = df['score'].value_counts().sort_index()
print("Distribution of Ratings:")
print(rating_distribution)

total_upvotes = df['thumbsUpCount'].sum()
print(f"Total Number of Upvotes: {total_upvotes}")

longest_review = df.loc[df['content'].str.len().idxmax()]
print("Longest Review:")
print(longest_review['content'])

time_between_reviews = df['at'].diff().mean()
print(f"Average Time Between Reviews: {time_between_reviews}")

df['hour'] = df['at'].dt.hour
most_common_hour = df['hour'].mode()[0]
print(f"Most Common Hour for Reviews: {most_common_hour}:00")