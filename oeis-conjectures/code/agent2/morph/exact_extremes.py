# Exact extremes of n*r - a(n) for positions a(n) of letter t in the fixed point of a 2-letter Pisot substitution,
# via the Dumont-Thomas prefix automaton.  Value(N) = r*Delta_t(N), Delta_t(N) = |u[1..N]|_t - f_t*N, u_N = t.
import mpmath as mp
mp.mp.dps=50
def analyze(i0,i1,start,power,t,K=400):
    img={0:i0,1:i1}
    def app(w): return "".join(img[int(c)] for c in w)
    tau={c: str(c) for c in (0,1)}
    for _ in range(power): tau={c: app(tau[c]) for c in (0,1)}
    assert tau[start][0]==str(start)
    M=mp.matrix([[tau[0].count('0'),tau[1].count('0')],[tau[0].count('1'),tau[1].count('1')]])
    E,ER=mp.eig(M)
    idx=max(range(2),key=lambda i: mp.re(E[i])); l1=mp.re(E[idx]); l2=mp.re(E[1-idx])
    v=[mp.re(ER[0,idx]),mp.re(ER[1,idx])]; f=[v[0]/(v[0]+v[1]), v[1]/(v[0]+v[1])]
    ft=f[t]; r=1/ft
    def delta(p): return p.count(str(t)) - ft*len(p)
    edges={c:[(tau[c][:j],int(tau[c][j])) for j in range(len(tau[c]))] for c in (0,1)}
    INF=mp.mpf('1e100')
    mn={c:(0 if c==t else INF) for c in (0,1)}; mx={c:(0 if c==t else -INF) for c in (0,1)}
    hist=[]
    for j in range(1,K+1):
        w=l2**(j-1)
        mn={c:min(w*delta(p)+mn[d] for p,d in edges[c]) for c in (0,1)}
        mx={c:max(w*delta(p)+mx[d] for p,d in edges[c]) for c in (0,1)}
        hist.append((r*(mn[start]+1-ft), r*(mx[start]+1-ft)))
    return l1,l2,r,hist
import sys
cases=[("A026368","11","110",1,1,0,-2,4),("A283963u","1","1010",1,1,0,-1,2),("A283963v","1","1010",1,1,1,-1,2),
 ("A284365","1","101010",1,1,0,-2,2),("A284366","1","101010",1,1,1,-1,2),("A284386u","1","1101",1,1,0,0,2),("A284386v","1","1101",1,1,1,-1,1),
 ("A284505u","1","1100",1,1,0,-3,4),("A284505v","1","1100",1,1,1,-2,4),("A284657","1","0110",1,2,0,-1,3),("A284752","01","0001",0,1,0,-1,3),
 ("A284852","01","0100",0,1,0,-2,2),("A285036","10","001",1,2,1,-1,2),("A285135","10","0001",0,2,1,-1,1),("A285144","10","0010",1,2,1,-1,mp.sqrt(3)),
 ("A285206","10","0100",0,2,0,-1,1),("A285278","10","0111",1,2,0,0,6),("A285374","10","1110",1,1,0,-4,1),("A285423","11","011",1,2,1,-2,2)]
for (aid,i0,i1,st,pw,t,lo,hi) in cases:
    l1,l2,r,h=analyze(i0,i1,st,pw,t)
    inf_,sup_=h[-1]
    verdict = "HOLDS" if (inf_>lo and sup_<hi) else ("inf==lo?" if abs(inf_-lo)<mp.mpf('1e-30') and sup_<hi else "FAILS")
    print(f"{aid:9s} l2={mp.nstr(l2,6):9s} r={mp.nstr(r,10):12s} inf={mp.nstr(inf_,20):24s} sup={mp.nstr(sup_,20):24s} bounds=({mp.nstr(lo,6)},{mp.nstr(hi,6)}) {verdict}")
