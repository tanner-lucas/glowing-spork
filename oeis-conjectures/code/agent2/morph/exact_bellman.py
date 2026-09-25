# Exact inf/sup (closure) of n*r - a(n) for positions of letter t in the fixed point of a 2-letter Pisot substitution,
# via an exactly-verified Bellman fixed point in Q(sqrt D).  Values = r*(V + 1 - f_t), V = sum_i lam^i delta(p_i)
# over reversed Dumont-Thomas paths starting at letter t.
from fractions import Fraction as F
from exact_qsqrt import Q
from sympy import factorint
import itertools
def setup(i0,i1,power):
    img={0:i0,1:i1}; tau={c:str(c) for c in (0,1)}
    for _ in range(power): tau={c:"".join(img[int(x)] for x in tau[c]) for c in (0,1)}
    M=[[tau[0].count('0'),tau[1].count('0')],[tau[0].count('1'),tau[1].count('1')]]
    tr=M[0][0]+M[1][1]; det=M[0][0]*M[1][1]-M[0][1]*M[1][0]; disc=tr*tr-4*det
    # disc = s^2 * D
    s=1; D=disc
    for p,e in factorint(disc).items():
        s*=p**(e//2); D//=p**(2*(e//2))
    Q.D=D
    l1=Q(F(tr,2),F(s,2)); l2=Q(F(tr,2),F(-s,2))
    f0=Q(M[0][1])/(Q(M[0][1])+l1-Q(M[0][0]))
    return tau,M,D,l1,l2,f0
def solve(i0,i1,start,power,t):
    tau,M,D,l1,l2,f0=setup(i0,i1,power)
    ft=f0 if t==0 else Q(1)-f0
    def delta(p): return Q(p.count(str(t)))-ft*len(p)
    rev={c:[] for c in (0,1)}
    for cp in (0,1):
        w=tau[cp]
        for j,ch in enumerate(w): rev[int(ch)].append((cp,w[:j]))
    neg = l2.sign()<0
    # numeric value iteration to find policy
    fl=float(l2); J={0:0.0,1:0.0}; S={0:0.0,1:0.0}
    for _ in range(3000):
        J2={c:min(float(delta(p))+fl*(S[cp] if neg else J[cp]) for cp,p in rev[c]) for c in (0,1)}
        S2={c:max(float(delta(p))+fl*(J[cp] if neg else S[cp]) for cp,p in rev[c]) for c in (0,1)}
        J,S=J2,S2
    polJ={c:min(rev[c],key=lambda e: float(delta(e[1]))+fl*(S[e[0]] if neg else J[e[0]])) for c in (0,1)}
    polS={c:max(rev[c],key=lambda e: float(delta(e[1]))+fl*(J[e[0]] if neg else S[e[0]])) for c in (0,1)}
    # exact solve by fixed-point iteration on the linear policy system (contraction) -> solve 4x4 linear system exactly
    # unknown vector x = [J0,J1,S0,S1]; equations x = b + A x
    idx={('J',0):0,('J',1):1,('S',0):2,('S',1):3}
    A=[[Q(0)]*4 for _ in range(4)]; b=[Q(0)]*4
    for c in (0,1):
        cp,p=polJ[c]; b[idx[('J',c)]]=delta(p); A[idx[('J',c)]][idx[('S' if neg else 'J',cp)]]=l2
        cp,p=polS[c]; b[idx[('S',c)]]=delta(p); A[idx[('S',c)]][idx[('J' if neg else 'S',cp)]]=l2
    # solve (I-A)x=b by Gaussian elimination over Q(sqrt D)
    Mx=[[ (Q(1) if i==j else Q(0)) - A[i][j] for j in range(4)]+[b[i]] for i in range(4)]
    for col in range(4):
        piv=next(r for r in range(col,4) if Mx[r][col].sign()!=0)
        Mx[col],Mx[piv]=Mx[piv],Mx[col]
        pv=Mx[col][col]
        Mx[col]=[v/pv for v in Mx[col]]
        for r in range(4):
            if r!=col and Mx[r][col].sign()!=0:
                fac=Mx[r][col]; Mx[r]=[Mx[r][k]-fac*Mx[col][k] for k in range(5)]
    x=[Mx[i][4] for i in range(4)]
    Jx={0:x[0],1:x[1]}; Sx={0:x[2],1:x[3]}
    # exact verification of Bellman optimality
    ok=True
    for c in (0,1):
        vals=[delta(p)+l2*(Sx[cp] if neg else Jx[cp]) for cp,p in rev[c]]
        if any(v<Jx[c] for v in vals) or not any(v==Jx[c] for v in vals): ok=False
        vals=[delta(p)+l2*(Jx[cp] if neg else Sx[cp]) for cp,p in rev[c]]
        if any(Sx[c]<v for v in vals) or not any(v==Sx[c] for v in vals): ok=False
    r=Q(1)/ft
    inf_=r*(Jx[t]+Q(1)-ft); sup_=r*(Sx[t]+Q(1)-ft)
    return D,l2,r,inf_,sup_,ok
from exact_extremes import cases as C
import sys
for (aid,i0,i1,st,pw,t,lo,hi) in C:
    D,l2,r,inf_,sup_,ok=solve(i0,i1,st,pw,t)
    Q.D=D
    lo_q=Q(lo) if not hasattr(lo,'mantissa') else None
    print(f"{aid:9s} D={D} lam2={l2} r={r}\n          inf={inf_} ~ {float(inf_):.12f}   sup={sup_} ~ {float(sup_):.12f}   Bellman-verified={ok}")
