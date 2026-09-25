import gmpy2, sys
from gmpy2 import mpz
D = int(sys.argv[1])
bad = []
for d in range(2, D+1):
    lo = mpz(10)**(d-1); hi = lo*10
    best = None
    x = 2
    while True:
        # need x<=y; smallest value with y=x is 2x^x
        if 2*mpz(x)**x >= hi: break
        # smallest y>=x with x^y+y^x >= lo
        # x^y+y^x increasing in y for y>=x>=2
        ylo, yhi = x, x
        while mpz(x)**yhi + mpz(yhi)**x < lo: yhi *= 2
        while ylo < yhi:
            m = (ylo+yhi)//2
            if mpz(x)**m + mpz(m)**x >= lo: yhi = m
            else: ylo = m+1
        y = ylo
        v = mpz(x)**y + mpz(y)**x
        if v < hi and (best is None or v < best[0]): best = (v, x, y)
        x += 1
    if d > 11:
        conj = lo + mpz(d-1)**10
        if best is None or best[0] != conj:
            bad.append((d, best[1:] if best else None))
            print("d=%d: smallest d-digit Leyland is x=%s y=%s, conj value %s d-digit? %s" % (d, best[1] if best else None, best[2] if best else None, "10^(d-1)+(d-1)^10", len(str(conj))==d), flush=True)
    else:
        print(d, best[1:] if best else None)
print("done up to d =", D, "exceptions:", bad)
