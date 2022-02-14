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

# 認証情報を設定
auth=tweepy.OAuthHandler(AK, AKS)
auth.set_access_token(AT, ATS)
