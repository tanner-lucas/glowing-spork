from sympy import divisors
from math import prod
N=20000
seen={}
coll=[]
for n in range(1,N+1):
    ds=divisors(n); P=prod(ds)
    v=sum(P//d for d in ds)
    assert all(P%d==0 for d in ds)
    if v in seen: coll.append((seen[v],n,v))
    else: seen[v]=n
print("collisions up to",N,":",coll[:20], len(coll))
