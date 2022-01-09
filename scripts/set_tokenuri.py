from brownie import Phantom, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT

metadata_dict = {"1": "https://ipfs.io/ipfs/QmYuZUeQWnUCnJgVoUjo1LfYRF17nnrSWqJXAZDM5vhL5J?filename=jsonname1.json"}


def main():
    
    print("Working on " + network.show_active())
    phantom_collectible = Phantom[len(Phantom) - 1]
    number_of_phantom_collectibles = phantom_collectible.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_phantom_collectibles))
    for token_id in range(number_of_phantom_collectibles):
        if not phantom_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, phantom_collectible,metadata_dict["0"])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print("You can view your NFT at {}".format(OPENSEA_FORMAT.format(nft_contract.address, token_id)))


