import os
import requests
import json
from brownie import Phantom, network
from metadata import sample_metadata
from pathlib import Path
from dotenv import load_dotenv
from .upload_to_pinata import uploadToPinata
import sys
import getopt

args = (sys.argv)
print(args)

load_dotenv()
metadatas={}
id = 'phantom'

def incrementId(a):
    global id
    id = a



# args = (sys.argv)
# received_data = args[5]
# str = received_data.replace("\'", "\"")
# data = json.loads(str)
# print('Staaaaaaaaaaaaaaaaaaaaaaaaaaaart')
# print(data['image'])
# print('Endddddddddddddddddddddddddddddddd')



def main():

    print(id)
    print("Working on " + network.show_active())
    phantom_collectible = Phantom[len(Phantom) - 1]
    number_of_phantom_collectibles = phantom_collectible.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_phantom_collectibles))
    #increment id
    # incrementId(number_of_phantom_collectibles + 1)
    write_metadata(number_of_phantom_collectibles)
    


def write_metadata(number_of_phantom_collectibles):        
    with open("received_data.json", 'r') as f:
        data = json.load(f)
        print(data["description"])

        print(data)

        #image from URL
        f = open(f'./img/{id}.png','wb')
        response = requests.get(data["image"])
        f.write(response.content)
        f.close()
        #image from URL end


        collectible_metadata = sample_metadata.metadata_template
        metadata_file_name = f"./metadata/rinkeby/json_{id}.json"
        # if Path(metadata_file_name).exists():
        #     print("{} already found, delete it to overwrite!".format(metadata_file_name))
        # else:
            
        print("Creating Metadata file: " + metadata_file_name)
        collectible_metadata["name"] = data["name"]
        collectible_metadata["description"] = data["description"]
        collectible_metadata["attributes"] =  data["attributes"]
    
        image_to_upload = None
        if os.getenv("UPLOAD_IPFS") == "true":
            image_path = "./img/{}.png".format(id)
            image_to_upload = upload_to_ipfs(image_path,id, number_of_phantom_collectibles )
        collectible_metadata["image"] = image_to_upload
        with open(metadata_file_name, "w") as file:
            json.dump(collectible_metadata, file)
        if os.getenv("UPLOAD_IPFS") == "true":
            upload_to_ipfs(metadata_file_name,id, number_of_phantom_collectibles )
            


def upload_to_ipfs(filepath,id, token_number):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = (
            os.getenv("IPFS_URL")
            if os.getenv("IPFS_URL")
            else "http://localhost:5001"
        )

        #Here should be Pinata code
         #1. It should take the picture and send it to Pinata server
          #2. Response should be returned and be put to IPFS link

        pinata_hash = uploadToPinata(filepath)
        print(pinata_hash)

        #end

        # response = requests.post(ipfs_url + "/api/v0/add",
        #                          files={"file": image_binary})
        # ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]

        image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(pinata_hash, filename)
        # print(image_uri)

        if image_uri.endswith('json'):
            metadatas[token_number]=f"{image_uri}"
            with open("meta.json",'w') as file:
                json.dump(metadatas,file)
    return image_uri