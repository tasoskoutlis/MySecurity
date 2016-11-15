import base64

msg = raw_input("Provide the message to encode in Base64: ")

print "The encoded Base64 message is ", base64.encodestring(msg)