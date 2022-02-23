import json
from urllib import response
import requests


'''
POST - encrypts a file with generated PGP key and upload to IPFS
returns :	encryptedMedia (Url), encryptedMediaType, publicPgpLin, privateKeyFilePath
'''
#def nft_encrypt_and_upload():


'''
POST - Uploads Media for Nft to Ipfs
returns :	Ipfs Url, Ipfs Hash
'''
#def nft_upload_json():


'''
POST - Creates The Nft on blockchain and Save the secret shamir shards with NFT id and seed
returns :	NftId
'''
#def nft_mint():


'''
GET - Checks the Nft if it exists on the Blockchain and Burns it
returns :	NftId
'''
#def nft_burn():


'''
GET - Checks the Nfts if they exist on the Blockchain and Burns the Batch of them
returns : Array of Nfts Burned
'''
#def nft_burn_batch():


'''
POST -	Takes Required Files for Nft and creates the Nft on blockchain and saves decryption key shamirs, all the steps in one call.
		it can take any number of additional properties in request form data which will be added to NFT metadata as string, for example, power: "100"
returns :	NftId, TeeResponse
'''
def nft_create(api_url, previewFilePath, encryptFilePath, title, description, seed, seriesID="", properties=""):
	request = '{0}api/nft/create/{1}'.format(api_url, previewFilePath)
	response = requests.post(request)
	return 

'''
GET - Decrypt the Nft or Capsule Encrypted Item
returns :	Decrypted Data
'''
#def nft_decrypt():



''''
GET - searches the NFT on indexer
returns :	nft_id, owner, listed, timestampBurn, creator,
			seriesId, createdAt, nftIpfs, price, timestampList,
			currency, marketplaceId, previousOwner
'''
def nft_id(api_url, id):										
	request = '{0}api/nft/{1}'.format(api_url, id)					
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)



'''
GET - Search for all the nfts owned by a user and returns list of nft IDS from Indexer
returns :	nft_Ids (array)
'''
def nft_address(api_url, address):
	request = '{0}api/nft/owner/{1}'.format(api_url, address)
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)




'''
GET -  Search for all the nfts of a specific owner For the Same series Id
returns : nft_Ids (array)
'''
#def nft_address_seriesId():



'''
GET - Search for all the nfts in the series Id
returns :	nft_Ids (array)
'''
def nft_seriesId(api_url, seriesId):
	request = '{0}api/nft/series/{1}'.format(api_url, seriesId)
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)

'''
POST -	lists the Nft On sale on a given market place
		the series which the nft belongs to must be locked before an NFT can be listed for sale 
returns :	Message (About Nft listed for sale on particular Market Place)
'''
#def nft_list():


'''
POST -	transfer the Nft to the receiverAddress
		the series which the nft belongs to must be locked before an NFT can be transferred 
returns :	Message (About transferred Nft id
'''
#def nft_transfer():


'''
POST - Unlists the Nft from sale on a particular market place
returns :	Message (About Nft unlisted from sale on particular Market Place)
'''
#def nft_unlist():


'''
POST - Locks the particular series Id
returns :	Message (About Particular Serie is locked)
'''
#def nft_series_lock():


'''
POST - Transfers the nft to the other Account
returns :	Message (About Particular Nft is Transferred to desired account)
'''
#def nft_transfer():

