import json
import requests
import os
import glob
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

def uploadToPinata(filepath):
    PINATA_BASE_URL = 'https://api.pinata.cloud/'
    endpoint = 'pinning/pinFileToIPFS'

    # filepath = "./nft_demo/img/4.png"
    filename = filepath.split('/')[-1:][0]
    headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
            'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}
    print(glob.glob("./nft_demo/img/*"))

    with open(filepath, 'r') as im:
        print(im)


    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(PINATA_BASE_URL + endpoint,
                                files={"file": (filename, image_binary)},
                                headers=headers)
        data = response.json()                       
        print(data['IpfsHash'])
        return data['IpfsHash']


