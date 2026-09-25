from math import comb, factorial
import sys
s=lambda x: bin(x).count("1")
# A000139 parity
def fibbin(n): return n & (n>>1) == 0
bad=0
for n in range(0,200001):
    v = s(n)+s(n+1)-s(3*n)
    odd = (v==0)
    pred = (n%2==1) and fibbin(n)
    if odd!=pred: bad+=1; print("A000139 mismatch",n)
# exact check small n
for n in range(0,400):
    a = 2*factorial(3*n)//(factorial(2*n+1)*factorial(n+1))
    assert 2*factorial(3*n) % (factorial(2*n+1)*factorial(n+1))==0
    v=(a & -a).bit_length()-1
    assert v == s(n)+s(n+1)-s(3*n), n
print("A000139 checks done, mismatches:",bad)
# compare with OEIS A022341 terms
A022341=[1,5,9,17,21,33,37,41,65,69,73,81,85,129,133,137,145,149,161,165,169]
print("A022341 prefix ok:", [n for n in range(1,170) if n%2 and fibbin(n)]==A022341)
# A361034 parity
for n in range(0,600):
    num=2520*factorial(4*n); den=factorial(n)*factorial(n+2)**3
    assert num%den==0
    a=num//den
    assert (a%2==1) == ((n+2)&(n+1)==0), n
print("A361034 ok to 600")
