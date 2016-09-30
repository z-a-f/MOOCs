## Answers to the problem set 1 (SPOILERS!!!)

These are the answers - if you didn't do them, please STOP READING NOW - there are a lot of spoilers :)
*NOTE:* The questions differ every time you do them

### Question 1
Consider the following five events:
Correctly guessing a random 128-bit AES key on the first try.
1. Winning a lottery with 1 million contestants (the probability is 1/10<sup>6</sup> ).
2. Winning a lottery with 1 million contestants 5 times in a row (the probability is (1/10<sup>6</sup>)<sup>5</sup> ).
3. Winning a lottery with 1 million contestants 6 times in a row.
4. Winning a lottery with 1 million contestants 7 times in a row.
5. What is the order of these events from most likely to least likely?
- [ ] 3, 2, 5, 4, 1			
- [ ] 2, 4, 3, 1, 5			
- [ ] 2, 3, 5, 4, 1
- [X] 2, 3, 4, 1, 5

##### Explanation
Guessing AES key on the first try has probability of 1/2<sup>128</sup>≈1/10<sup>38.53</sup>. Thus, it has to be between options 4 and 5.

### Question 2
Suppose that using commodity hardware it is possible to build a computer for about $200 that can brute force about 1 billion AES keys per second. Suppose an organization wants to run an exhaustive search for a single 128-bit AES key and was willing to spend 4 trillion dollars to buy these machines (this is more than the annual US federal budget). How long would it take the organization to brute force this single 128-bit AES key with these machines? Ignore additional costs such as power and maintenance.
- [ ] More than a week but less than a month
- [ ] More than an hour but less than a day
- [ ] More than a year but less than 100 years
- [X] More than a billion (10<sup>9</sup>) years
- [ ] More than a million years but less than a billion (10<sup>9</sup>) years
 
##### Explanation
The total budget is $4 trillion dollars (4·10<sup>12</sup>), while every computer costs $200. That means the company can afford 20·10<sup>9</sup> machines. If every machine checks 10<sup>9</sup> keys per second, the company can check 20·10<sup>9</sup>·10<sup>9</sup>=20·10<sup>18</sup> keys per second. In the worst case scenario there are 2·10<sup>128</sup> keys to check, so it will take the company ≈1.7·10<sup>19</sup> seconds ≈ 5.4·10<sup>12</sup> years to break.

### Question 3
Let F:{0,1}<sup>n</sup>×{0,1}<sup>n</sup>→{0,1}<sup>n</sup> be a secure PRF (i.e. a PRF where the key space, input space, and output space are all {0,1}<sup>n</sup>) and say n=128. Which of the following is a secure PRF (there is more than one correct answer):
- [ ] F′(k, x)={F(k,x) when x≠0<sup>n</sup> ; 0<sup>n</sup> otherwise
- [X] F′(k,x)=F(k,x)\[0,…,n−2\]     (i.e., F′(k,x) drops the last bit of F(k,x))
- [X] F′((k1,k2), x)=F(k1,x)||F(k2,x)    (here || denotes concatenation)
- [X] F′(k, x)=k⨁x
- [ ] F′(k,x)=F(k, x)⨁F(k, x⊕1<sup>n</sup>)
- [X] F′(k,x)=F(k, x⨁1<sup>n</sup>)

##### Explanation
1. Cannot be secure, as the attacker can send m=0<sup>n</sup>
2. Any bit in the F′ will look like it originated from a truly random generator
3. Two random strings of bits are still indistinguishable from truly random
4. The same as one-time pad algo...
5. F(k, x)⨁F(k, x⊕1<sup>n</sup>)=0<sup>n</sup>, so NO!
6. F(k, x⨁1<sup>n</sup>) = F(k, x), so YES!

### Question 4
Recall that the Luby-Rackoff theorem discussed in [Lecture 3.2](https://www.coursera.org/crypto/lecture/view?lecture_id=13) states that applying a three round Feistel network to a secure PRF gives a secure block cipher. Let's see what goes wrong if we only use a two round Feistel. Let F:K×{0,1}<sup>32</sup>)→{0,1}<sup>32</sup>) be a secure PRF. Recall that a 2-round Feistel defines the following PRP   F2:K<sup>2</sup>×{0,1}<sup>64</sup>)→{0,1}<sup>64</sup>): 
![fNetwork][feisterNet]
Here R0 is the right 32 bits of the 64-bit input and L0 is the left 32 bits. 

One of the following lines is the output of this PRP F2 using a random key, while the other three are the output of a truly random permutation f:{0,1}<sup>64</sup>→{0,1}<sup>64</sup>. All 64-bit outputs are encoded as 16 hex characters. Can you say which is the output of the PRP?   Note that since you are able to distinguish the output of F2 from random, F2 is not a secure block cipher, which is what we wanted to show. 

Hint: First argue that there is a detectable pattern in the xor of F2(⋅,0<sup>64</sup>) and F2(⋅,1<sup>32</sup>0<sup>32</sup>). Then try to detect this pattern in the given outputs.
- [ ] On input 0<sup>64</sup> the output is "7b50baab 07640c3d".    On input 1<sup>32</sup>0<sup>32</sup> the output is "ac343a22 cea46d60".
- [ ] On input 0<sup>64</sup> the output is "4af53267 1351e2e1".    On input 1<sup>32</sup>0<sup>32</sup> the output is "87a40cfa 8dd39154".
- [ ] On input 0<sup>64</sup> the output is "5f67abaf 5210722b".    On input 1<sup>32</sup>0<sup>32</sup> the output is "bbe033c0 0bc9330e".
- [X] On input 0<sup>64</sup> the output is "9f970f4e 932330e4".    On input 1<sup>32</sup>0<sup>32</sup> the output is "6068f0b1 b645c008".

##### Explanation
If we XOR two messages with the same right hand side, and different left hand sides, two round Feistel network produces L1⨁L2...

[feistelNet]: https://d396qusza40orc.cloudfront.net/crypto/images/Feistel.jpg "Feistel network block with 2 rounds"

