#!/usr/bin/env python

def q8():
    str1 = (
        'We see immediately that one needs little information to begin to break down the process.',
        'To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.',
        'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.',
        'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
       )
    str2  = (
        'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.',
        'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.',
        'An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.',
        'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
    )
    str3 = (
        'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.',
        'We see immediately that one needs little information to begin to break down the process.',
        'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.',
        'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.'
    )
    for i in range(len(str1)):
        print "%d. %d"%(i+1,len(str1[i]))
        # print "%d. %d"%(i+1,abs(len(str[i])/16)*16+16)
    print
    for i in range(len(str2)):
        print "%d. %d"%(i+1,len(str2[i]))
        # print "%d. %d"%(i+1,abs(len(str[i])/16)*16+16)
    print
    for i in range(len(str3)):
        print "%d. %d"%(i+1,len(str3[i]))
        # print "%d. %d"%(i+1,abs(len(str[i])/16)*16+16)

if __name__ == '__main__':
    q8()
