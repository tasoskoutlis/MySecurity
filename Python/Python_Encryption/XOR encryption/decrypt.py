#!/usr/bin/python

def decrypt_file(the_key):
    input_file = open('trash.crypt', 'rb')
    output_file = open('trash-decrypted.pdf', 'wb')
    key_index = 0
    for byte in input_file.read():
        encrypted_byte = chr(ord(the_key[key_index]) ^ ord(byte))
        output_file.write(encrypted_byte)
        key_index = key_index + 1
        if key_index >= len(the_key):
            key_index = 0
    output_file.close()
    input_file.close()


the_key = 'BABAAAAABABBAABB'
decrypt_file(the_key)

