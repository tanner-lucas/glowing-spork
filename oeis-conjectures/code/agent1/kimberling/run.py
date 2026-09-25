import numpy as np, math, sys
from morph import apply, gen
from mpmath import mp, mpf, sqrt
mp.dps = 40
N = int(sys.argv[1]) if len(sys.argv)>1 else 10**7
def fibword(N):
    w = np.array([0],dtype=np.uint8)
    while len(w) < N: w = apply(w, [[0,1],[0]])
    return w
def data(A):
    for line in open('/home/user/work/oeisdata/seq/%s/%s.seq'%(A[:4],A)):
        if line[:2] in ('%S','%T','%U'): yield from [int(x) for x in line.split(' ',2)[2].strip().strip(',').split(',') if x]
cases = [
 # A-number, images, start, parity, symbol, r (mpf expr), lo, hi, n0 (first index), note
 ('A026367', [[1,1],[1,1,0]], 1, 0, 1, '(1+sqrt(3))/2', -1, 2, 1),
 ('A045672', [[1,1],[1,1,1,0]], 1, 0, 0, '(5+sqrt(17))/2', -1, 3, 1),
 ('A284015', [[1],[1,0,1,0,1]], 1, 0, 1, '(-1+sqrt(17))/2', -1, 2, 1),
 ('A284364u', [[1],[1,0,1,0,1,0]], 1, 0, 0, '(9+sqrt(21))/6', -2, 2, 1),
 ('A284364v', [[1],[1,0,1,0,1,0]], 1, 0, 1, '(-1+sqrt(21))/2', -1, 2, 1),
 ('A284371', [[1],[1,0,0,1]], 1, 0, 1, 'sqrt(3)', -2, 3, 1),
 ('A284655', [[1],[0,1,1,0]], 0, 0, 1, 'sqrt(3)', -1, 2, 1),
 ('A284679', [[1],[0,1,1,1]], 0, 1, 1, '(-1+sqrt(13))/2', -1, 1, 1),
 ('A285035', [[1,0],[0,0,1]], 0, 1, 0, '1+sqrt(mpf(1)/2)', -1, 2, 1),
 ('A285134', [[1,0],[0,0,0,1]], 0, 0, 0, '1+sqrt(mpf(1)/3)', -1, 1, 1),
 ('A285143', [[1,0],[0,0,1,0]], 0, 1, 0, '(3+sqrt(3))/3', -1, 1, 1),
 ('A285276', [[1,0],[0,1,1,1]], 0, 0, 1, 'sqrt(2)', -2, 1, 1),
 ('A285343', [[1,0],[1,0,1,1]], 1, 0, 1, 'sqrt(2)', -1, 1, 1),
 ('A285360', [[1,0],[1,1,0,1]], 1, 0, 1, 'sqrt(2)', 0, 2, 1),
 ('A285422', [[1,1],[0,1,1]], 0, 1, 0, '2+sqrt(3)', -1, 5, 1),
 ('A287727', None, None, None, 1, '(15-sqrt(5))/10', -1, 1, 1),
]
for (A, imgs, start, par, sym, rexpr, lo, hi, n0) in cases:
    if A == 'A287727':
        f = fibword(N)
        w = apply(f, [[1],[0,1,1]])[:N]
    else:
        # starting from 0 always like the Mathematica programs; parity of iteration count
        w = gen(imgs, 0, par, N)
    pos = np.nonzero(w == sym)[0] + 1  # 1-based positions
    base = A[:7]
    try:
        S = list(data(base))
    except Exception as e:
        S = None
    if base == 'A045672':
        S = S[1:]  # a(0)=0 then positions for n>=1
    if base in ('A284364',):
        # check the word itself
        ok = list(w[:len(S)]) == S
    else:
        ok = list(pos[:len(S)]) == S
    r = float(eval(rexpr, {'sqrt':sqrt,'mpf':mpf}))
    n = np.arange(1, len(pos)+1, dtype=np.float64)
    d = n*r - pos
    imin, imax = int(np.argmin(d)), int(np.argmax(d))
    print("%-9s data_ok=%s  #terms=%d  min=%.6f at n=%d  max=%.6f at n=%d   conj (%g,%g)  %s" % (A, ok, len(pos), d[imin], imin+1, d[imax], imax+1, lo, hi, "VIOLATION?" if (d[imin] <= lo or d[imax] >= hi) else ""))
    sys.stdout.flush()
