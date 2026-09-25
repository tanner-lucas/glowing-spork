import numpy as np
from morph import apply, gen
from math import sqrt
for A, imgs, par, r, lo, hi in [('A285134', [[1,0],[0,0,0,1]], 0, 1+sqrt(1/3), -1, 1), ('A285143', [[1,0],[0,0,1,0]], 1, (3+sqrt(3))/3, -1, 1)]:
    w = gen(imgs, 0, par, 2000)
    pos = np.nonzero(w==0)[0]+1
    viol = [(n, p, n*r-p) for n,p in enumerate(pos, start=1) if not (lo < n*r-p < hi)]
    print(A, "first 50 terms:", list(pos[:50]))
    print(A, "first violations:", viol[:8])
