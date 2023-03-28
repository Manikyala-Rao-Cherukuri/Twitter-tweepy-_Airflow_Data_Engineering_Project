# pip install tweepy
# reference: https://www.youtube.com/watch?v=q8q3OFFfY6c
import tweepy # this library used to connect with twitter API
import s3fs # this library used to read and store the data to/from s3 bucket
import pandas as pd
import json
from datetime import datetime


# using above code creating one cpmmon function
def run_twitter_etl:
    # twitter API access keys
    access_key = "API Key"
    access_secret = "API Key Secret"
    consumer_key = "Access Token"
    consumer_secret = "Access Token Secret"
    
    # Twitter authentication to access the data
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)
    
    # Creating an API object
    api = tweepy.API(auth)
    
    # fetching data of a particular Twitter account
    tweets = api.user_timeline(screen_name='@elonmusk',
                               count=200, # 200 is the maximum allowed count
                               include_rts = False, # re-tweet is keeping as false
                               tweet_mode = 'extended')
    
    # reading and storing the data in list format from tweets
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text': text,
                         'favorite_count' : tweet.favorite_count,
                         'retweet_count' : tweet.retweet_count,
                         'created_at' : tweet.created_at
                        }
        tweet_list.append(refined_tweet)
    
    # Creating a DataFrame using above list
    df = pd.DataFrame(tweet_list)
    
    # storing this data into local driver as csv file
    df.to_csv("s3://airflow-twitter-bucket/elonmusk_twitter_data.csv")
