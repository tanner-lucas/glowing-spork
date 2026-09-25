from mpmath import mp, mpf, sqrt, floor, frac
mp.dps=40
s=sqrt(2)
for name, r, lo, hi in [('A341249', 2+sqrt(2), 1, 2), ('A341239', 1+sqrt(2), 1, 3)]:
    vals=[]; bad=[]; mn=10; mx=-10
    for n in range(1,20001):
        a = int(floor(r*floor(s*n)))
        if n<=12: vals.append(a)
        d = r*s*n - a
        mn=min(mn,d); mx=max(mx,d)
        if not (lo < d < hi): bad.append(n)
        f = frac(s*n)
        pred = 2*f+1 if f < 1/sqrt(2) else 2*f+2
        if name=='A341239': pred = f+1 if f < 1/sqrt(2) else f+2
        assert abs(pred-d) < mpf(10)**-20, (name,n)
    print(name, vals, "range [%.6f, %.6f]"%(mn,mx), "violations:", len(bad), bad[:6])
