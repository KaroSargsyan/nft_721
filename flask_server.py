from ast import dump
from datetime import time
from flask import Flask, redirect, url_for,render_template, request
import os
from time import sleep
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

#Connect to DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metadata/nft_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 

class Received_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String())
    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/')
def home():
    return "Hello World"

@app.route('/mint', methods = ['POST'])
def mint():
    
    task_content = request.get_json()
    task_content_string = json.dumps(task_content)
    print(task_content_string)
    new_task = Received_data(content=task_content_string)

    try:
        db.session.add(new_task)
        db.session.commit()
        print('db is done')

    except:
        print('Error')
    

    os.system(f'brownie run scripts/create_metadata.py --network rinkeby')

    os.system('brownie run scripts/create_collectible.py --network rinkeby')

    

    with open(f"./metadata/meta.json", 'r') as f:
        data = json.load(f)

    return data

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


