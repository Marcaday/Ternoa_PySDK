import json
import requests


'''
POST - creates a new marketplace on blockchain.
returns :	Message (About Marketplace created with particular id).
'''
#def marketplace_create(api_url, name, commission_fee, kind, seed, uri="", logoUri="")

'''
GET -  will give the list of all registered marketplaces on blockchain
returns :	array of objects of marketplace
'''
def marketplace_all(api_url):	##not tested yet
	request = '{0}api/marketplace/all'.format(api_url)					
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)

'''
GET - searches for marketplace against specific id on blockchain and returns the data.
returns :	name, id, owner, kind, comission_fee, uri,
			logo_uri, allow_list, disallow_list
'''
def marketplace_details(api_url, id):	##not tested yet
	request = '{0}api/marketplace/details/{1}'.format(api_url, id)					
	response = requests.get(request)
	if response.status_code == 200:
		return (json.loads(response.content.decode('utf-8')))
	else:
		return (None)


'''
POST - updates the commission fee of specific marketplace on blockchain
returns :	Message (about commission fee update)
'''
#def marketplace_update_commission(api_url, mpId, commission_fee, seed):



'''
POST - updates the owner of specific marketplace on blockchain.
returns :	Message (about owner update).
'''
#def marketplace_update_owner(api_url, mpId, owner, seed):



'''
POST - updates the type (marketplace Kind) of specific marketplace on blockchain.
returns :	Message (about kind update)
'''
#def marketplace_update_type(api_url, mpId, kind, seed):


'''
POST - updates the name of specific marketplace on blockchain.
returns :	Message (about name update)
'''
#def marketplace_update_name(api_url, mpId, name, seed):



'''
POST - updates the uri of specific marketplace on blockchain.
returns :	Message (about uri update)
'''
#def marketplace_update_uri(api_url, mpId, uri, seed):




'''
POST - updates the logo uri of specific marketplace on blockchain.
returns :	Message (about logo uri update)
'''
#def marketplace_update_logoUri(api_url, mpId, logo_uri, seed):
