from mpmath import mp, mpf, sqrt, floor
from fractions import Fraction
from math import comb
mp.dps=50
# A341239: 1 < r s n - floor(r floor(s n)) < 3
r=1+sqrt(2); s=sqrt(2)
bad=0; lo=10; hi=-10
for n in range(1,200001):
    a=int(floor(r*int(floor(s*n))))
    T=r*s*n-a
    lo=min(lo,T); hi=max(hi,T)
    if not (1<T<3): bad+=1
data=[2,4,9,12,16,19,21,26,28,33,36,38,43,45,50,53,57,60,62,67,70,74,77,79]
assert [int(floor(r*int(floor(s*n)))) for n in range(1,25)]==data
print("A341239 n<=2e5 bad",bad,"range",float(lo),float(hi))
# A374571 mod 2 vs fibbinary
N=1<<14
a=[0]*(N+1); a[0]=1
# A(x)=A(x^2)-x*A(x^2)^2 : compute coefficients iteratively
# coefficient n: [x^n]A(x^2) = a[n/2] if n even; [x^n] x*A(x^2)^2 = [x^(n-1)] A(x^2)^2 = (if n-1 even) sum_{i+j=(n-1)/2} a_i a_j
for n in range(1,N+1):
    v = a[n//2] if n%2==0 else 0
    if (n-1)%2==0:
        m=(n-1)//2
        v -= sum(a[i]*a[m-i] for i in range(m+1))
    a[n]=v
assert a[:26]==[1,-1,-1,2,-1,1,2,-6,-1,5,1,0,2,-8,-6,22,-1,-11,5,-30,1,33,0,0,2,-16]
fib=lambda n: (n & (n>>1))==0
print("A374571 parity mismatches n<=",N,":",sum(1 for n in range(1,N+1) if (a[n]%2==1)!=fib(n)))
# A384819: compute a(n) via Gauss congruence
from sympy import divisors, mobius
M=3000; A=[0]*(M+1)
for n in range(1,M+1):
    S=sum(mobius(n//d)*(d*d-A[d]) for d in divisors(n) if d<n) + n*n  # term d=n has mu(1)=1: n^2 - A[n]
    A[n]=S % n   # need S - A[n] == 0 mod n
data=[0,1,2,1,4,3,6,1,2,7,10,3,12,11,3,1,16,3,18,15,14,19,22,3,4,23,2,27]
assert A[1:29]==data, A[1:29]
from sympy import primerange
bad=[(p,k) for p in primerange(2,M+1) for k in range(1,12) if p**k<=M and A[p**k]!=p-1]
print("A384819 prime-power failures up to",M,":",bad)
# A207969 integrality for k=0..6, 150 terms, via Gauss congruences on b(n)=5F(n)^(2k)
F=[0,1]
for i in range(400): F.append(F[-1]+F[-2])
for k in range(0,8):
    ok=True
    for n in range(1,301):
        S=sum(mobius(n//d)*5*F[d]**(2*k) for d in divisors(n))
        if S%n: ok=False; print("fail k",k,"n",n); break
    print("A207969 k=",k,"Gauss congruences n<=300:",ok)
# A395839 conjectures
cat=[comb(2*n,n)//(n+1) for n in range(3002)]
a3=[10*cat[n+1]-cat[n] for n in range(3000)]
assert a3[:13]==[9,19,48,135,406,1278,4158,13871,47190,163098,571064,2021334,7220988]
print("A395839 parity mism:",sum(1 for n in range(3000) if (a3[n]%2==1)!=((n+1)&n==0)))
print("A395839 mod3 mism:",sum(1 for n in range(999) if not (a3[3*n+1]%3==cat[n]%3 and a3[3*n]%3==0 and a3[3*n+2]%3==0)))
# A143132 finite differences of a(n+4)-a(n)
def a143(n): return (552-1190*n+895*n**2-280*n**3+35*n**4)//12
assert [a143(n) for n in range(1,10)]==[1,6,26,96,321,876,2006,4026,7321]
Q=[a143(n+4)-a143(n) for n in range(1,10)]
d=[Q]; 
for k in range(4): d.append([d[-1][i+1]-d[-1][i] for i in range(len(d[-1])-1)])
print("A143132 Delta^k(a(n+4)-a(n)) at n=1:",[row[0] for row in d], "last digits a(1..4):",[a143(n)%10 for n in range(1,5)])
