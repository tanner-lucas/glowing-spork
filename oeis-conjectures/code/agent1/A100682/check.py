from math import comb, isqrt
from sympy import integer_nthroot
def iroot4(x):
    r = isqrt(isqrt(x))
    while (r+1)**4 <= x: r += 1
    while r**4 > x: r -= 1
    return r
def a(n): return iroot4(comb(n+3,4))
# b-file check
S=[int(x) for x in "0,1,1,1,2,2,3,3,4,4,5,5,6,6,6,7,7,8,8,9,9,10,10,11,11,11,12,12,13,13,14,14,15,15,16,16,16,17,17,18,18,19,19,20,20,21,21,21,22,22,23,23,24,24,25,25,25,26,26,27,27,28,28,29,29,30,30,30,31,31".split(',')]
b = {i:v for i,v in enumerate(S)}
bad = [i for i in b if a(i)!=b[i]]
print("bfile terms", len(b), "mismatches", bad[:5])
def g(n):  # floor((n - 3/2)/24^(1/4)) exact : max k>=0 with 384 k^4 <= (2n-3)^4, for 2n-3>=0
    t = 2*n-3
    if t < 0:
        # floor of negative number
        import mpmath
        mpmath.mp.dps=50
        return int(mpmath.floor(mpmath.mpf(t)/2/mpmath.mpf(24)**0.25))
    k = iroot4(t**4 // 384)
    while 384*(k+1)**4 <= t**4: k+=1
    while 384*k**4 > t**4: k-=1
    return k
exc=[]

exc2 = [n for n in range(0, 200001) if a(n)!=g(n+3)]
print("exceptions with n+3 shift:", exc2)
