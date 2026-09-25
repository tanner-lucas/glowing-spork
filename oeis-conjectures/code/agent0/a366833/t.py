import gmpy2
from sympy import primerange
LIM=10**18
# non-square proper prime powers p^k, k>=3
hp=[]
for p in primerange(2,10**6+1):
    v=p**3
    while v<=LIM:
        hp.append(v); v*=p
hp.sort()
print("higher powers:",len(hp))
def is_pp(n):
    # proper prime power (k>=2) test
    if n<4: return False
    for k in range(2,64):
        r,exact=gmpy2.iroot(n,k)
        if r<2: break
        if exact and gmpy2.is_prime(r): return True
    return False
# brute force small range: count prime powers between consecutive primes up to 10^7
import numpy as np
N=10**7
sieve=np.ones(N+1,dtype=bool); sieve[:2]=False
for i in range(2,int(N**.5)+1):
    if sieve[i]: sieve[i*i::i]=False
primes=np.nonzero(sieve)[0]
pp=set()
for p in primes[primes<=int(N**.5)+1]:
    v=int(p)*int(p)
    while v<=N: pp.add(v); v*=int(p)
pp=np.array(sorted(pp))
idx=np.searchsorted(primes,pp)  # index of next prime >= pp
from collections import Counter
c=Counter(idx.tolist())
mx=max(c.values()); print("max proper prime powers in one prime gap up to 1e7:",mx, [ (int(primes[i-1]),int(primes[i])) for i,v in c.items() if v>=2][:8])
# large range: pairs of higher powers within 3000
cand=[]
for i in range(len(hp)-1):
    j=i+1
    while j<len(hp) and hp[j]-hp[i]<3000:
        cand.append((hp[i],hp[j])); j+=1
print("close higher-power pairs:",len(cand))
found=[]
for a,b in cand:
    if a<10**6: continue
    # find the prime gap containing a: previous prime < a and next prime > a
    lo=int(gmpy2.prev_prime(a)) if hasattr(gmpy2,'prev_prime') else None
    hi=int(gmpy2.next_prime(a))
    if hi<b: continue   # a prime lies between a and b
    # lo: previous prime
    x=a-1
    while not gmpy2.is_prime(x): x-=1
    lo=x
    cnt=sum(1 for n in range(lo+1,hi) if is_pp(n))
    found.append((a,b,lo,hi,cnt))
print("pairs in same prime gap (>=1e6):",found)
