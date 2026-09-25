from fractions import Fraction
from math import gcd, factorial
def cf(n):
    y=Fraction(n+1)
    for j in range(n-1,1,-1):
        y = j - Fraction(j+1)/y
    return 1/y
data=[5,7,3,11,13,1,17,19,1,23,1,1,29,31,1,1,37,1,41,43,1,47,1,1,53,1,1,59,61,1,1,67,1,71,73,1,1,79,1,83,1,1,89,1,1,1,97,1,101,103,1,107,109,1,113,1,1,1,1,1,1,127,1,131,1,1,137,139,1,1,1,1,149,151,1,1,157,1,1,163,1,167]
ok=True
for n in range(3,400):
    v=cf(n)
    den=v.denominator
    m=2*n-1
    pred = m//gcd(m, factorial(n-2))
    # closed form check: value = ( m*sum_{k=0}^{n-3} k! + n*(n-2)! ) / (2*m) ?
    cand = Fraction(m*sum(factorial(k) for k in range(n-2)) + n*factorial(n-2), 2*m)
    if n-3 < len(data) and data[n-3]!=den: ok=False; print("data mismatch",n)
    if den!=pred: ok=False; print("pred mismatch", n, den, pred)
    if v!=cand: print("closed form differs", n, v, cand); break
print("ok",ok)
print([ (n,cf(n)) for n in range(3,9)])
