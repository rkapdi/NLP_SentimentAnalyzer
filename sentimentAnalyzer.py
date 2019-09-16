'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                SENTIMENT ANALYZER
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Sentiment Analysis: The process of understanding and extracting feelings from data.

The program uses NLP algorithm from TextBlob along with Twitter API: Tweepy to analyse tweets and provide a sentiment score on a particular key word.
The key word can be any topic, for example in this program Sentiment Analysis is done on Trump.

~~~~~~~~~~~Jargon~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Polarity: measures how positive or negative a text is.
Subjectivity: measures how opionated a text is vs factual.

```````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
Author: Rissalat A. Kapdi
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
```````````````````````````````````````````````````````````````````````````

Learning material used: https://www.youtube.com/watch?v=o_OZdbCzHUA&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=2
'''

import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#aunthentication variable
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#calling the set_access_token method on auth
auth.set_access_token(access_token, access_token_secret)

#api variable opens a door to a wide gamut of functionality in the tweepy library, for example Create, Delete and Find tweets.
api = tweepy.API(auth)

#from the tweepy API we will be used in this method.
#The variable will store a list of tweets.
#To fill the list created in public_tweets, we will use the search method from the API
public_tweets = api.search('Trump')


for tweet in public_tweets:
    print(tweet.text)#we will print out all the list elements(tweets)
    analysis = TextBlob(tweet.text)#The Sentiment Analysis takes plac here. Analysis variable will store our analysis and call TextBlob with tweet as a string as the argument.
    print(analysis.sentiment)#we can print out the sentiment attribute of the analysis variable
