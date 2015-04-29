#!/usr/bin/env python

def q4():
    # a = (
    #     0x7b50baab07640c3d,
    #     0x4af532671351e2e1,
    #     0x5f67abaf5210722b,
    #     0x9f970f4e932330e4
    # )
    # b = (
    #     0xac343a22cea46d60,
    #     0x87a40cfa8dd39154,
    #     0xbbe033c00bc9330e,
    #     0x6068f0b1b645c008
    # )
    a = (
        0x9d1a4f78cb28d863,
        0x290b6e3a39155d6f,
        0x7c2822ebfdc48bfb,
        0x5f67abaf5210722b
    )
    b = (
        0x75e5e3ea773ec3e6,
        0xd6f491c5b645c008,
        0x325032a9c5e2364b,
        0xbbe033c00bc9330e
    )
    print "a =",
    print a
    print "b =",
    print b
    """
    for ii in range(len(a)):
        print ""
        for jj in range(len(b)):
            num1 = (a[ii]^b[jj]) >> 32
            num2 = (a[ii]^b[jj]) & 0xffffffff
            print "a[%d]^b[%d]=0x %8x %8x"%(ii,jj,num1, num2)
    """
    for ii in range(len(a)):
        num1 = (a[ii]^b[ii]) >> 32
        num2 = (a[ii]^b[ii]) & 0xffffffff
        print "a[%d]^b[%d]=0x %8x %8x"%(ii,ii,num1, num2)
if __name__ == '__main__':
    q4()
