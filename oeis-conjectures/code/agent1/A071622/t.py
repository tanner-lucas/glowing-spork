import gmpy2, math, sys
from gmpy2 import mpz
N=int(sys.argv[1])
p4=mpz(1); p3=mpz(1); s=0; out=[]; viol=[]; minratio=(10**9,0)
for k in range(1,N+1):
    p4*=4; p3*=3
    f = p4//p3
    s += -1 if (f & 1)==0 else 1   # a(n) = -sum (-1)^floor  : even floor -> -1, odd -> +1
    if k<=34: out.append(s)
    if k>2300:
        L = math.log(k)**2
        if s <= L: viol.append((k,s,L))
        if s - L < minratio[0]: minratio=(s-L,k,s)
print(out)
print("N=",N,"a(N)=",s,"violations:",len(viol),viol[:10], "min a(n)-log(n)^2 over n>2300:",minratio)
