import os
from dotenv import load_dotenv, find_dotenv
import dotenv
import sys
# print(os.environ['IPFS_URL'])

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

args = (sys.argv)



def func(ar):
    return ar

nv = func(args)
print(nv[1])

print(sys.path)


# .env set a variable----------------------------------------------

# load_dotenv()

# print(os.environ['IPFS_URL'])
# dotenv_path = '../nft_demo/.env'

# dotenv.set_key(dotenv_path, 'AAAAAAAAAAAA', '888888')




#-----------.env copy-----------------------------------------

# ### remove the '#' to use the environment variables
# export PRIVATE_KEY=b78330805132f471817bc7db07168d1d26c8c162c0e96dfdf4a8b2016082101f
# export WEB3_INFURA_PROJECT_ID=5b27c96566b243a292579c7c8967c62f


# ### Optional - don't uncomment if you don't know what they do!
#  export ETHERSCAN_TOKEN=QBPG4NSN42M33J8HG3KCWBK35CM1DW1MGK
# export IPFS_URL=http://127.0.0.1:5001
# export UPLOAD_IPFS=true

# export PINATA_API_KEY=8f5d65dd726665c6461b
# export PINATA_API_SECRET=8b3003d5ff4e7e188121d56f999dbecffa1c6621a7e4381e186398d3eb2ce625

# #export PRIVATE_KEY=8b42f7d608ce70b802454e3a2d0baa104a05f2b315a30d162f36b6f0a96f6929