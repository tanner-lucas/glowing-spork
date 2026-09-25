import mpmath as mp
mp.mp.dps=60
def s(m): return mp.zeta(3, m+1)   # zeta(3) - H^{(3)}_m
# Pell solutions p^2-2n^2=+-1
P=[(1,1),(3,2)]
while len(P)<30: p,n=P[-1]; P.append((p+2*n,p+n))
for p,n in P[:26]:
    a=int(mp.nint(n/mp.sqrt(2)))
    lo=s(a)*n**2; hi=s(a-1)*n**2
    print(n, p*p-2*n*n, a, lo<1<hi, mp.nstr(1-lo,6), mp.nstr(hi-1,6), mp.nstr((1-lo)*n**4,8), mp.nstr((hi-1)*n**4,8))
