# exact test for a covering with period L by primes dividing 10^L-1:
# class r mod L is covered iff gcd(10^r + p, 10^L - 1) > 1.
import gmpy2, sys
from gmpy2 import mpz
U=[48247,2971, 9811, 15817, 20089, 25609, 28909, 33331, 35839]
LMAX=int(sys.argv[1])
for p in U:
    res=None
    for L in range(1,LMAX+1):
        M=mpz(10)**L-1
        ok=True
        t=mpz(1)
        for r in range(L):
            if gmpy2.gcd(t+p,M)==1: ok=False; break
            t*=10
        if ok: res=L; break
    print(p,"smallest covering period L<=%d:"%LMAX,res,flush=True)
