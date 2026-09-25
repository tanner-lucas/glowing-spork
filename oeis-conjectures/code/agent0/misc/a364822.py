from math import comb
from sympy import isprime
N=1500
a=[0]*(N+1)
C=[[1]]
for n in range(N+1):
    s = 1 if n%2==0 else 0
    # a(n) = c(n) + 2*sum_{k odd} C(n,k) a(n-k)
    row=[comb(n,k) for k in range(n+1)]
    for k in range(1,n+1,2): s+=2*row[k]*a[n-k]
    a[n]=s
assert a[:11]==[1,2,9,56,465,4832,60249,876416,14570145,272502272,5662834089], a[:11]
print("primes p with a(p)!=2 mod p:", [p for p in range(3,N+1) if isprime(p) and (a[p]-2)%p])
print("m with a(2^m)!=1 mod 2^m:", [m for m in range(1,11) if 2**m<=N and (a[2**m]-1)%(2**m)])
print("composite odd n with a(n)==2 mod n:", [n for n in range(9,N+1,2) if not isprime(n) and (a[n]-2)%n==0][:20])
