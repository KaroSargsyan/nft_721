
brownie run scripts/deploy_phantom.py --network rinkeby
brownie run scripts/create_collectible.py --network rinkeby
brownie run scripts/create_metadata.py --network rinkeby
brownie run scripts/set_tokenuri.py --network rinkeby


Request is sent from Postman to local server http://127.0.0.1:5000/mint

The data sample posted is:

{"name": "SampleName",
    "description": "Some Data Sample",
    "image": "https://media.istockphoto.com/photos/non-fungible-token-picture-id1307372676",
    "attributes": [{"trait_type": "cuteness", "value": "100"}]
}

Th data is dsaved in a temporary file called 'received_data.py'.

Now the task is to push the data to DB and get it from there.

The programm receives the data, creates metadata, uploads it to Pinata and returnes the URI. 



