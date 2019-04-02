from flask import Flask, request
from controllers import Word_splitter as ws, range_controller as rc
from flask.json import jsonify

app = Flask(__name__)

@app.route('/split/<word>',)
def split(word):
    return jsonify(ws.word_splitter(word))

@app.route('/range',methods=['POST'])
def ranges():
    json = request.get_json()
    return jsonify(rc.ranges(int(json['start']),int(json['end'])))


if __name__ == '__main__':
    app.run(port='1001',depug=True)
