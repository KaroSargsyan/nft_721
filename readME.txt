
scripts/upload_to_pinata.py

brownie run scripts/deploy_simple.py --network rinkeby
brownie run scripts/create_collectible.py --network rinkeby
brownie run scripts/create_metadata.py --network rinkeby
brownie run scripts/set_tokenuri.py --network rinkeby



{"description":"DAW is an NFT collection of 10,000 Desperate ApeWives. Each Desperate ApeWife is unique and algorithmically generated from 221 traits. All ApeWives are hot but some are supermodels. Your Desperate ApeWife is also your exclusive DAW membership card. Ownership and commercial usage rights are given to you, the owner, over your NFT.","image":"ipfs://QmfNcU57Jg88Xr38P6x8jvL7g8nwiK21fft9izmmvjRUMW/1.png","name":"Desperate ApeWife #1","attributes":[{"trait_type":"NAME","value":"Stay Strong"},{"trait_type":"BACKGROUND","value":"Macaroon"},{"trait_type":"FUR","value":"Bubble gum"},{"trait_type":"EYES","value":"Staring"},{"trait_type":"CLOTHING","value":"Stay Strong T-shirt "},{"trait_type":"HAIR","value":"Pink Bandana"},{"trait_type":"MOUTH","value":"Desperate Pink"}]}