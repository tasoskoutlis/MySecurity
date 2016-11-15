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

#You can manipulate the header values (like the user-agent)
#myHeaders = {'user-agent' : 'Iphone 6'}

#r = requests.get('https://api.github.com', auth=('user', 'pass'), params=payload)
r = requests.get('http://httpbin.org/redirect-to', params = payload)
#r = requests.get('http://httpbin.org/ip')
#r = requests.get('http://httpbin.org/headers', headers=myHeaders)

print r.url
print 'Status Code: ' + str(r.status_code) + '\n'
print '********************************************************'

'''
print 'Server Headers'
for header in r.headers:
    print '\t' + header + ' : ' + r.headers[header]
print '********************************************************\n'
'''

print 'Content:'
print r.text

print 'History'
for history in r.history:
    print str(history.status_code) + ' : ' + history.url
print '********************************************************\n'
