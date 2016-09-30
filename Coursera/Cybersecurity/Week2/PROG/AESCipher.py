#!/usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
import array

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class CBCcipher:
    def __init__(self, key):
        self.mode = AES.MODE_CBC
        self.key = key.decode('hex')

    def encrypt( self, raw, iv=Random.new().read( AES.block_size )):
        raw = pad(raw)
        cipher = AES.new( self.key, self.mode, IV=iv )
        return ( iv + cipher.encrypt( raw ) ).encode('hex')

    def decrypt( self, enc ):
        enc = enc.decode('hex')
        iv = enc[:16]
        cipher = AES.new(self.key, self.mode, IV=iv)
        return unpad(cipher.decrypt( enc[16:] ))

class CTRcipher:
    def __init__(self, key):
        self.mode = AES.MODE_CTR
        self.key = key.decode('hex')

    def encrypt( self, raw, iv=Random.new().read( AES.block_size )):
        raw = pad(raw)
        cipher = AES.new( self.key, self.mode, IV=iv )
        ctr = Counter.new(128, initial_value=long(iv.encode("hex"), 16))
        return ( iv + cipher.encrypt( raw ) ).encode('hex')

    def decrypt( self, enc ):
        enc = enc.decode('hex')
        iv = enc[:16]
        ctr = Counter.new(128, initial_value=long(iv.encode("hex"), 16))
        cipher = AES.new(self.key, self.mode, counter=ctr)
        return cipher.decrypt( enc[16:] )
        # return unpad(cipher.decrypt( enc[16:] ))
    
def q1():
    key = '140b41b22a29beb4061bda66b6747e14'
    cipher = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
    cbc = CBCcipher(key)
    print "------------------------------------------------"
    print "Q1:"
    print cbc.decrypt(cipher)

def q2():
    key = '140b41b22a29beb4061bda66b6747e14'
    cipher = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
    cbc = CBCcipher(key)
    print "------------------------------------------------"
    print "Q2:"
    print cbc.decrypt(cipher)

def q3():
    key = '36f18357be4dbd77f050515c73fcf9f2'
    cipher = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
    ctr = CTRcipher(key)
    print "------------------------------------------------"
    print "Q3:"
    print ctr.decrypt(cipher)

def q4():
    key = '36f18357be4dbd77f050515c73fcf9f2'
    cipher = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
    ctr = CTRcipher(key)
    print "------------------------------------------------"
    print "Q4:"
    print ctr.decrypt(cipher)
    
if __name__ == '__main__':
    q1()
    q2()
    q3()
    q4()
    
