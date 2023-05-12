from flask import Flask, jsonify

app = Flask(__name__)

data = [

]

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})
