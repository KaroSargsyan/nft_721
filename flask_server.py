from ast import dump
from datetime import time
from flask import Flask, redirect, url_for,render_template, request

# from nft_demo.scripts import create_collectible
import os
from time import sleep
import json
import glob
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# // 172.18.0.3   
# // root
# // example
# // sudo docker ps

# create_collectible.main()


app = Flask(__name__)

#Connect to DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 

class Received_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String())
    def __repr__(self):
        return '<Task %r>' % self.id

#End DB


@app.route('/')
def home():
    return "Hello World"

@app.route('/mint', methods = ['POST'])
def mint():
    # content = request.get_json()
    # with open("received_data.json",'w') as file:
    #     json.dump(content,file)

#Adddddddded
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

    data_from_db = Received_data.query.get_or_404(1)
    
#End of added

    print('start..............create_metadata')

    os.system(f'brownie run scripts/create_metadata.py --network rinkeby')

    print('start..............create_collectible')


    os.system('brownie run scripts/create_collectible.py --network rinkeby')

    #choose file and return the content

    # list_of_files = glob.glob('metadata/rinkeby/*') # * means all if need specific format then *.csv
    # latest_file = max(list_of_files, key=os.path.getctime)
    # print(latest_file)

    # with open(f"{latest_file}", 'rb') as f:
    #     data = json.load(f)
    #     print(data)

    print('Mint is dooooooooooooooooooooooooooooooone')
    return '??????/'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


