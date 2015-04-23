#!/usr/bin/env python

def a2num(str):
    numVal = 0
    for c in str:
        numVal = (numVal << 8) + ord(c)
    return numVal


def q7():
    str = "attack at dawn"
    strNew = "attack at dusk"
    cypher = 0x6c73d5240a948c86981bc294814d
    numStr = a2num(str)

    key = cypher ^ numStr

    print hex(key ^ a2num(strNew))
    
if __name__ == '__main__':
    q7()
