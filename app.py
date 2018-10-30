
from flask import Flask, request, render_template, redirect, config
from fb import setup
import os
from storage import Database
from capture import path_to_save


app = Flask(__name__)

app.secret_key = "raspberry pi iot system"
db = Database()
db.create_table()
firebase,credentials = setup()

@app.route('/')
def index():
    db = Database()
    dataset = db.view()
    if not dataset:
        dataset =[]
    return render_template('index.html',files=dataset)

@app.route('/upload',methods=['POST','GET'])
def upload():
    print("uploading")


if __name__ == '__main__':
    app.run(debug=True)