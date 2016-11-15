'''
    Using requests library we can make post requests
    You will need to fill in the data variable with the credentials
'''
#!/usr/bin/env python
import requests

#add parameters to the post request
value = {'name':'packt'}

r = requests.post('http://httpbin.org/post', data=value)

print r.url
print 'Status Code: *' + str(r.status_code) + '\n'
print '********************************************************'

print 'Server Headers'
for header in r.headers:
    print '\t' + header + ' : ' + r.headers[header]
print '********************************************************\n'

print 'Content:'
print r.text
