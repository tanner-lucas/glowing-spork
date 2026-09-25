import mpmath as mp
mp.mp.dps=50
def s(m): return mp.zeta(3, m+1)   # zeta(3)-H3(m)
bad=[]; minmargin=[]
for n in range(1,5001):
    a=int(mp.floor(n/mp.sqrt(2)+mp.mpf(1)/2))   # round(n/sqrt2)
    lo=s(a); hi=s(a-1); t=mp.mpf(1)/n**2
    if not (lo<t<hi): bad.append(n)
    if n<=40: minmargin.append((n, mp.nstr((hi-t)*n**2,5), mp.nstr((t-lo)*n**2,5)))
print("violations n<=5000:",bad)
print(minmargin)
# Beatty positions check
import math
N=10**6
A=[int(mp.floor(n/mp.sqrt(2)+0.5)) for n in range(0,2000)]
ones=[n for n in range(0,1999) if A[n+1]-A[n]==1]; zeros=[n for n in range(0,1999) if A[n+1]-A[n]==0]
b53=[int(mp.floor((j+mp.mpf(1)/2)*mp.sqrt(2))) for j in range(0,1500)]
b54=[int(mp.floor((j+mp.mpf(1)/2)*(2+mp.sqrt(2)))) for j in range(0,700)]
print("diffs in {0,1}:", all(A[n+1]-A[n] in (0,1) for n in range(1999)))
print("ones==A001953 prefix:", ones==[b for b in b53 if b<1999], " zeros==A001954 prefix:", zeros==[b for b in b54 if b<1999])
