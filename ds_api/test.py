import json

test = json.load(open(r'resources/tweets_messi.json'))
json = json.loads(test)
print(json)