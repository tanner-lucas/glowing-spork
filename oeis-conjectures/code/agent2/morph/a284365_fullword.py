# Third check: build the word by full iteration (like the Mathematica code in A284364) and read positions of 0.
import numpy as np
from math import isqrt
tab={48:b'1',49:b'101010'}
w=b'1'
while len(w)<25_000_000:
    w=b''.join(tab[c] for c in w)
arr=np.frombuffer(w,dtype=np.uint8)
zeros=np.flatnonzero(arr==48)+1   # 1-indexed positions of 0
n=8933313
an=int(zeros[n-1])
print("A284365(%d) = %d"%(n,an))
# exact test: n*(9+sqrt21)/6 - an >= 2  <=> n*sqrt21 >= 6*(an+2)-9n
R=6*(an+2)-9*n
print("R =",R," 21 n^2 - R^2 =",21*n*n-R*R, "->", "violation (>=2)" if (R<=0 or 21*n*n>=R*R) else "ok")
# also first violation index among n <= len(zeros)
ns=np.arange(1,len(zeros)+1,dtype=np.float64)
d=ns*(9+np.sqrt(21))/6-zeros
idx=np.flatnonzero(d>=2-1e-6)
print("first n with d>=2-1e-6 (float prefilter):", idx[:3]+1, "max d:",d.max(), "at n=",int(d.argmax())+1, " min d:", d.min())
