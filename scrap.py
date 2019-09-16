# Importing libraries and dependencies

import tweepy
import csv
import pandas as pd

# twitter API access credentials

#Consumer API keys
consumer_key = '' #(API key)
consumer_secret = '' #(API secret key)

# Access token & access token secret
access_token = '' #(Access token)
access_secret = '' #(Access token secret)
# Read and write (Access level)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

###UNITED AIRLINES###

#Open/Create a file to append data
csvFile = open('ua.csv','a')

#use a csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="#unitedAIRLINES", count=100, lang="en", since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
