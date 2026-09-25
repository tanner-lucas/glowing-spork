import gmpy2, time
from gmpy2 import mpz, powmod
for (n,m) in [(209,207),(157169,157167)]:
    t=time.time()
    p=mpz(3)*(mpz(2)**n)+1
    e=mpz(2)**m
    r2=powmod(2,e,p); r3=powmod(3,e,p)
    print(f"p=3*2^{n}+1: 2^(2^{m}) == -1 mod p: {r2==p-1};  3^(2^{m}) == -1 mod p: {r3==p-1};  BPSW prp: {gmpy2.is_prime(p,1) if n<5000 else 'skipped'}  [{time.time()-t:.1f}s]",flush=True)
