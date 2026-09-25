# Independent random-access computation of A284365(n) = position of n-th 0 in the fixed point
# of 0->1, 1->101010 (A284364), via descent through the derivation tree.
import sys
from math import isqrt
img={0:[1],1:[1,0,1,0,1,0]}
K=40
Z=[[1,0]]; Ln=[[1,1]]
for k in range(1,K+1):
    Z.append([sum(Z[k-1][d] for d in img[c]) for c in (0,1)])
    Ln.append([sum(Ln[k-1][d] for d in img[c]) for c in (0,1)])
def a(n):
    k=K; c=1; m=n; off=0
    assert Z[K][1]>=n
    while k>0:
        for d in img[c]:
            if Z[k-1][d]<m: m-=Z[k-1][d]; off+=Ln[k-1][d]
            else: c=d; k-=1; break
    assert c==0 and m==1
    return off+1
def cmp_d(n,an,t):
    # sign of n*r - an - t, r=(9+sqrt21)/6  <=> sign of n*sqrt21 - (6(an+t)-9n)
    R=6*(an+t)-9*n
    if R<=0: return 1 if not (R==0 and n==0) else 0
    lhs=21*n*n; rhs=R*R
    return (lhs>rhs)-(lhs<rhs)
# check against OEIS data
S=open('/home/user/work/oeisdata/seq/A284/A284365.seq').read()
data=[int(x) for x in "".join(l[11:] for l in S.splitlines() if l[:2] in('%S','%T','%U')).replace('\n','').split(',') if x.strip()]
print("data match:", [a(n) for n in range(1,len(data)+1)]==data, len(data))
from decimal import Decimal, getcontext
getcontext().prec=60
r=(9+Decimal(21).sqrt())/6
for n in map(int,sys.argv[1:]):
    an=a(n)
    print(n, an, "n*r-a(n) =", n*r-an, " (>=2)?", cmp_d(n,an,2)>=0)
