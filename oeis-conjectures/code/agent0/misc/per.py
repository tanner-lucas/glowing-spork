from math import comb, factorial
from sympy import totient
N=700
# A064618: Stirling transform of (n!)^2
S=[[1]]
for n in range(1,N+1):
    prev=S[-1]; row=[0]*(n+1)
    for k in range(1,n+1):
        row[k]=(k*(prev[k] if k<len(prev) else 0)) + prev[k-1]
    S.append(row)
a064618=[sum(S[n][k]*factorial(k)**2 for k in range(n+1)) for n in range(N+1)]
assert a064618[:10]==[1,1,5,49,821,21121,775205,38516689,2490976661,203419086241]
# A179929: e.g.f. 3/(1+2e^{-3x}); compute via a(n)=sum_k A123125-type... use recurrence from e.g.f.: A*(1+2e^{-3x}) = 3
# => a(n) + 2*sum_j C(n,j) (-3)^j a(n-j) = 3*[n==0]
a179=[0]*(N+1)
for n in range(N+1):
    s=3 if n==0 else 0
    s-=2*sum(comb(n,j)*(-3)**j*a179[n-j] for j in range(1,n+1))
    assert s%3==0
    a179[n]=s//3
assert a179[:13]==[1,2,2,-6,-30,42,882,954,-39870,-203958,2300562,29677914,-120958110], a179[:13]
# A258899: a(n)=sum_{d|n} 2^d n!/(d!(n/d)!), a(0)=1
from sympy import divisors
a258=[1]+[sum(2**d*factorial(n)//(factorial(d)*factorial(n//d)) for d in divisors(n)) for n in range(1,N+1)]
assert a258[:14]==[1,2,6,10,42,34,786,130,17058,81154,545346,2050,102457218,8194]
def check(seq,name):
    bad=[]
    for k in range(2,101):
        ph=int(totient(k)); start=300
        if any((seq[n+ph]-seq[n])%k for n in range(start,N+1-ph)): bad.append(k)
    print(name,"moduli k<=100 where a(n+phi(k))!=a(n) mod k for n in [300,700]:",bad)
check(a064618,"A064618"); check(a179,"A179929"); check(a258,"A258899")
