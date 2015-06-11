#!/usr/bin/env python

"""
This one is not solved by me :( - I don't deserve the credit - it all goes to github/mgraczyk
"""


import gmpy2

from gmpy2 import mpz
from gmpy2 import powmod
from gmpy2 import isqrt
from gmpy2 import isqrt_rem
from gmpy2 import div
from gmpy2 import invert

from math import ceil
from binascii import unhexlify

N_1 = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581

N_2 = 648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877

N_3 = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929

ciphertext_1 = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540

e_1 = 65537

Ns = (N_1, N_2, N_3)

def ceil_sqrt(x):
    s,t = isqrt_rem(x)
    return s + (1 if t else 0)

def check_factors(p,q,N):
    return p*q == N

def factor_with_average(A, N):
    x = isqrt(A**2 - N)
    return (A - x, A + x)

def check_ch3(i,A,N):
    p,q = (div(A + i - 1,3), div(A - i,2))
    if check_factors(p,q,N):
        return p,q

    p,q = (div(A - i,3), div(A + i - 1,2))
    if check_factors(p,q,N):
        return p,q

    return None
    

def ch3_factor(N):
    """ Valid when |3p - 2q| < N^(1/4)
    """

    A = ceil_sqrt(6*N)

    # let M = (3p+2q)/2
    # M is not an integer since 3p + 2q is odd
    # So there is some integer A = M + 0.5 and some integer i such that
    # 3p = M + i - 0.5 = A + i - 1
    # and
    # 2q = M - i + 0.5 = A - i
    #
    # N = pq = (A-i)(A+i-1)/6 = (A^2 - i^2 - A + i)/6
    # So 6N = A^2 - i^2 - A + i
    # i^2 - i = A^2 - A - 6N 

    # Solve using the quadratic equation!
    a = mpz(1)
    b = mpz(-1)
    c = -(A**2 - A - 6*N)

    det = b**2 - 4*a*c

    roots = (div(-b + isqrt(b**2 - 4*a*c), 2*a),
         div(-b - isqrt(b**2 - 4*a*c), 2*a))


    for i in roots:
        if i >= 0:
            f = check_ch3(i,A,N)
            if f:
                return f

    # We should have found the root
    assert(False)

def factor(N):
    N = mpz(N)

    # Valid when |p-q| < 2N^(1/4)
    A = ceil_sqrt(N)
    p,q = factor_with_average(A, N)
    if check_factors(p,q,N):
        return (p,q)

    # Valid when |p-q| < 2^11 * N^(1/4)
    for i in range(2**20):
        A += 1
        p,q = factor_with_average(A, N)
        if check_factors(p,q,N):
            return (p,q)

    return ch3_factor(N)

def decrypt_RSA(ciphertext, pk):
    N, e = pk

    p,q = factor(N)
    phiN = N - p - q + 1

    d = invert(e, phiN)

    return powmod(ciphertext, d, N)


def self_test():
    # Ns = Ns

    for num,N in enumerate(Ns):
        p,q = factor(N)

        if check_factors(p,q,N):
            print("N[{}]: Found p = \n{}\n".format(num, min(p,q)))
        else:
            print("ERROR: Incorrectly factored N[{}]!".format(num))

    # Find the plaintext
    pt = decrypt_RSA(ciphertext_1, (N_1, e_1))
    ptHex = hex(pt)
    pos = ptHex.find("00")
    print("Plaintext:")
    print(ptHex)
    print("Message:")
    print(unhexlify(ptHex[pos+2:]))

if __name__ == "__main__":
    self_test()


