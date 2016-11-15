import hashlib

md5hash = hashlib.md5('password123')
sha1hash = hashlib.sha1('password123')

print 'md5 hash is ', md5hash.hexdigest()
print "SHA1 hash is", sha1hash.hexdigest()