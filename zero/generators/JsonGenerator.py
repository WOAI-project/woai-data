import json

#NOTICE: This file may need to be changed with IPFS migration

#Global definitions
##Base URI of the smart contract is "http://woai-data.woai.io/zero/" until the IPFS migration
##This will means the json files will be accessed from "http://woai-data.woai.io/zero/{tokenId}.json"
baseURI = "http://woai-data.woai.io/zero/"

def generate(floor,ceiling):
    for i in range(floor,ceiling+1):

        #The JSON data to be pushed
        #Please note that the attributes may be changed prior to IPFS push.
        data = {"image":f"{baseURI}art/{i}.png","external_url":"https://woai.io/","name":f"World of AI/Zero/{i}","seller_fee_basis_points":250,"fee_recipient":"0xa7c7aaD22974d81EBd5B7C4B06EEA3911d33e2A9","attributes":[{"trait_type":"Ungenerated","value":"False"},{"trait_type":"Failed","value":"False"}]}

        with open(f"../{i}", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    return True

if __name__ == "__main__":
    print(generate(0,2499))