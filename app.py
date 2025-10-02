from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodburi")
db = client["stockDB"]
collection = db["items"]

#your project routing code

if __name__ == "__main__":
    app.run(debug=True)