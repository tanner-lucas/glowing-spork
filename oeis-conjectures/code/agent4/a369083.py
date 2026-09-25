# a(n) mod 2 for A(x) = 1 + x*(E^2+O^2) + 3x*E*O  (E,O = even/odd parts of A), exact integer recurrence check first
import sys
N=int(sys.argv[1])
# exact integers for small N to reproduce data
def exact(N):
    a=[1]+[0]*N
    for n in range(1,N+1):
        m=n-1; s=0
        for i in range(0,m+1):
            j=m-i; ai=a[i]; aj=a[j]
            if i%2==0 and j%2==0: s+=ai*aj
            elif i%2==1 and j%2==1: s+=ai*aj
            else: s+=3*ai*aj if i%2==0 else 0  # E*O term counted once per (even i, odd j) pair; times 3 -> handle below
        # E*O: sum over (i even, j odd) and (i odd, j even)?? E*O coefficient at m = sum_{i even, j odd, i+j=m} a_i a_j (single product)
        a[n]=s
    return a
# careful derivation: [x^m](E^2+O^2) = sum_{i+j=m, i,j same parity} a_i a_j ; [x^m](E*O) = sum_{i even, j odd, i+j=m} a_i a_j
def exact2(N):
    a=[1]+[0]*N
    for n in range(1,N+1):
        m=n-1; same=0; eo=0
        for i in range(m+1):
            j=m-i
            if (i-j)%2==0: same+=a[i]*a[j]
            elif i%2==0: eo+=a[i]*a[j]
        a[n]=same+3*eo
    return a
print(exact2(12))
# mod 2 fast with python ints as bitsets
import numpy as np
a=np.zeros(N+1,dtype=np.uint8); a[0]=1
# O(N^2) with numpy dot per step
bad=[]
for n in range(1,N+1):
    m=n-1
    x=a[:m+1]; y=x[::-1]
    idx=np.arange(m+1)
    # same parity pairs: i and m-i same parity iff m even; then all pairs are same parity
    if m%2==0:
        v=int(np.dot(x.astype(np.int64),y.astype(np.int64)))&1
    else:
        # all pairs mixed parity; E*O counts pairs with i even: 3*sum_{i even} a_i a_{m-i}
        v=int(np.dot(x[0::2].astype(np.int64), y[0::2].astype(np.int64)))&1
    a[n]=v
    from math import comb
    b=1 if (n & (3*n+3))==0 else 0
    if v!=b: bad.append(n)
print('mismatches with binomial(4n+3,n) mod 2 for n<=%d:'%N, bad[:20])
