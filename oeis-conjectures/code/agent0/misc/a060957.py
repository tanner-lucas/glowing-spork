import sys
from sympy import primerange
N=int(sys.argv[1])
S={1}
data=[1,1,2,4,8,16,26,52,88,152,238,476,648,1296,2016,2984,4232,8464,11360]
for n in range(1,N+1):
    S = S | {x*n for x in S}
    if n<len(data): assert len(S)==data[n], (n,len(S))
    if n>=4:
        bad=None
        for p in primerange(2,n+1):
            groups={}
            for x in S:
                e=0; u=x
                while u%p==0: u//=p; e+=1
                groups.setdefault(u,[]).append(e)
            for u,es in groups.items():
                es.sort()
                if es[-1]-es[0]+1!=len(es):
                    bad=(p,u,es); break
            if bad: break
        print(n,len(S),"violation:",bad, flush=True)
