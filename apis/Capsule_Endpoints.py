import json
import requests



'''
POST - Encrypt a file with generated PGP key and upload to IPFS.
returns :	url, ipfs, mediaType, size, publicPgpHash
'''
#def capsule_media_encrypt_item(api_url, file, nftId)



'''
POST - takes a file and nftId of a capsule, encrypts the file with the pgp public key of that NFT then uploads the encrypted file to IPFS. After that, the a new offchain metadata is generated with existing files of capsule along with new file, and blockchain is update with the new IPFS hash of the offchain metadata for capsule.
returns :	ipfsHash
'''
#def capsule_media_add(api_url, nftId, title, seed)



'''
POST - akes NftId of the capsule and IPFS hash of the capsule item which is to be deleted, if that item exists on capsule offchain metadata, it is removed and as a result, a new capsule offchain metadata on ipfs is generated which is then updated on BlockChain.
returns :	ipfsBaseUrl, ipfsHash, mediaType, size
'''
#def capsule_media_remove(api_url, file_ipfs, nftId, seed)



'''
POST - Creates a capsule from existing nft.
returns :	nftId
'''
#def capsule_convert_from_nft(api_url, ipfs, nftId, seed)



'''
POST - Converts Capsule back to nft.
returns :	nftId
'''
#def capsule_convert_from_nft(api_url, nftId, seed)



'''
POST - Creates a Capsule on blockchain.
returns :	nftId
'''
#def capsule_create(api_url, nft_ipfs, capsule_ipfs, seed, series_id="")



'''
GET - gets the list of all encrypted files in the capsule
returns :	Json array of encrypted items
'''
def capsule_nftId(api_url, nftId):
	request = '{0}api/capsule/items/{1}'.format(api_url, nftId)
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)



'''
POST -	Uploads the an array of "capsuleCryptedMedias" on IPFS.
		check specs : https://ternoa-2.gitbook.io/sdk/api/capsule-endpoints
returns :	Ipfs Data (Url and Ipfs Hash)

'''
#def capsule_upload_json()




'''
GET -  Returns a metaData of a capsule
returns :	Owner, Ipfs_Reference
'''
def capsule_metadata(api_url, nftId):
	request = '{0}api/capsule/metadata/{1}'.format(api_url, nftId)
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)



'''
GET - sets the ipfs reference for a Capsule on blockchain
returns :	ipfsData
'''
#def capsule_set_ipfs_reference(api_url, nftId, ipfs="", seed)


