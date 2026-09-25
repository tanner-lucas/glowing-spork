from fractions import Fraction as Fr
from math import gcd, factorial
from sympy import factorint, isprime
def cf_den(n):
    t=Fr(-5)
    for j in range(n-1,1,-1):
        t=j-Fr(j+1)/t
    return (1/t).denominator
def closed(n):
    D=n*n+3*n-5
    # gcd(D, 5(n-1)(n-3)!) computed with factorial mod D
    f=1
    for i in range(2,n-2): f=f*i%D
    return D//gcd(D,5*(n-1)*f%D)
data=[13,23,7,49,13,83,103,5,149,1,29,233,53,23,67,373,59,1,499,109,593]
print('data ok', [cf_den(n) for n in range(3,24)]==data)
bad=[n for n in range(3,801) if cf_den(n)!=closed(n)]
print('CF vs closed form mismatches n<=800:',bad)
# valuation formula check to 30000
def vfact(n,p):
    s=0; q=p
    while q<=n: s+=n//q; q*=p
    return s
viol=[]
for n in range(3,30001):
    D=n*n+3*n-5
    a=1
    for p,e in factorint(D).items():
        w=vfact(n-3,p)+ (1 if p==5 else 0)
        m=n-1
        while m%p==0: m//=p; w+=1
        if e>w: a*=p**(e-w)
    if n<=800: assert a==closed(n)
    if a!=1 and not isprime(a) and a!=49: viol.append((n,a))
print('violations (a composite, not 49) n<=30000:',viol)
