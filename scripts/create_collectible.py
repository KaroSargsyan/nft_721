from brownie import Phantom, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT
import json


metadatas=json.load(open("meta.json"))

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    phantom_collectible = Phantom[len(Phantom) - 1]
    token_id = phantom_collectible.tokenCounter()
    token_uri=metadatas[str(token_id)]
    transaction = phantom_collectible.createCollectible(token_uri, {"from": dev})
    transaction.wait(1)
    print("Awesome! You can view your NFT at {}".format(OPENSEA_FORMAT.format(phantom_collectible.address, token_id)))
    