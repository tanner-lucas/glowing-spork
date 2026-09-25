import sys
from sympy import primepi, prime, factorint
import numpy as np
N=int(sys.argv[1])
# sieve spf and prime index
L=N*5+100  # sigma(k) < ~5k for k<=N? sigma(k)/k < 5 for k < 1e7? use factorint fallback
spf=np.zeros(L+1,dtype=np.int64)
for i in range(2,L+1):
    if spf[i]==0:
        spf[i::i][spf[i::i]==0]=i
pidx=np.zeros(L+1,dtype=np.int64); 
primes=np.nonzero(spf==np.arange(L+1))[0]; primes=primes[primes>=2]
pidx[primes]=np.arange(1,len(primes)+1)
def fac(n):
    f={}
    while n>1:
        p=int(spf[n]); e=0
        while n%p==0: n//=p; e+=1
        f[p]=e
    return f
def A348717(n):
    if n==1: return 1
    f=fac(n) if n<=L else factorint(n)
    ps=sorted(f); p1=int(pidx[ps[0]]) if ps[0]<=L else int(primepi(ps[0]))
    r=1
    for p in ps:
        i=int(pidx[p]) if p<=L else int(primepi(p))
        r*=int(primes[i-p1])**f[p]   # prime(i+1-p1) = primes[i-p1] (0-based)
    return r
def sigma(n):
    s=1
    for p,e in fac(n).items(): s*=(p**(e+1)-1)//(p-1)
    return s
from math import isqrt
terms=[]; bad=[]
for k in range(1,N+1):
    s=sigma(k)
    if A348717(k)%A348717(s)==0:
        terms.append(k)
        if k!=2 and isqrt(k)**2!=k: bad.append(k)
print(terms[:20]); print('non-square terms other than 2:',bad[:20], 'count terms',len(terms))
