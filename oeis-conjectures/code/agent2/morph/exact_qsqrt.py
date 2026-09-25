# Exact DP in Q(sqrt(D)) for the boundary cases.
from fractions import Fraction as F
class Q:
    D=3
    def __init__(s,a,b=0): s.a=F(a); s.b=F(b)
    def __add__(s,o): o=o if isinstance(o,Q) else Q(o); return Q(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __neg__(s): return Q(-s.a,-s.b)
    def __sub__(s,o): return s+(-(o if isinstance(o,Q) else Q(o)))
    def __mul__(s,o): o=o if isinstance(o,Q) else Q(o); return Q(s.a*o.a+Q.D*s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def inv(s): n=s.a*s.a-Q.D*s.b*s.b; return Q(s.a/n,-s.b/n)
    def __truediv__(s,o): o=o if isinstance(o,Q) else Q(o); return s*o.inv()
    def sign(s):
        a,b=s.a,s.b
        if a>=0 and b>=0: return 0 if (a==0 and b==0) else 1
        if a<=0 and b<=0: return -1
        # opposite signs
        v=a*a-Q.D*b*b
        if a>0: return 1 if v>0 else (-1 if v<0 else 0)
        else: return -1 if v>0 else (1 if v<0 else 0)
    def __lt__(s,o): return (s-o).sign()<0
    def __le__(s,o): return (s-o).sign()<=0
    def __eq__(s,o): return (s-o).sign()==0
    def __float__(s): return float(s.a)+float(s.b)*Q.D**0.5
    def __repr__(s): return f"({s.a}+{s.b}*sqrt{Q.D})"
def run(i0,i1,start,power,t,D,l2,f0,K=40,mode='min'):
    Q.D=D
    img={0:i0,1:i1}; tau={c:str(c) for c in (0,1)}
    for _ in range(power): tau={c:"".join(img[int(x)] for x in tau[c]) for c in (0,1)}
    ft = f0 if t==0 else Q(1)-f0
    def delta(p): return Q(p.count(str(t)))-ft*len(p)
    edges={c:[(tau[c][:j],int(tau[c][j])) for j in range(len(tau[c]))] for c in (0,1)}
    val={c:(Q(0) if c==t else None) for c in (0,1)}
    out=[]
    pw=Q(1)
    for j in range(1,K+1):
        new={}
        for c in (0,1):
            best=None
            for p,d in edges[c]:
                if val[d] is None: continue
                v=pw*delta(p)+val[d]
                if best is None or (v<best if mode=='min' else best<v): best=v
            new[c]=best
        val=new; pw=pw*l2
        out.append(val[start])
    r=Q(1)/ft
    return [r*(v+Q(1)-ft) for v in out]
import sys
s3=Q(0,1); Q.D=3
# A284752: 0->01,1->0001, start 0, t=0; lambda2 = 1-sqrt3; f0=(3-sqrt3)/2
Q.D=3
vals=run("01","0001",0,1,0,3,Q(1,-1),Q(F(3,2),F(-1,2)),K=40,mode='min')
print("A284752 inf pattern (value+1):",[ (v+1) for v in vals[-6:]]); print(" all > -1:", all((v+1).sign()>0 for v in vals))
# ratio check (value+1) at consecutive K
print(" ratios:",[float((vals[k]+1)/(vals[k-1]+1)) if (vals[k-1]+1).sign()!=0 else None for k in range(30,40)])
