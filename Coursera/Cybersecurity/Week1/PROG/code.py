#!/usr/bin/env python3.3
import binascii

max_key_length = 14
CHARACTERS_LENGTH = 256
FILENAME = 'cypher.txt'

with open(FILENAME) as file:
    ciphertext = file.read()

ciphertext = binascii.unhexlify(ciphertext.strip())

# occurences is an array of length 256
# each position is the number of occurences of byte i
def init(occurences):
    occurences.clear()
    for i in range(CHARACTERS_LENGTH):
        occurences.append(0)

def display(occurences):
    for i in range(CHARACTERS_LENGTH):
        print('Char %d : %d' % (i, occurences[i]))

def compute_distribution(occurences):
    distribution = 0
    for i in range(len(occurences)):
        distribution += (occurences[i] / CHARACTERS_LENGTH) ** 2
    return distribution

occurences = []

def find_key_length(occurences):
    max_distribution = 0
    for N in range(2, max_key_length):
        init(occurences)
        for i in range(len(ciphertext)):
            if i % N == 0:
                l = ciphertext[i]
                occurences[l] += 1
        distribution = compute_distribution(occurences) * N
        if distribution > max_distribution:
            max_distribution = distribution
            key_length = N
        print('N = %d: %f' % (N, distribution))
    return key_length

key_length = find_key_length(occurences)
print('Key length = %d' % key_length)

def find_bytes(N):
    stream = ciphertext[0:len(ciphertext):N]
    for b in range(1, CHARACTERS_LENGTH + 1):
        streamb = []
        for char in stream:
            streamb.append(char ^ b)
        print(streamb)
# TODO: if one character in streamb is outside the 32 => 127 range, then we can exclude b
find_bytes(key_length)
