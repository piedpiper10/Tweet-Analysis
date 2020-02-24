import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
def clean_tweet (tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
	return analysis.sentiment.polarity
tweet='RT @Conor__Clery: @GameOfThrones I have never been more entertained by a movie or tv show. My jaw was on the floor for all of the spoils of war..'
n=get_tweet_sentiment(tweet)
print "The  tweet retrieved is:"
print tweet
print " The value of sentiment analysis of the tweet is",n
