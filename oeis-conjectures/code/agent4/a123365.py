# number of distinct cube residues mod k, multiplicative; compute c(p^e) by brute force, then check c(k)=(k+2)/3
import sys
from sympy import factorint
N=int(sys.argv[1])
cache={}
def cpe(p,e):
    key=(p,e)
    if key not in cache:
        m=p**e
        if e==1:
            cache[key]=(p-1)//3+1 if p%3==1 else p
        else:
            cache[key]=len({pow(x,3,m) for x in range(m)}) if m<=4*10**6 else None
    return cache[key]
# smallest prime factor sieve
spf=list(range(N+1))
for i in range(2,int(N**.5)+1):
    if spf[i]==i:
        for j in range(i*i,N+1,i):
            if spf[j]==j: spf[j]=i
res=[]
for k in range(1,N+1):
    if (k+2)%3: continue
    m=k; c=1
    while m>1:
        p=spf[m]; e=0
        while m%p==0: m//=p; e+=1
        v=cpe(p,e)
        if v is None: c=None; break
        c*=v
    if c is not None and 3*c==k+2: res.append(k)
from sympy import isprime
odd=[k for k in res if not (isprime(k) and k%6==1)]
print(len(res), res[:15], 'non-(6k+1 prime) terms:', odd[:20])
