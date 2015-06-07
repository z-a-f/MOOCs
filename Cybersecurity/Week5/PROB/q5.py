#!/usr/bin/env python

def extEuler(a, b):
    # Define q, r, s, t
    q = [[None] * 2]
    r = [a, b]
    s = [1, 0]
    t = [0, 1]

    idx = 2                     # Current index
    while r[-1] != 0:
        q.append((r[-2]) / (r[-1]))
        r.append(r[-2] - q[-1]*r[-1])
        s.append(s[-2] - q[-1]*s[-1])
        t.append(t[-2] - q[-1]*t[-1])
    # print q
    # print r
    # print s
    # print t
    return (r[-2],s[-2],t[-2])  # Return remainder and two variables

def solveLinear(a, b, c, p):
    # Solve equation ax + b = c (mod p)
    for x in range(p):
        if ((a * x + b) % p == c):
            return x

    return None
    
    
        
def q5():
    return extEuler(7, 23)

def q6():
    return solveLinear(3, 2, 7, 19)
    
if __name__ == '__main__':
    print q5()
    print "----------------"
    print q6()
    print "----------------"
    
