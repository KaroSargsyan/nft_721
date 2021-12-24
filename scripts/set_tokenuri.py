from brownie import SimpleCollectible, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT

dog_metadata_dic = {"0": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"}

def main():
    
    print("Working on " + network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    number_of_simple_collectibles = simple_collectible.tokenCounter()
    print("The number of tokens you've deployed is: "+ str(number_of_simple_collectibles))
    for token_id in range(number_of_simple_collectibles):
        if not simple_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, simple_collectible,dog_metadata_dic["0"])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print("You can view your NFT at {}".format(OPENSEA_FORMAT.format(nft_contract.address, token_id)))


