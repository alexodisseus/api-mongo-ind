from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá menino</p>"

