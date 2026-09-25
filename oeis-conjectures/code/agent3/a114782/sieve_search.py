import gmpy2, sys, numpy as np
from gmpy2 import mpz
from sympy import primerange
U=[2971, 9811, 15817, 20089, 25609, 28909, 33331, 35311, 35839, 37159, 37357]
K0,K1=1001,int(sys.argv[1]) if len(sys.argv)>1 else 8000
Q=np.array([q for q in primerange(7,200000)],dtype=np.int64)
for p in U:
    alive=np.ones(K1+1,dtype=bool)
    t=np.ones_like(Q)            # 10^k mod q
    pm=p%Q
    for k in range(K1+1):
        if k>=K0 and np.any((t+pm)%Q==0): alive[k]=False
        t=(t*10)%Q
    found=0; tested=0
    for k in range(K0,K1+1):
        if alive[k]:
            tested+=1
            if gmpy2.is_prime(mpz(10)**k+p, 2): found=k; break
    print(p,"first k in [%d,%d] with 10^k+p PRP:"%(K0,K1),found,"(PRP tests:",tested,")",flush=True)
