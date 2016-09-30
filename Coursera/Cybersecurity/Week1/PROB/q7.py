#!/usr/bin/env python

def a2num(str):
    numVal = 0
    for c in str:
        numVal = (numVal << 8) + ord(c)
    return numVal


def q7():
    string = "attack at dawn"
    strNew = "attack at dusk"
    # cypher = 0x6c73d5240a948c86981bc294814d
    cypher = 0x09e1c5f70a65ac519458e7e53f36
    numStr = a2num(string)

    key = cypher ^ numStr

    print "Original string: ", string
    print "Original cypher: ", hex(cypher)
    print "Key (string ^ cypher): ", hex(key)
    print "New string: ", strNew
    print "New cypher: ", hex(key ^ a2num(strNew))
    
if __name__ == '__main__':
    q7()
