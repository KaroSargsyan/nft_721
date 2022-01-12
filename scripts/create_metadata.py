import os
import requests
import json
from brownie import Phantom, network
from metadata import sample_metadata
from pathlib import Path
from dotenv import load_dotenv
from .upload_to_pinata import uploadToPinata
import sqlite3

conn = sqlite3.connect('../nft_demo/test.db')
c = conn.cursor()

print('**********************')
aa = c.execute('SELECT * FROM Received_data WHERE ID = (SELECT MAX(ID)  FROM Received_data)')
fetched_data = (aa.fetchall()[0][1])
print(fetched_data)



load_dotenv()
metadatas={}
id = 'phantom'



def main():

    print(fetched_data)
    print("Working on " + network.show_active())
    phantom_collectible = Phantom[len(Phantom) - 1]
    number_of_phantom_collectibles = phantom_collectible.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_phantom_collectibles))
    write_metadata(number_of_phantom_collectibles)
    

def write_metadata(number_of_phantom_collectibles):        
    # with open("received_data.json", 'r') as f:
        data = json.loads(fetched_data)
        print('--------------------------------------------------')
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