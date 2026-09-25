# Exact extremal discrepancy for positions of letter c in tau(w), w = lim sigma^K(start) (binary sigma).
import mpmath as mp
from fractions import Fraction as Fr
from qs import QS, sqfree
import math
mp.mp.dps=80
def apply(sig,word): return ''.join(sig[int(ch)] for ch in word)
def power_images(sig,L):
    out=[]
    for a in '01':
        w=a
        for _ in range(L): w=apply(sig,w)
        out.append(w)
    return out
class Problem:
    def __init__(s, s0, s1, t0='0', t1='1', start=0, K=20, c=0):
        s.sig=[s0,s1]; s.tau=[t0,t1]; s.start=start; s.K=K; s.c=c
        M=[[s0.count('0'),s1.count('0')],[s0.count('1'),s1.count('1')]]
        s.M=M
        tr=M[0][0]+M[1][1]; det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
        disc=tr*tr-4*det
        f,d=sqfree(disc) if disc>0 else (0,1)
        assert disc>0
        if d==1: raise ValueError("rational eigenvalues")
        s.d=d
        s.l1=QS(Fr(tr,2),Fr(f,2),d); s.l2=QS(Fr(tr,2),Fr(-f,2),d)
        # right Perron eigenvector v: (M - l1) v = 0
        if M[0][1]!=0: v=[QS(M[0][1],0,d), s.l1-M[0][0]]
        else: v=[s.l1-M[1][1], QS(M[1][0],0,d)]
        s.v=v
        L=v[0]*len(t0)+v[1]*len(t1); Cc=v[0]*t0.count(str(c))+v[1]*t1.count(str(c))
        s.r=L/Cc
        s.htau=[s.r*s.tau[a].count(str(c))-len(s.tau[a]) for a in (0,1)]
        # check left-eigen property
        for a in (0,1):
            img=s.sig[a]; val=sum((s.htau[int(ch)] for ch in img), QS(0,0,d))
            assert val==s.l2*s.htau[a], "h not l2-eigen"
        # root and period: first-letter map
        fl=lambda a: int(s.sig[a][0])
        x=start
        for _ in range(K): x=fl(x)
        s.b=x; p=1; y=fl(x)
        while y!=x: y=fl(y); p+=1
        s.p=p
        s.pisot = abs(s.l2.mpf())<1
        # L: multiple of p with l2^L>0
        Lm=p
        if s.l2.sign()<0 and Lm%2==1: Lm*=2
        s.L=Lm
    def h_word(s,word): return sum((s.htau[int(ch)] for ch in word), QS(0,0,s.d))
    def bottom(s,e):
        out=[]
        te=s.tau[e]
        for j,ch in enumerate(te):
            if ch==str(s.c):
                u=te[:j]
                out.append(s.r*u.count(str(s.c))-len(u)+s.r-1)
        return out
    def exact_extremes(s):
        # Bellman on sigma^L with discount mu=l2^L>0
        d=s.d; mu=QS(1,0,d)
        for _ in range(s.L): mu=mu*s.l2
        s.mu=mu
        imgs=power_images(s.sig,s.L)
        edges=[]  # (e_from, j, e_to, cost)
        for ep in (0,1):
            for j,ch in enumerate(imgs[ep]):
                edges.append((ep,j,int(ch),s.h_word(imgs[ep][:j])))
        res={}
        for mode in ('min','max'):
            better=(lambda x,y: x<y) if mode=='min' else (lambda x,y: x>y)
            # initial policy via float value iteration
            W=[mp.mpf(0),mp.mpf(0)]
            for it in range(3000):
                W2=[None,None]
                for (ep,j,e,cst) in edges:
                    val=cst.mpf()+mu.mpf()*W[ep]
                    if W2[e] is None or (val<W2[e] if mode=='min' else val>W2[e]): W2[e]=val
                W=W2
            pol=[None,None]
            for (ep,j,e,cst) in edges:
                val=cst.mpf()+mu.mpf()*W[ep]
                if pol[e] is None or (val<pol[e][0] if mode=='min' else val>pol[e][0]): pol[e]=(val,ep,j,cst)
            # policy iteration exact
            for it in range(50):
                # solve W(e) = c(e) + mu W(pi(e))
                c0,c1=pol[0][3],pol[1][3]; p0,p1=pol[0][1],pol[1][1]
                # linear system A W = c ; A = I - mu P
                A=[[QS(1,0,d),QS(0,0,d)],[QS(0,0,d),QS(1,0,d)]]
                A[0][p0]=A[0][p0]-mu; A[1][p1]=A[1][p1]-mu
                det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
                W0=(c0*A[1][1]-A[0][1]*c1)/det; W1=(A[0][0]*c1-A[1][0]*c0)/det
                We=[W0,W1]
                changed=False
                for (ep,j,e,cst) in edges:
                    val=cst+mu*We[ep]
                    if better(val,We[e]):
                        pol[e]=(None,ep,j,cst); We[e]=val; changed=True
                        break
                if not changed: break
            else: raise RuntimeError("policy iteration did not converge")
            # combine with bottom
            best=None; arg=None
            for e in (0,1):
                for bv in s.bottom(e):
                    val=bv+We[e]
                    if best is None or better(val,best): best=val; arg=(e,pol[e][1],pol[e][2])
            res[mode]=(best,We,[(pol[e][1],pol[e][2]) for e in (0,1)])
        return res
    # ---------- finite-depth DP (float) and DFS for first violation ----------
    def gen_prefix(s, T):
        w=str(s.b)
        for _ in range(T): w=apply(s.sig,w)
        return w
    def first_violation_dfs(s, lo, hi, maxT=400, strict=False):
        """Find smallest n with D(n) not in (lo,hi) using exact-finite-depth DP pruning. lo,hi: QS or None."""
        d=s.d; mp_lo = lo.mpf() if lo is not None else mp.mpf(-10)**30; mp_hi = hi.mpf() if hi is not None else mp.mpf(10)**30
        r=s.r.mpf(); ht=[x.mpf() for x in s.htau]; c=str(s.c)
        # G[t][a] = (min,max) of D-values over prefixes of sigma^t(a) followed by c (within), as offsets (+ r - 1 included)
        G=[[None,None]]
        for a in (0,1):
            vals=[x.mpf() for x in s.bottom(a)]
            G[0][a]=(min(vals),max(vals)) if vals else (mp.inf,-mp.inf)
        l2=s.l2.mpf()
        wt=[ht[:]]  # wt[t][a] = h_tau(sigma^t(a))
        for t in range(1,maxT+1):
            row=[None,None]
            for a in (0,1):
                mn=mp.inf; mx=-mp.inf; acc=mp.mpf(0)
                for ch in s.sig[a]:
                    e=int(ch)
                    gmn,gmx=G[t-1][e]
                    if gmn<mn: mn=acc+gmn if acc+gmn<mn else mn
                    if acc+gmx>mx: mx=acc+gmx
                    if acc+gmn<mn: mn=acc+gmn
                    acc+=wt[t-1][e]
                row[a]=(mn,mx)
            G.append(row); wt.append([sum(wt[t-1][int(ch)] for ch in s.sig[a]) for a in (0,1)])
        # choose top level T (multiple of p) where violation exists
        eps=mp.mpf(10)**-60
        if strict: eps=-mp.mpf(10)**-50
        Ttop=None
        for t in range(0,maxT+1,s.p):
            mn,mx=G[t][s.b]
            if mn<mp_lo+eps or mx>mp_hi-eps: Ttop=t; break
        if Ttop is None: return None
        # counts
        lens=[[len(s.tau[a]) for a in (0,1)]]; cnts=[[s.tau[a].count(c) for a in (0,1)]]
        for t in range(1,Ttop+1):
            lens.append([sum(lens[t-1][int(ch)] for ch in s.sig[a]) for a in (0,1)])
            cnts.append([sum(cnts[t-1][int(ch)] for ch in s.sig[a]) for a in (0,1)])
        # DFS
        def dfs(t,a,V,P,Ncnt):
            gmn,gmx=G[t][a]
            if V+gmn>mp_lo+eps and V+gmx<mp_hi-eps: return None
            if t==0:
                te=s.tau[a]
                for j,ch in enumerate(te):
                    if ch==c:
                        u=te[:j]; val=V+r*u.count(c)-len(u)+r-1
                        if val<mp_lo+eps or val>mp_hi-eps:
                            return (Ncnt+u.count(c)+1, P+j+1, val)
                return None
            acc=mp.mpf(0); PP=P; NN=Ncnt
            for ch in s.sig[a]:
                e=int(ch)
                res=dfs(t-1,e,V+acc,PP,NN)
                if res: return res
                acc+=wt[t-1][e]; PP+=lens[t-1][e]; NN+=cnts[t-1][e]
            return None
        import sys; sys.setrecursionlimit(10000)
        return dfs(Ttop,s.b,mp.mpf(0),0,0)
