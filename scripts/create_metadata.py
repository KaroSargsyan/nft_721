import os
import requests
import json
from brownie import SimpleCollectible, network
from metadata import sample_metadata
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
metadatas={}


def main():
    print("Working on " + network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    number_of_simple_collectibles = simple_collectible.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_simple_collectibles))
    write_metadata(number_of_simple_collectibles, simple_collectible)

def write_metadata(token_ids, nft_contract):        
    for id in range(1,4):
        collectible_metadata = sample_metadata.metadata_template
        metadata_file_name = f"./metadata/rinkeby/jsonname{id}.json"
        if Path(metadata_file_name).exists():
            print("{} already found, delete it to overwrite!".format(metadata_file_name))
        else:
            print("Creating Metadata file: " + metadata_file_name)
            collectible_metadata["name"] = "NFT_!!!"
            collectible_metadata["description"] = "!!!"
        
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(id)
                image_to_upload = upload_to_ipfs(image_path,id)
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                
                
                upload_to_ipfs(metadata_file_name,id)
            


def upload_to_ipfs(filepath,id):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = (
            os.getenv("IPFS_URL")
            if os.getenv("IPFS_URL")
            else "http://localhost:5001"
        )
        response = requests.post(ipfs_url + "/api/v0/add",
                                 files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
        # print(image_uri)
        if image_uri.endswith('json'):
            metadatas[id]=f"{image_uri}"
            with open("meta.json",'w') as file:
                json.dump(metadatas,file)
    return image_uri

