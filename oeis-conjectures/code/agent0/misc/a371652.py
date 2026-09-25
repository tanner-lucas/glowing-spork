from math import comb
from fractions import Fraction
N=1500
S=0; bad=[]
data=[1,3,29,399,6514,117711,2275251,46139015,969837866,20962468086]
for n in range(1,N+1):
    k=n-1
    t=(145*k*k+104*k+18)*comb(2*k,k)*comb(3*k,k)**2
    assert t%(2*k+1)==0 or True
    S+=Fraction(t,2*k+1)
    val=S/(6*n*(2*n-1)*comb(3*n,n))
    if n<=len(data): assert val==data[n-1],(n,val)
    if val.denominator!=1: bad.append(n)
print("A371652 non-integers up to",N,":",bad[:20])
