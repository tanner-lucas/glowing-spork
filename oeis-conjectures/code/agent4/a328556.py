import numpy as np, sys
from sympy import primerange
N=int(sys.argv[1])
pp=[]
for p in primerange(2,N+1):
    q=p
    while q<=N: pp.append(q); q*=p
pp.sort()
res=[]
for P in [(1<<61)-1, 4611686018427387847]:
    a=np.zeros(N+1,dtype=np.int64); a[0]=1
    for q in pp:
        t=a[q:]-a[:-q]
        t%=P
        a[q:]=t
    res.append(a)
zeros=[i for i in range(N+1) if res[0][i]==0 and res[1][i]==0]
print(len(zeros), zeros[-5:])
# print first terms signed
P=(1<<61)-1
v=[int(x) if x<P//2 else int(x)-P for x in res[0][:40]]
print(v)
