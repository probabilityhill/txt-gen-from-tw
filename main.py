import os
from dotenv import load_dotenv
import tweepy
import csv

CSV_PATH = ""

# .envを読み込む
load_dotenv()

# 環境変数を取得
# AK = os.getenv("API_KEY")
# AKS = os.getenv("API_KEY_SECRET")
# AT = os.getenv("ACCESS_TOKEN")
# ATS = os.getenv("ACCESS_TOKEN_SECRET")
BT = os.getenv("BEARER_TOKEN")

# Authentication（Twitter API v2）
# OAuth 2.0 Bearer Token (App-Only)
client = tweepy.Client(BT)

# OAuth 1.0a User Context
# client = tweepy.Client(consumer_key=AK, consumer_secret=AKS, access_token=AT, access_token_secret=ATS)

# Tweet "succeeded"
# client.create_tweet(text="succeeded")

USER_ID = "77907829"
tweet_data = []
tweets = client.get_users_tweets(USER_ID, max_results=5)
for tweet in tweets.data:
    tweet_data.append(tweet.text)

print("\n------------------\n".join(tweet_data))

with open(CSV_PATH, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(tweet_data)

"""
for page in range(1):
    tweets = client.get_users_tweets(user_id, max_results=3, pagination_token=page)
    for tweet in tweets:
        # print('----------')
        # print(tweet.text)
        tweet_data.append([tweet.text])
"""
