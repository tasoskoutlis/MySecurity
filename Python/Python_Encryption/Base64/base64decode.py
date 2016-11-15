import base64

msg = raw_input("Provide the Base64 message: ")

print "The decoded Base64 message is ", base64.decodestring(msg)