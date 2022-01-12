
scripts/upload_to_pinata.py

brownie run scripts/deploy_simple.py --network rinkeby
brownie run scripts/create_collectible.py --network rinkeby
brownie run scripts/create_metadata.py --network rinkeby
brownie run scripts/set_tokenuri.py --network rinkeby

