import os
from dotenv import load_dotenv

import json
from requests_oauthlib import OAuth1Session

import pandas as pd
import tweepy

# .envを読み込む
load_dotenv()
# 環境変数を取得
AK = os.getenv("API_KEY")
AKS = os.getenv("API_KEY_SECRET")
AT = os.getenv("ACCESS_TOKEN")
ATS = os.getenv("ACCESS_TOKEN_SECRET")

# APIインスタンスの作成
client = tweepy.Client(consumer_key=AK, consumer_secret=AKS, access_token=AT, access_token_secret=ATS)

client.create_tweet(text="succeeded")

"""
# アカウント指定（@の後ろ）
Account = "hirasawa"

tweet_data = []  # ツイートの保存
num = 0  # 取得するツイートを計算

for page in range(1):
    tweets = client.search_recent_tweets(query="", Account, exclude="retweets", max_results=3, pagination_token=page)
    for tweet in tweets:
        # print('----------')
        # print(tweet.text)
        num += 1
        tweet_data.append([tweet.text])

print(num, 'ツイート表示しました。')

# ツイートデータをデータフレームに変換
tweet_data = pd.DataFrame(tweet_data)
tweet_data
"""

"""
# 適当なツイートデータを抜き出す
tweet_data.iloc[7]
print(tweet_data.iloc[7].date)
print(tweet_data.iloc[7].tweet)
"""
