# NFT data for WOAI/Zero

This repository contains all data related to the WOAI/Zero -collection NFTs.

Each json file matches with the ID of the NFT in question. I.e.: WOAI/Zero/1 maps to 1

The contents of this directory are to be hosted at https://woai-data.woai.io/zero/ with the exception of the "generators" sub-directory.

Once all NFTs have been minted, or at least most of them, the contents of this folder will be uploaded onto an IPFS instance. Following this change, the baseURI of the WOAI/Zero smart contract will be changed to reflect the right IPFS location. Until then, the baseURI will be https://woai-data.woai.io/zero/

## Generators
The generators -directory contains a python generator for creating the relevant json files. Please note that the generator does not work for the *p* and *f* -files (pending generation and failed generation, respectively); they have been added manually.

## Collection data
Below is a list of collection-level data:

**Basics**
- Website: https://woai.io
- Author: The World of AI -project

**Collection data**
- Full name: World of AI/Zero
- Aabbreviated name: WOAI/Zero
- Alternative abbreviated name: WOAI/Z
- Token symbol: WOAI
- Description: AI generated art based on user given inputs.
- Max supply: 2500
- Mint price: 0.04 ETH

**Collection attributes**
- Ungenerated: False/True (this trait defaults to True and changes to False when the NFT owner requests their AI art generation)
- Failed: False/True (this trait defaults to False and changes to True if the art generation request was illegal (footnote 1))
- *More may be added prior to IPFS migration*

**Blockchain data**
- Network: Ethereum
- Deployer: 0xa7c7aaD22974d81EBd5B7C4B06EEA3911d33e2A9
- Contract address: TBD

**Financial data**
- Seller fee (basis points): 250
- Fee recipient: 0xa7c7aaD22974d81EBd5B7C4B06EEA3911d33e2A9

**Technology**
- NFT data & image hosting: webserver with planned migration to IPFS

#Footnotes
1. The project utilises DALL-E 2 for generating the NFT art, based on user input (up to 100 characters). If the user inputs a string that is forbidden or unavailable through DALL-E 2, the NFT will be minted using a pre-existing "failure" art and be mapped as a "Failed" NFT.