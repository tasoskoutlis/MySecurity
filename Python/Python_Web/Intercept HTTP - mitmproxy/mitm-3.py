'''
	Error based SQLi with mitmproxy

	For every url that has a parameter we replace each parameter value with FUZZ,
	while conserving the rest of the parameters values

	ex In a request http://test.com/index.php?id=1&area=2
	 				the script will do http://test.com/index.php?id=FUZZ&area=2
					the script will do http://test.com/index.php?id=1&area=FUZZ
'''

import urlparse
from copy import deepcopy
import requests
import sys

def injector (url):
	errors = ['Mysql','error in your SQL']
	injections = ['\'','\"',';--']
	f = open('sqlinjection_results.txt','a+')
	a = urlparse.urlparse(url)
	query = a.query.split('&')
	qlen = len(query)
	while qlen != 0:
		querys = deepcopy(query)
		querys[qlen-1] = querys[qlen-1].split('=')[0] + '=FUZZ'
		newq='&'.join(querys)
		url_to_test = a.scheme+'://'+a.netloc+a.path+'?'+newq
		qlen-=1
		for inj in injections:
	                req=requests.get(url_to_test.replace('FUZZ',inj))
			print req.content
		        for err in errors:
              	        	if req.content.find(err) != -1:
                                        res = req.url + ";" + err
	                                f.write(res)
	f.close()

def request(context, flow):
	#Only if it is a query string
	q = flow.request.get_query()
	print q
	if q:
		injector(flow.request.url)
		flow.request.set_query(q)
