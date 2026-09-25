import numpy as np
from morph import apply, gen
from math import sqrt
N = 30000000
w = gen([[1],[1,0,1,0,1,0]], 0, 0, N)
print("prefix", ''.join(map(str,w[:40])))
r = (9+sqrt(21))/6; s = (-1+sqrt(21))/2
for sym, c, lo, hi, name in [(0, r, -2, 2, 'A284365 (positions of 0)'), (1, s, -1, 2, 'A284366 (positions of 1)')]:
    pos = np.nonzero(w==sym)[0]+1
    n = np.arange(1, len(pos)+1, dtype=np.float64)
    d = n*c - pos
    bad = np.nonzero((d <= lo+1e-9) | (d >= hi-1e-9))[0]
    print(name, "count of violations (incl. within 1e-9) up to position", N, ":", len(bad))
    for i in bad[:10]:
        print("   n=%d a(n)=%d  n*c-a(n)=%.9f" % (i+1, pos[i], d[i]))
