# search k = 2*m^2 (m>=2) that are terms of A364131: A348717(k) multiple of A348717(sigma(k))
import sys
from sympy import factorint, primepi, prime, prevprime
from functools import lru_cache
M=int(sys.argv[1])
@lru_cache(maxsize=None)
def fsig(p,e):  # factorization of sigma(p^e)
    return factorint((p**(e+1)-1)//(p-1))
@lru_cache(maxsize=None)
def pi_(p): return int(primepi(p))
@lru_cache(maxsize=None)
def pr(i): return int(prime(i))
found=[]
for m in range(2,M+1):
    f=factorint(m); f={p:2*e for p,e in f.items()}; f[2]=f.get(2,0)+1   # k=2m^2
    k=2*m*m
    s={}
    for p,e in f.items():
        for q,c in fsig(p,e).items(): s[q]=s.get(q,0)+c
    q1=min(s); shift=pi_(q1)-1
    # A348717(sigma(k)) = prod prime(pi(q)-shift)^c ; A348717(k)=k (k even)
    ok=True; kk=k
    for q,c in s.items():
        r=pr(pi_(q)-shift)
        t=r**c
        if kk % t: ok=False; break
        kk//=t
    if ok: found.append(m); print('FOUND k=2*%d^2=%d'%(m,k), flush=True)
print('searched m<=',M,'found',found)
