from datetime import time
from flask import Flask, redirect, url_for,render_template, request
app = Flask(__name__)
# from nft_demo.scripts import create_collectible
import os
from time import sleep
import json
import glob


# // 172.18.0.3   
# // root
# // example
# // sudo docker ps

# create_collectible.main()

@app.route('/')
def home():
    
    return "Hello World"

@app.route('/mint', methods = ['POST'])
def mint():
    content = request.get_json()
    
    with open("received_data.json",'w') as file:
        json.dump(content,file)
    
     

    os.system(f'brownie run scripts/create_metadata.py --network rinkeby')
    # sleep(5)
    os.system('brownie run scripts/create_collectible.py --network rinkeby')

    #choose file and return the content

    list_of_files = glob.glob('metadata/rinkeby/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    with open(f"{latest_file}", 'rb') as f:
        data = json.load(f)
        print(data)

    return data

if __name__ == "__main__":
    app.run(debug=True)


