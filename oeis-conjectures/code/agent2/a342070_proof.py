# Proof that 1323 is the last term of A342070: k with pi(3k)-pi(2k) > pi(2k)-pi(k).
import numpy as np, sympy as sp, mpmath as mp
# Part 1: exhaustive check for k <= K1 = 400000 (covers k < 355991)
K1=400000; M=3*K1+10
sieve=np.ones(M+1,dtype=bool); sieve[:2]=False
for i in range(2,int(M**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
pi=np.cumsum(sieve)
ks=np.arange(1,K1+1)
D=pi[3*ks]-2*pi[2*ks]+pi[ks]
terms=list(ks[D>0])
S=open('/home/user/work/oeisdata/seq/A342/A342070.seq').read()
data=[int(x) for x in "".join(l[11:] for l in S.splitlines() if l[:2] in('%S','%T','%U')).replace('\n','').split(',') if x.strip()]
print("terms found <= %d:"%K1, len(terms), "last:", terms[-1], " matches OEIS data:", terms[:len(data)]==data, len(data))
# Part 2: analytic inequality for k >= 355991 using
#  pi(x) <= x/L(1+1/L+2.51/L^2), x>=355991 (Dusart 1999);  pi(x) >= x/L(1+1/L+2/L^2), x>=88783 (Dusart 2010).
# Need U(3k)+U(k) < 2*Lo(2k).  Divide by k; with L=ln k, a=ln2, b=ln3:
L=sp.symbols('L',positive=True); a=sp.log(2); b=sp.log(3)
def U(t,lt): return t/lt*(1+1/lt+sp.Rational(251,100)/lt**2)
def Lo(t,lt): return t/lt*(1+1/lt+2/lt**2)
h = 2*Lo(2,L+a) - U(3,L+b) - U(1,L)
num,den = sp.fraction(sp.together(h))
num=sp.expand(num); den=sp.factor(den)
print("denominator:",den)
P=sp.Poly(num,L)
coeffs=[sp.N(c,60) for c in P.all_coeffs()]
print("degree",P.degree(),"coeffs:",[sp.N(c,8) for c in coeffs])
mp.mp.dps=60
roots=mp.polyroots([mp.mpf(str(c)) for c in coeffs],maxsteps=500,extraprec=500)
print("roots of numerator:",[mp.nstr(r,10) for r in roots])
L0=sp.log(355991)
print("L0 =",sp.N(L0,10)," num(L0) =",sp.N(num.subs(L,L0),15), " h(L0)*k-scale =", sp.N(h.subs(L,L0),15))
print("h at L=100, 1000:",sp.N(h.subs(L,100),10),sp.N(h.subs(L,1000),10))
y=sp.symbols('y')
Q=sp.Poly(sp.expand(num.subs(L,12+y)),y)
cq=[sp.N(c,50) for c in Q.all_coeffs()]
print("coefficients of num(12+y) (all must be >0):",[sp.N(c,6) for c in cq], all(c>0 for c in cq))
