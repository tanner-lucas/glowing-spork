# Rigorous check of P. Bala's conjectures that a(n/2) is an integer (fractional factorials via Gamma).
# a(n/2) = prod_i ((k_i*n/2)!)^{e_i}
from fractions import Fraction
from math import factorial, lcm, log2, floor
cases = {
 "A061164": [(20,1),(1,1),(10,-1),(7,-1),(4,-1)],
 "A295454": [(30,1),(9,1),(5,1),(18,-1),(15,-1),(10,-1),(1,-1)],
 "A295468": [(30,1),(5,1),(3,1),(2,1),(15,-1),(10,-1),(8,-1),(6,-1),(1,-1)],
 "A295481": [(24,1),(4,1),(3,1),(12,-1),(9,-1),(8,-1),(2,-1)],
}
def s2(x): return bin(x).count("1")
def exact_value(ke,n):
    # returns Fraction value of a(n/2) divided by sqrt(pi)^{sum e over half-integer args}; also that exponent
    val=Fraction(1); spi=0
    for k,e in ke:
        if (k*n)%2==0:
            f=Fraction(factorial(k*n//2))
        else:
            M=k*n  # x = M/2, x! = M! sqrt(pi)/(2^M ((M-1)/2)!)
            f=Fraction(factorial(M), 2**M*factorial((M-1)//2)); spi+=e
        val*= f**e
    return val,spi
for name,ke in cases.items():
    K=[k for k,e in ke]; L=lcm(*K)
    bal=sum(k*e for k,e in ke); half=sum(e for k,e in ke if k%2)
    # Landau for integer case (n even): Psi(y)=sum e*floor(k*y), y=j/L
    psi_min=min(sum(e*((k*j)//L) for k,e in ke) for j in range(L))
    # odd n, odd primes: Phi(y) = sum_{k even} e floor(k y) + sum_{k odd} e floor(k y + 1/2), y=j/(2L)
    phi_min=min(sum(e*((k*j)//(2*L)) if k%2==0 else e*((k*j+L)//(2*L)) for k,e in ke) for j in range(2*L))
    # p=2, odd n: V(n) = n*sum_{k even} e*k - sum_{k even} e*s2(k*n/2)
    c=sum(e*k for k,e in ke if k%2==0)
    # bound: sum_{k even,e>0} e*s2(kn/2) <= sum e*(log2(k n/2)+1); find N0 with c*n > that
    N0=1
    while not (c*N0 > sum(e*(log2(k*N0/2)+1) for k,e in ke if k%2==0 and e>0) and c>0): 
        N0+=1
        if N0>10**6: break
    v2min=min(c*n - sum(e*s2(k*n//2) for k,e in ke if k%2==0) for n in range(1,max(N0,2000)+1,2))
    # brute-force exact integrality for n up to 300
    ok=True
    for n in range(0,301):
        v,spi=exact_value(ke,n)
        if spi!=0 or v.denominator!=1: ok=False; print(name,"FAIL at n=",n,v,spi); break
    print(f"{name}: balance={bal} sqrtpi-exponent={half} Landau(int) min={psi_min} Phi(half,odd p) min={phi_min} c={c} N0={N0} min v2 over odd n<=max(N0,2000)={v2min} exact n<=300 integral={ok}")
