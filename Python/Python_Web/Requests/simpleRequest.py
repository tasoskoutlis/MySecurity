'''
    Using requests library we can make get/post requests

    You can add auth to provide authentication credentials
                parameters to provide the url parameters

    r.url
    r.headers
    r.text
    r.status_code
'''
#!/usr/bin/env python
import requests

#add parameters to the requests
payload = {'url':'http://www.edge-security.com'}

#r = requests.get('https://api.github.com', auth=('user', 'pass'), params=payload)
r = requests.get('http://httpbin.org/redirect-to', params = payload)

print r.url
print 'Status Code: *' + str(r.status_code) + '\n'
