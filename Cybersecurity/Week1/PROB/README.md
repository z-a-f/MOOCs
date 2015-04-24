## Answers to the problem set 1 (SPOILERS!!!)

These are the answers - if you didn't do them, please STOP READING NOW - there are a lot of spoilers :)
*NOTE:* The questions differ every time you do them

### Question 1
Data compression is often used in data storage and transmission. Suppose you want to use data compression in conjunction with encryption. Does it make more sense to:
- [X] Compress then encrypt.			
- [ ] Encrypt then compress.			
- [ ] The order does not matter -- either one is fine.
- [ ] The order does not matter -- neither one will compress the data.

##### Explanation
The order does matter - if the text is encrypter first, it will look random and compression will not really work. If compressed and then encrypted, the compression will work.

### Question 2
Let G:{0,1}<sup>s</sup>→{0,1}<sup>n</sup> be a secure PRG. Which of the following is a secure PRG (there is more than one correct answer):
- [ ] `G'(k)=G(k)||G(k)`        (here || denotes concatenation)
- [X] `G'(k)=G(k⊕1^s)`          (here 1^s means 1<sup>s</sup>)
- [ ] `G'(k)=G(0)`
- [ ] `G'(k)=G(k)||0`           (here || denotes concatenation)
- [X] `G'(k1,k2)=G(k1)||G(k2)`  (here || denotes concatenation)
- [X] `G'(k)=reverse(G(k))`,     where reverse(x) reverses the string x so that the first bit of x is the last bit of reverse(x), the second bit of x is the second to last bit of reverse(x), and so on.
 
##### Explanation
The outputs of unmarked answers above will not be random

### Question 3
Let G:K→{0,1}<sup>n</sup> be a secure PRG. Define G'(k1,k2)=G(k1)⋀G(k2) where ⋀ is the bit-wise AND function. Consider the following statistical test A on {0,1}<sup>n</sup>: 
A(x) outputs LSB(x), the least significant bit of x. 
What is Adv<sub>PRG</sub>[A,G']? You may assume that LSB(G(k)) is 0 for exactly half the seeds k in K. 

Note: Please enter the advantage as a decimal between 0 and 1 with a leading 0. If the advantage is 3/4, you should enter it as 0.75

`ANSWER: 0.25`

##### Explanation
LSB of G(k) is 0 with 50% chance. That means that the chances of two numbers LSB(G(k1)) and LSB(G(k2)) being 11 is 0.5*0.5 = 0.25 (AND function will produce 1 only in quarter of all values)

### Question 4
Let (E,D) be a (one-time) semantically secure cipher with key space K={0,1}<sup>ℓ</sup>. A bank wishes to split a decryption key k∈{0,1}<sup>ℓ</sup> into two pieces p1 and p2 so that both are needed for decryption. The piece p1 can be given to one executive and p2 to another so that both must contribute their pieces for decryption to proceed.

The bank generates random k1 in {0,1}<sup>ℓ</sup> and sets k1'←k⊕k1. Note that k1⊕k1'=k. The bank can give k1 to one executive and k1' to another. Both must be present for decryption to proceed since, by itself, each piece contains no information about the secret key k (note that each piece is a one-time pad encryption of k).

Now, suppose the bank wants to split k into three pieces p1,p2,p3 so that any two of the pieces enable decryption using k. This ensures that even if one executive is out sick, decryption can still succeed. To do so the bank generates two random pairs (k1,k1') and (k2,k2') as in the previous paragraph so that k1⊕k1'=k2⊕k2'=k. How should the bank assign pieces so that any two pieces enable decryption using k, but no single piece can decrypt?

- [ ] `p1=(k1,k2),  p2=(k1,k2),    p3=(k2')`
- [ ] `p1=(k1,k2),  p2=(k1',k2'),  p3=(k2')`
- [X] `p1=(k1,k2),  p2=(k1',k2),   p3=(k2')`
- [ ] `p1=(k1,k2),  p2=(k2,k2'),   p3=(k2')`
- [ ] `p1=(k1,k2),  p2=(k1'),      p3=(k2')`

##### Explanation
Combinations 1,2,5 cannot decrypt when any 2 people come together. Combination 4 can decrypt when only p2 is present. Thus, combination 3 is the only solution

### Question 5
Let M=C=K={0,1,2,…,255} and consider the following cipher defined over (K,M,C): 
`E(k,m)=m+k(mod 256); D(k,c)=c−k(mod 256)`
Does this cipher have perfect secrecy?
- [ ] No, there is a simple attack on this cipher.
- [X] Yes
- [ ] No, only the One Time Pad has perfect secrecy.

##### Explanation
This code has a perfect secrecy

### Question 6
Let (E,D) be a (one-time) semantically secure cipher where the message and ciphertext space is {0,1}<sup>n</sup>. Which of the following encryption schemes are (one-time) semantically secure?
- [ ] E'(k, m)=E(0<sup>n</sup>, m)
- [X] E'((k,k'), m)=E(k,m)||E(k', m)
- [ ] E'(k,m)=E(k,m)||LSB(m)
- [X] E'(k,m)=0||E(k,m)     (i.e. prepend 0 to the ciphertext)
- [ ] E'(k,m)=E(k,m)||k
- [X] E'(k,m)=reverse(E(k,m))

##### Explanation
1. To break semantic security, an attacker would ask for the encryption of 0<sup>n</sup> and 1<sup>n</sup> and can easily distinguish EXP(0) from EXP(1) because it knows the secret key, namely 0<sup>n</sup>.
2. an attack on E' gives an attack on E.
3. To break semantic security, an attacker would ask for the encryption of 0<sup>n</sup> and 0<sup>n-1</sup>1 and can distinguish EXP(0) from EXP(1).
4. an attack on E' gives an attack on E.
5. To break semantic security, an attacker would read the secret key from the challenge ciphertext and use it to decrypt the challenge ciphertext. Basically, any ciphertext reveals the secret key.
6. an attack on E' gives an attack on E.

### Question 7
Suppose you are told that the one time pad encryption of the message "attack at dawn" is _6c73d5240a948c86981bc294814d_ (the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex). What would be the one time pad encryption of the message "attack at dusk" under the same OTP key?

`ANSWER: 6c73d5240a948c86981bc2808548L`

##### Explanation
Given the original message and encoded cypher, we can recover that `key=d07a14569fface7ec3ba6f5f623L`. After XORing the key with the new message, we get the correct answer

### Question 8
The movie industry wants to protect digital content distributed on DVD’s. We develop a variant of a method used to protect Blu-ray disks called AACS.

Suppose there are at most a total of n DVD players in the world (e.g. n=2<sup>32</sup>). We view these n players as the leaves of a binary tree of height log2n. Each node in this binary tree contains an AES key k<sup>i</sup>. These keys are kept secret from consumers and are fixed for all time. At manufacturing time each DVD player is assigned a serial number i∈[0,n−1]. Consider the set of nodes Si along the path from the root to leaf number i in the binary tree. The manufacturer of the DVD player embeds in player number i the keys associated with the nodes in the set S<sub>i</sub>. A DVD movie m is encrypted as 

E(k<sub>root</sub>,k)||E(k,m) 

where k is a random AES key called a content-key and kroot is the key associated with the root of the tree. Since all DVD players have the key kroot all players can decrypt the movie m. We refer to E(k<sub>root</sub>,k) as the header and E(k,m) as the body. In what follows the DVD header may contain multiple ciphertexts where each ciphertext is the encryption of the content-key k under some key k<sub>i</sub> in the binary tree.

Suppose the keys embedded in DVD player number r are exposed by hackers and published on the Internet. In this problem we show that when the movie industry distributes a new DVD movie, they can encrypt the contents of the DVD using a slightly larger header (containing about log<sub>2</sub>n keys) so that all DVD players, except for player number r, can decrypt the movie. In effect, the movie industry disables player number r without affecting other players.

As shown below, consider a tree with n=16 leaves. Suppose the leaf node labeled 25 corresponds to an exposed DVD player key. Check the set of keys below under which to encrypt the key k so that every player other than player 25 can decrypt the DVD. Only four keys are needed.
![tree][treeDVD]
- [ ] 21
- [ ] 17
- [ ] 5
- [X] 26
- [X] 6
- [X] 1
- [X] 11
- [ ] 24

##### Explanation
Because key 25 is to the right of the key 0, we can safely include all elements under key 1. With the same logic (but different parent), we can include 6 and 11. In the remaining leafs the only thing we need to include is 26.


### Question 9
Continuing with the previous question, if there are n DVD players, what is the number of keys under which the content key k must be encrypted if exactly one DVD player's key needs to be revoked?
- [ ] n - 1
- [ ] √n
- [ ] n/2
- [ ] 2
- [X] log<sub>2</sub>n

##### Explanation
The key will need to be encrypted under one key for each node on the path from the root to the revoked leaf. There are log<sub>2</sub>n nodes on the path.

### Question 10
Continuing with question 8, suppose the leaf nodes labeled 16, 18, and 25 correspond to exposed DVD player keys. Check the smallest set of keys under which to encrypt the key k so that every player other than players 16,18,25 can decrypt the DVD. Only six keys are needed.
- [ ] 27
- [X] 6
- [ ] 24
- [X] 15
- [X] 11
- [X] 17
- [ ] 0
- [ ] 29
- [X] 4
- [X] 26

##### Explanation
Following the same logic as in question 8, we can exclude 16, 18, and 25



[treeDVD]: https://d396qusza40orc.cloudfront.net/crypto/images/revoke.png "Tree with Root=0, and 30 elements"
