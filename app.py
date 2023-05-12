'''
Flask Application
'''
from flask import Flask, jsonify

app = Flask(__name__)

data = [

]

'''
Test Function
'''


@app.route('/')
def hello_world():
    '''
    Returns a JSON message
    '''
    return jsonify({"message": "Hello, World!"})
