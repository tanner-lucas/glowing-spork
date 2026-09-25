import numpy as np
N=10**7
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
primes=np.nonzero(s)[0]
R=np.zeros(N+1,dtype=bool)
for q in primes:
    r=int(str(q)[::-1])
    if str(q)[-1]!='0' and r<=N: R[r]=True
found=np.zeros(N+1,dtype=bool); found[:4]=True
for p in primes[:5000]:
    idx=np.arange(p+1,N+1)          # n with n-p>=1
    hit=R[idx-p] & ~found[idx]
    found[idx[hit]]=True
    if found.all(): break
missing=np.nonzero(~found)[0]
print('n<=1e7 without representation using primes p <= %d:'%p, missing[:20], len(missing))
