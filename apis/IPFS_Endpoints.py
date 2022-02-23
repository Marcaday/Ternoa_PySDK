import json
import requests

'''
POST -  Uploads a file to IPFS. Used to upload preview and encrypted secret.
returns :	url, mediaType, mediaIPFSHash, mediasize
'''
#def ipfs_upload(api_url, file)