from Services import Twitter as tw
import json
import datetime
from flask import jsonify
import os
x = datetime.datetime.now()
class TweetController(object):
    def __init__(self):
        self.twitterSerivices = tw.TwitterClient(json.load(open('resources/twitter.json')))


    def get_tweets_and_save(self,keyword):
        tweets = self.twitterSerivices.get_all_tweets(keyword)
        path = r'resources/tweets_{}.json'.format(keyword)
        file = open(path, 'w')
        json.dump(json.dumps([tweet._json for tweet in tweets]),file)
        return os.path.abspath(path)

    def tweets_sentiment(self,file_path):
        json_string = json.load(open(file_path))
        tweets_json = json.loads(json_string)
        for tweet in tweets_json:
            sentiment = self.twitterSerivices.get_tweet_sentiment(tweet['text'])
            tweet['sentiment'] = sentiment

        return tweets_json





















