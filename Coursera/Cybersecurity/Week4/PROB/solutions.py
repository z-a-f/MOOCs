#!/usr/bin/env python

def q1():
    iv = '20814804c1767293b99f1d9cab3bc3e7'
    cipher = 'ac1e37bfb15599e5f40eef805488281d'
    message = 'Pay Bob 100$'

    print "------------------------------------------------"
    print "Q1:"
    print 'Encoded text is: %s' % cipher
    print 'Encoded character is: %s' % cipher[16:18]
    print 'Encoding IV is: %s' % iv[16:18]
    ivByte = int(iv[16:18], 16)
    cipherByte = int(cipher[16:18], 16)
    cipherByte = cipherByte ^ ivByte
    messageByte = int(message[8], 16)
    newMessageByte = 5

    newCipherByte = cipherByte ^ messageByte ^ newMessageByte

    
    


    

    
if __name__ == '__main__':
    q1()
    
