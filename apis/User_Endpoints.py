import json
import requests


'''
GET - Generate the unique Mnemonics and address.
returns :	Mnemonic, public address for the newly generated mnemonic
'''
def user_generate_mnemonic(api_url):										
	request = '{0}api/user/generate-mnemonic'.format(api_url)					
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)



'''
GET - To transfer balance while making sure the minimum balance to keep the accout active on blockchain is left in wallet
returns :	success or erorr message for balance transfer
'''

###	Not working still need to find how to pass multiple args in a request (im watching tutorials lolz)
def user_balance_transfer_keep_alive(api_url, recieverAddress, value):
	request = '{0}api/user/balances/transfer-keep-alive/{1}{2}'.format(api_url, recieverAddress, value)					
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)