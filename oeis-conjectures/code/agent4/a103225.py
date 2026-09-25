import math
from math import isqrt
from sympy import isprime
def N(r):  # number of (x,y) with x^2+y^2 < r^2
    s=0
    R=r*r-1
    for x in range(-r+1,r):
        s+=2*isqrt(R-x*x)+1
    return s
res=[]
for p in range(3,20000,4):
    if isprime(p):
        a=N(p)-1
        d=a-math.pi*p*p
        if d>0: res.append((p,a,d))
print(len(res)); print(res[:10])
