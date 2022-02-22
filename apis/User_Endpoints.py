import json
import requests

def user_generate_mnemonic(api_url):										
	request = '{0}api/user/generate-mnemonic'.format(api_url)					
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)
