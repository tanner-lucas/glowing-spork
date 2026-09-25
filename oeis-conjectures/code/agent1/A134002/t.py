from math import isqrt
from sympy import isprime
def term(n):
    T=n*(n+5)
    for a in range(1, n):
        r=T-a*(a+5)
        if r<6: break
        # b(b+5)=r -> b = (-5+sqrt(25+4r))/2
        d=25+4*r; s=isqrt(d)
        if s*s==d and (s-5)%2==0 and (s-5)//2>=1: return True
    return False
N=3000
terms=[n for n in range(1,N+1) if term(n)]
print(terms[:23])
pred=[n for n in range(1,N+1) if n%5==0 or not isprime(n*n+(n+5)**2)]
print("terms == {n: 5|n or n^2+(n+5)^2 composite} for n<=%d:"%N, terms==pred)
