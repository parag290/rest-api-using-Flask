"""
To run this program :
$ python3 get_request.py

"""

from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name' : 'Java'}, {'name': 'Python'}, {'name': 'C++'}]

@app.route('/')
def hello_world():
    return 'Welcome to Rest API Sample Code'


@app.route('/lang', methods=['GET'])
def return_all():
    return jsonify({'Languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnone(name):
    langs = [i for i in languages if i['name'] == name]
    return jsonify({'Languages' : langs[0]})


if __name__ == '__main__':
    app.run(debug = True, port = 8080) #run app at port 8080 in debug mode