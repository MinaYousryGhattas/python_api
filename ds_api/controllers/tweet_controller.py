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


    def tweets_analysis(self,file_path):
        json_string = json.load(open(file_path))
        tweets_json = json.loads(json_string)

        tweet_analysis = dict()
        tweet_analysis['positive'] = 0
        tweet_analysis['unique_positive'] = 0
        tweet_analysis['negative'] = 0
        tweet_analysis['unique_negative'] = 0
        tweet_analysis['neutral'] = 0
        tweet_analysis['unique_neutral'] = 0



        for tweet in tweets_json:
            id = None
            if ('retweeted_status' in tweet.keys()):
                id = tweet['retweeted_status']['id_str']
            else:
                id = tweet['id_str']

            sentiment = self.twitterSerivices.get_tweet_sentiment(tweet['text'])

            if (id in tweet_analysis):
                tweet_analysis[id]['text'] = tweet['text']
                tweet_analysis[id]['sentiment'] = sentiment
                tweet_analysis[id]['counter'] += 1


            else:
                tweet_analysis[id] = {}
                tweet_analysis[id]['text'] = tweet['text']
                tweet_analysis[id]['sentiment'] = sentiment
                tweet_analysis[id]['counter'] = 1
                if (sentiment == 'positive'):
                    tweet_analysis['unique_positive'] += 1
                elif (sentiment == 'negative'):
                    tweet_analysis['unique_negative'] += 1
                else:
                    tweet_analysis['unique_neutral'] += 1

            if (sentiment == 'positive'):
                tweet_analysis['positive']+=1
            elif (sentiment == 'negative'):
                tweet_analysis['negative']+=1
            else:
                tweet_analysis['neutral']+=1


        return tweet_analysis
