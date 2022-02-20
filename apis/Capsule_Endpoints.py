import json
import requests


def capsule_nftId(api_url, nftId):
	request = '{0}api/capsule/items/{1}'.format(api_url, nftId)
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)


def capsule_metadata(api_url, nftId):
	request = '{0}api/capsule/metadata/{1}'.format(api_url, nftId)
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)