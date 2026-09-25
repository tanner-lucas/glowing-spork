from sympy import divisors, mobius
from math import factorial, gcd, prod
import sys
N=int(sys.argv[1])
fact=[1]*(N+1)
for i in range(1,N+1): fact[i]=fact[i-1]*i
def P(n,d):
    m=n//d
    num=fact[n]*prod(1+j*d for j in range(m))
    den=d**m*fact[m]
    assert num%den==0
    return num//den
data=[1,1,4,15,96,455,4320,29295,300160,2663199,36288000,348523175,5748019200,68027248575,1116542242816,16813959537375,334764638208000,4954072089341375,115242726703104000,1966765155600364119,45415699475660800000,930312555383281809375]
res=[]
for n in range(1,N+1):
    a=sum(mobius(d)*P(n,d) for d in divisors(n))
    if n<=len(data): assert a==data[n-1],(n,a)
    if n>3 and a%(n*n-1)!=0: res.append(('div',n))
    if gcd(a,n)!=1: res.append(('gcd',n))
print("data ok; failures up to",N,":",res[:40])
