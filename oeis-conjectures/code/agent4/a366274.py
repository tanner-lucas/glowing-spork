import numpy as np, math
from sympy import primerange
N=2*10**7
sieve=np.ones(2*N+10,dtype=bool); sieve[:2]=False
for i in range(2,int((2*N+10)**.5)+1):
    if sieve[i]: sieve[i*i::i]=False
pi=np.cumsum(sieve)
primes=np.nonzero(sieve)[0]
P=primes[primes<N]
n=np.arange(1,len(P))  # n index 1..len-1 (1-based): p_n=P[n-1], p_{n+1}=P[n]
pn=P[:-1]; pn1=P[1:]
a=pi[pn+pn1-1]-n
print('first terms',a[:30].tolist())
viol=[(int(k),int(v)) for k,v in zip(n,a) if k>=3 and v>=k]
print('violations (n>=3):',viol[:10],'checked n up to',n[-1],'p_n up to',pn[-1])
# margin
r=(n-a)[2:]
print('min n-a(n) for n>=3:',r.min(),'at n=',int(n[2:][r.argmin()]))
# analytic check at boundary: for x>=396738, 2x(1+d)/(ln x -0.4069) vs 2x/(ln x-1) with d=1/(50 ln^2 x)
for x in [396738,1e6,1e9,1e20]:
    d=1/(50*math.log(x)**2); print(x, d*(math.log(x)-1), '< 0.5931')
