from fractions import Fraction
from math import comb, factorial
from sympy import bernoulli, factorint
# A305214: residues not sums of two cubes mod n nonzero iff 7|n or 9|n
bad=0
for n in range(1,3001):
    cubes=sorted({pow(x,3,n) for x in range(n)})
    S=set()
    for c in cubes:
        for d in cubes: S.add((c+d)%n)
    if (len(S)<n)!=(n%7==0 or n%9==0): bad+=1; print("A305214 fail",n)
print("A305214 n<=3000 bad",bad)
# A195986
print("A195986 bad", sum(1 for n in range(1,3000) if ((5**n-3**n)&-(5**n-3**n)).bit_length()-1 != (1 if n%2 else ((3**n-1)&-(3**n-1)).bit_length()-1+1)))
# A160627
bad=0
for n in range(0,400):
    L=sum(Fraction(comb(n,k)*(-4)**k, factorial(k)) for k in range(n+1))
    if L.numerator%2==0: bad+=1
print("A160627 n<400 even numerators:",bad)
# A363151 cubefree: B_j(1) = B_j except B_1(1)=+1/2
def B1(j):
    b=bernoulli(j)
    return Fraction(1,2) if j==1 else Fraction(int(b.p),int(b.q))
Bs=[B1(j) for j in range(301)]
bad=0
for n in range(0,301):
    s=sum(Bs[j]*Bs[n-j] for j in range(n+1))
    if s.denominator>1 and max(factorint(s.denominator).values())>=3: bad+=1
print("A363151 n<=300 non-cubefree:",bad)
