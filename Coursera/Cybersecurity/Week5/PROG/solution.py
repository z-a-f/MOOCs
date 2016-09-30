#!/usr/bin/env python

import gmpy2

from gmpy2 import divm
from gmpy2 import mpz
from gmpy2 import powmod

def compute_x0(p, g, h, B):
    return { (idx0, powmod(g, B*idx0, p)) for idx0 in range(B) }

def compute_x1(p, g, h, B):
    return { divm(h, powmod(g, idx1, p), p) : idx1 for idx1 in range(B) }

# Finding x = x0*B + x1
# h = (g**B)**x0 * g**x1
def solve (p, g, h, B):
    p = mpz(p)
    g = mpz(g)
    h = mpz(h)
    B = mpz(B)
    
    # Create both tables, and find the same one (space complexity is terrible)
    X0 = compute_x0(p, g, h, B)
    X1 = compute_x1(p, g, h, B)
    # print X0
    # print X1

    for x0, x0temp in X0:
        x1 = X1.get(x0temp)
        if x1 is not None:
            print "x0 =", x0, ", x1 =",x1
            out = mpz(x0)*B + mpz(x1)
            print "x =", out
            print "h =", h
            print "h'=", powmod(g, out, p)
            return out



def test_final():
    p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
    h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
    B = 2**20
    
    """print "x = ", """
    return solve(p, g, h, B)
    
if __name__ == '__main__':
    print "----------------------------------"
    print "----------------------------------"
    test_final()
