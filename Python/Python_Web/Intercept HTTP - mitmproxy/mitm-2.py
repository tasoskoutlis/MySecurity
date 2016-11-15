'''
	Get the query string, check if it has any content and if it does add a new parameter called
	isadmin = True. Finally, update the equest query string.

	flow -- holds all info about the communication

	ex In a request http://test.com/index.php?id=1 the script will do http://test.com/index.php?id=1&isadmin=True
'''

import sys

def request(context, flow):
	#get the query string
	q = flow.request.get_query()
	if q:
		q["isadmin"] = ["True"]
		flow.request.set_query(q)
