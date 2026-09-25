import sys
from sympy import prime
X=10**int(sys.argv[1])
P=[prime(i) for i in range(1,60)]
items=[]  # (m, tau, omega)
def rec(i, m, maxe, tau, om):
    items.append((m,tau,om))
    p=P[i]; v=m; e=0
    while e<maxe:
        v*=p; e+=1
        if v>X: break
        rec(i+1, v, e, tau*(e+1), om+1)
rec(0,1,200,1,0)
items.sort()
print("A025487 elements <= X:",len(items))
# HCN: records of tau; A059992: records of tau-omega
best_tau=0; best_d=-1; hcn=[]; rec_d=set()
for m,t,o in items:
    if t>best_tau: best_tau=t; hcn.append(m)
    if t-o>best_d: best_d=t-o; rec_d.add(m)
data59992=[1,4,8,12,24,36,48,60,72,120,180,240,360,720,840,1080,1260,1440,1680]
assert sorted(rec_d)[:len(data59992)]==data59992, sorted(rec_d)[:20]
hcn_data=[1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,1680,2520,5040]
assert hcn[:len(hcn_data)]==hcn_data
miss=[h for h in hcn if h not in rec_d]
print("HCNs up to 10^%s:"%sys.argv[1], len(hcn), " HCNs not in A059992:", miss[:20])
from sympy import factorint
tau={m:t for m,t,o in items}; om={m:o for m,t,o in items}
marg=[(tau[hcn[i]]-tau[hcn[i-1]]-om[hcn[i]], hcn[i]) for i in range(1,len(hcn))]
print("min margins (tau(h)-tau(prev)-omega(h)):", sorted(marg)[:8])
print("last margins:", [m for m,h in marg[-10:]])
