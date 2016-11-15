'''
    Using requests library we can make head requests
    We could also set the headers to trick the server
'''
#!/usr/bin/env python
import requests

r = requests.head('http://httpbin.org/ip')

print r.url
print 'Status Code: *' + str(r.status_code) + '\n'
print '********************************************************'

print 'Server Headers'
for header in r.headers:
    print '\t' + header + ' : ' + r.headers[header]
print '********************************************************\n'

#we wont get the content because it is a head request
print 'Content:'
print r.text
