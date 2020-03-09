# aviasales/app.py
from flask import Flask, request, jsonify
from datetime import datetime
from itertools import groupby

# Init app
app = Flask(__name__)
words = {}


@app.route('/load', methods=['POST'])
def load():
    print(request.get_json(force=True))
    for k, g in groupby(request.get_json(force=True), key=lambda x: ''.join(sorted(x))):
        words.setdefault(k, []).extend(g)
    return 'Data uploaded'


@app.route('/get', methods=['GET'])
def anagrams():
    word = request.args.get('word')
    if word:
        sorted_input = ''.join(sorted(word))
        try:
            return str(words[f'{sorted_input}'])
        except KeyError:
            return 'There are no anagrams for this word'
    else:
        return 'Input word in request'


@app.route('/clean', methods=['GET'])
def clean():
    words.clear()
    return 'You can upload new words'


# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
