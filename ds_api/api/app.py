from flask import Flask, request
from controllers import Word_splitter as ws, range_controller as rc
from controllers import tweet_controller as tc
from flask.json import jsonify
import json
app = Flask(__name__)

@app.route('/split/<word>',)
def split(word):
    return jsonify(ws.word_splitter(word))

@app.route('/range',methods=['POST'])
def ranges():
    json = request.get_json()
    return jsonify(rc.ranges(int(json['start']),int(json['end'])))



@app.route('/get_tweets/<keyword>')
def get_tweets(keyword):
    twc = tc.TweetController()
    path = twc.get_tweets_and_save(keyword)
    json = jsonify(path)
    return path


@app.route('/analyze',methods=['POST'])
def analyze_tweets():
    path = request.values.get('path')
    twc = tc.TweetController()
    result = twc.tweets_sentiment(path)
    return jsonify(result)

@app.route('/analyze_source',methods=['POST'])
def tweet_analysis_source():
    path = request.values.get('path')
    twc = tc.TweetController()
    result = twc.tweets_analysis(path)
    return jsonify(result)



if __name__ == '__main__':
    app.run(port='1001',depug=True)
