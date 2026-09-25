from fractions import Fraction
from sympy import isprime
def cf(n):
    # 1/(2-3/(3-4/(4-5/(...(n-1)-n/(n+1)))))
    t = Fraction(n+1)
    for k in range(n-1, 1, -1):
        t = k - Fraction(k+1)/t
    return 1/t
vals=[cf(n).denominator for n in range(3,40)]
print(vals)
bad=[]
for n in range(3,1500):
    d=cf(n).denominator
    if d!=1 and not isprime(d): bad.append((n,d))
print("non-1 non-prime denominators:", bad[:10])
print([ (n, cf(n)) for n in range(3,9)])
