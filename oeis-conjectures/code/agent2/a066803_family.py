# Find primes p = c*2^n+1 (small c) with ord_p(2) = ord_p(3) = 2^(m+1), i.e. p | gcd(2^(2^m)+1, 3^(2^m)+1)
import gmpy2
from gmpy2 import mpz, powmod, is_prime
res=[]
for c in range(1,200,2):
  for n in range(1,3400):
    p = mpz(c)*(mpz(2)**n)+1
    if not is_prime(p,30): continue
    # order of 2 is a power of 2 iff 2^(2^n) == 1 (mod p) ... check 2^(2^n) mod p ==1 by n squarings
    x=mpz(2); m=-1
    for i in range(n+1):
      if x==p-1: m=i; break
      x=x*x % p
    if m<0: continue   # ord(2) not a power of 2 (<=2^n)
    if powmod(3, mpz(2)**m, p)==p-1:
      res.append((c,n,m))
      print("p = %d*2^%d+1 divides both 2^(2^%d)+1 and 3^(2^%d)+1"%(c,n,m,m), flush=True)
