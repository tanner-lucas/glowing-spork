from morph import *
from mpmath import mp, mpf, sqrt
w_even = iterate("10","0000",1,16)   # sigma^16(1): fixed point of sigma^2 starting with 1
w_odd  = iterate("10","0000",0,15)   # sigma^15(0) should be a prefix-compatible version
L=min(len(w_even),len(w_odd))
print("lengths",len(w_even),len(w_odd),"agree on common prefix:", bool((w_even[:L]==w_odd[:L]).all()))
w=w_even
data_word=[1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0]
assert list(w[:len(data_word)])==data_word
a=positions(w,1)
data=[1,3,5,7,13,15,17,19,21,27,29,31,33,35,41,43,45,47,49,55,61,67,73,79,81,83,85,87,93,95,97,99,101,107,109,111,113,115,121,123,125,127,129,135,137,139,141,143,149,155,161,167,173,175,177,179,181,187,189]
assert list(a[:len(data)])==data
print("data reproduced; #positions:",len(a))
n=np.arange(1,len(a)+1,dtype=np.float64)
for r in [(3+17**0.5)/2, 3.5621, 3.5615]:
    D=n*r-a
    i1=int(np.argmin(D)); i2=int(np.argmax(D))
    print("r=%.10f  min D=%.4f at n=%d (a=%d)   max D=%.4f at n=%d (a=%d)"%(r,D[i1],i1+1,a[i1],D[i2],i2+1,a[i2]))
    bad=np.nonzero((D<=-1)|(D>=3))[0]
    print("   first violation index n=",bad[0]+1 if len(bad) else None, " a(n)=", a[bad[0]] if len(bad) else None, "D=",D[bad[0]] if len(bad) else None)
np.save("a285130.npy", a[:2000000])
