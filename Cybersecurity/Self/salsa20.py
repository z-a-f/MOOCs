#!/usr/bin/env python
"""
Python implementation of Salsa20 encryption
specs: http://cr.yp.to/snuffle/spec.pdf

Python version: 2.7.9
"""

import struct
import numpy as np

class Salsa20(object):
    """
    	How to use:
    		s20 = Salsa20()
		s20.setup(key, r)
    		cyphertext = s20.encrypt(message)
    """
    # Define constants:
    TAU     = ( 0x61707865, 0x3120646e, 0x79622d36, 0x6b206574 )
    REPEATS = 10
    
    def __init__ (self, key='\x00'*16, nonce='\x00'*8, counter='\x00'*8):
        self.setup(key, nonce, counter)

    def setup (self, key='\x00'*16, nonce='\x00'*8, counter=None):
        TAU = self.TAU
        self.key = key
        self.nonce = nonce
        if (counter == None):
            counter = self.counter
        else:
            self.counter = counter
        state = [0]*16
        k = list(struct.unpack('<4I', key))
        n = list(struct.unpack('<2I', nonce))
        c = list(struct.unpack('<2I', counter))

        # What do we do if the len(key) = 32? or 64?
        state = np.array([0]*16)
        state[0] = TAU[0]
        state[1] = k[0]
        state[2] = k[1]
        state[3] = k[2]
        state[4] = k[3]
        state[5] = TAU[1]
        
        state[6] = n[0]
        state[7] = n[1]
        state[8] = c[0]
        state[9] = c[1]
        
        state[10] = TAU[2]
        state[11] = k[0]
        state[12] = k[1]
        state[13] = k[2]
        state[14] = k[3]
        state[15] = TAU[3]

        self.state = state


    def _rotateLeft(self, a,b,bits):
        # rotate left, and fit in (bits) bits:
        return ((a << b) | (a >> (bits - b))) & (2**bits-1)
    
    def _quarterround(self, y):
        if len(y) != 4:
            raise Exception ('Size of array for quarterround has to be 4')
        y = np.array(y)
        z = np.array([0]*4)          # placeholder
        """
        z[1] = (y[1] ^ ((y[0]+y[3])<<7)) & 0xffffffff
        z[2] = (y[2] ^ ((z[1]+y[0])<<9)) & 0xffffffff
        z[3] = (y[3] ^ ((z[2]+z[1])<<13)) & 0xffffffff
        z[0] = (y[0] ^ ((z[3]+z[2])<<18)) & 0xffffffff
        """
        z[1] = y[1] ^ self._rotateLeft( (y[0]+y[3]), 7, 32 )
        z[2] = y[2] ^ self._rotateLeft( (z[1]+y[0]), 9, 32 )
        z[3] = y[3] ^ self._rotateLeft( (z[2]+z[1]), 13, 32 )
        z[0] = y[0] ^ self._rotateLeft( (z[3]+z[2]), 18, 32 )
        return z

    def _rowround(self, y):
        if len(y) != 16:
            raise Exception ('Size of array for rowround has to be 16')
        y = np.array(y)
        z = np.array([0]*16) # placeholder
        z[[0,1,2,3]] = self._quarterround(y[[0,1,2,3]])
        z[[5,6,7,4]] = self._quarterround(y[[5,6,7,4]])
        z[[10,11,8,9]] = self._quarterround(y[[10,11,8,9]])
        z[[15,12,13,14]] = self._quarterround(y[[15,12,13,14]])
        return z
        
    def _columnround(self, y):
        if len(y) != 16:
            raise Exception ('Size of array for columnround has to be 16')
        y = np.array(y)
        z = np.array([0]*16) # placeholder
        z[[0,4,8,12]] = self._quarterround(y[[0,4,8,12]])
        z[[5,9,13,1]] = self._quarterround(y[[5,9,13,1]])
        z[[10,14,2,6]] = self._quarterround(y[[10,14,2,6]])
        z[[15,3,7,11]] = self._quarterround(y[[15,3,7,11]])
        return z
        
    def _doubleround(self, y):
        if len(y) != 16:
            raise Exception ('Size of array for columnround has to be 16')
        y = np.array(y)
        return self._rowround(self._columnround(y))

    def _littleendian(self, y):
        if len(y) != 4:
            raise Exception ('Size of array for littleendian has to be 4')
        y = np.array(y)
        return y[0] + y[1]<<8 + y[2]<<16 + y[3]<<24

    def _breakInBytes32(self, y):
        z = np.array([0]*4)
        z[0] = (y & 0xff000000) >> 24
        z[1] = (y & 0x00ff0000) >> 16
        z[2] = (y & 0x0000ff00) >> 8
        z[3] = (y & 0x000000ff)
        return z
    
    def hash(self, goal=None,counter=None):
        if (counter == None):
            counter = self.counter
        if (counter != self.counter):
            self.setup(self.key, self.nonce, counter)
        if (goal==None):
            goal = self.state
        # y = np.array([0]*16)
        y = 0
        x = np.array([0]*16)
        for ii in range(16-4):
            x[ii] = self._littleendian(self._breakInBytes32(goal[ii]))
        # print x
        z = self._doubleround(x)
        for ii in range(9):
            z = self._doubleround(z)

        for ii in range(16):
            y = y << 8 + self._littleendian(self._breakInBytes32(x[ii]+z[ii]))
        return y        
    
        
#------------------------------------------------------------------------
def test():
    s20 = Salsa20()
    """
    Quarterround:
    quarterround(0x00000000, 0x00000000, 0x00000000, 0x00000000)
	    = (0x00000000, 0x00000000, 0x00000000, 0x00000000).
    quarterround(0x00000001, 0x00000000, 0x00000000, 0x00000000)
	    = (0x08008145, 0x00000080, 0x00010200, 0x20500000).
    quarterround(0x00000000, 0x00000001, 0x00000000, 0x00000000)
	    = (0x88000100, 0x00000001, 0x00000200, 0x00402000).
    quarterround(0x00000000, 0x00000000, 0x00000001, 0x00000000)
	    = (0x80040000, 0x00000000, 0x00000001, 0x00002000).
    quarterround(0x00000000, 0x00000000, 0x00000000, 0x00000001)
	    = (0x00048044, 0x00000080, 0x00010000, 0x20100001).
    quarterround(0xe7e8c006, 0xc4f9417d, 0x6479b4b2, 0x68c67137)
	    = (0xe876d72b, 0x9361dfd5, 0xf1460244, 0x948541a3).
    quarterround(0xd3917c5b, 0x55f1c407, 0x52a58a7a, 0x8f887a3b)
	    = (0x3e2f308c, 0xd90a8f36, 0x6ab2a923, 0x2883524c).
    """
    # y = (0x00000000, 0x00000000, 0x00000000, 0x00000000)
    # y = (0x00000001, 0x00000000, 0x00000000, 0x00000000)
    # y = (0x00000000, 0x00000001, 0x00000000, 0x00000000)
    y = (0xd3917c5b, 0x55f1c407, 0x52a58a7a, 0x8f887a3b)
    z = s20._quarterround(y)
    print '-'*48
    print 'Quarterround example: { ',
    for elem in z:
        print ('0x%08X ' % elem),
        # print ('%d ' % elem),
    print '}'

    """
    Rowround:
    rowround(0x00000001, 0x00000000, 0x00000000, 0x00000000,
    	0x00000001, 0x00000000, 0x00000000, 0x00000000,
    	0x00000001, 0x00000000, 0x00000000, 0x00000000,
    	0x00000001, 0x00000000, 0x00000000, 0x00000000)
	    = (0x08008145, 0x00000080, 0x00010200, 0x20500000,
	    0x20100001, 0x00048044, 0x00000080, 0x00010000,
	    0x00000001, 0x00002000, 0x80040000, 0x00000000,
	    0x00000001, 0x00000200, 0x00402000, 0x88000100).
    rowround(0x08521bd6, 0x1fe88837, 0xbb2aa576, 0x3aa26365,
	0xc54c6a5b, 0x2fc74c2f, 0x6dd39cc3, 0xda0a64f6,
	0x90a2f23d, 0x067f95a6, 0x06b35f61, 0x41e4732e,
	0xe859c100, 0xea4d84b7, 0x0f619bff, 0xbc6e965a)
	    = (0xa890d39d, 0x65d71596, 0xe9487daa, 0xc8ca6a86,
	    0x949d2192, 0x764b7754, 0xe408d9b9, 0x7a41b4d1,
	    0x3402e183, 0x3c3af432, 0x50669f96, 0xd89ef0a8,
	    0x0040ede5, 0xb545fbce, 0xd257ed4f, 0x1818882d).
    """
    y = (0x00000001, 0x00000000, 0x00000000, 0x00000000,
    	0x00000001, 0x00000000, 0x00000000, 0x00000000,
    	0x00000001, 0x00000000, 0x00000000, 0x00000000,
    	0x00000001, 0x00000000, 0x00000000, 0x00000000)
    # y = (0x08521bd6, 0x1fe88837, 0xbb2aa576, 0x3aa26365,
    #     0xc54c6a5b, 0x2fc74c2f, 0x6dd39cc3, 0xda0a64f6,
    #     0x90a2f23d, 0x067f95a6, 0x06b35f61, 0x41e4732e,
    #     0xe859c100, 0xea4d84b7, 0x0f619bff, 0xbc6e965a)
    z = s20._rowround(y)
    print '-'*48
    print 'Rowround example: { ',
    for elem in z:
        print ('0x%08X ' % elem),
        # print ('%d ' % elem),
    print '}'


    """
    Salsa20( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    = ( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0).
    Salsa20(211,159, 13,115, 76, 55, 82,183, 3,117,222, 37,191,187,234,136,
    49,237,179, 48, 1,106,178,219,175,199,166, 48, 86, 16,179,207,
    31,240, 32, 63, 15, 83, 93,161,116,147, 48,113,238, 55,204, 36,
    79,201,235, 79, 3, 81,156, 47,203, 26,244,243, 88,118,104, 54)
    = (109, 42,178,168,156,240,248,238,168,196,190,203, 26,110,170,154,
    29, 29,150, 26,150, 30,235,249,190,163,251, 48, 69,144, 51, 57,
    118, 40,152,157,180, 57, 27, 94,107, 42,236, 35, 27,111,114,114,
    219,236,232,135,111,155,110, 18, 24,232, 95,158,179, 19, 48,202).
    Salsa20( 88,118,104, 54, 79,201,235, 79, 3, 81,156, 47,203, 26,244,243,
    191,187,234,136,211,159, 13,115, 76, 55, 82,183, 3,117,222, 37,
    86, 16,179,207, 49,237,179, 48, 1,106,178,219,175,199,166, 48,
    238, 55,204, 36, 31,240, 32, 63, 15, 83, 93,161,116,147, 48,113)
    = (179, 19, 48,202,219,236,232,135,111,155,110, 18, 24,232, 95,158,
    26,110,170,154,109, 42,178,168,156,240,248,238,168,196,190,203,
    69,144, 51, 57, 29, 29,150, 26,150, 30,235,249,190,163,251, 48,
    27,111,114,114,118, 40,152,157,180, 57, 27, 94,107, 42,236, 35).
    """
    # y = ( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    y = (211,159, 13,115, 76, 55, 82,183, 3,117,222, 37,191,187,234,136,
    49,237,179, 48, 1,106,178,219,175,199,166, 48, 86, 16,179,207,
    31,240, 32, 63, 15, 83, 93,161,116,147, 48,113,238, 55,204, 36,
    79,201,235, 79, 3, 81,156, 47,203, 26,244,243, 88,118,104, 54)
    z = s20.hash(Manybytes2words(y))
    print '-'*48
    print z

def bytes2word(y):
    y = np.array(y)
    z = 0
    for ii in range(len(y)):
        z = z << 8 + y[ii]
    return z

def Manybytes2words(y):
    y = np.array(y)
    z = np.array([0]*16)
    for ii in range(16):
        z[ii] = bytes2word(y[ii*4:ii*4+4])
    return z

if __name__ == '__main__':
    test()
