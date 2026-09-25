from math import comb, isqrt
def iroot4(x):
    r = isqrt(isqrt(x))
    while (r+1)**4 <= x: r += 1
    while r**4 > x: r -= 1
    return r
def conj(N):  # floor((N-3/2)/24^(1/4)) exactly, N>=2
    t = 2*N-3
    k = iroot4(t**4 // 384)
    while 384*(k+1)**4 <= t**4: k+=1
    while 384*k**4 > t**4: k-=1
    return k
c = 24**0.25
for line in open('cand.txt'):
    k = int(line.split()[0])
    N0 = int(k*c+1.5)
    for N in range(N0-2, N0+3):
        n = N-3   # sequence index: a(n) = floor(C(n+3,4)^(1/4))
        a = iroot4(comb(N,4)); g = conj(N)
        if a != g:
            print("EXCEPTION: N=%d (sequence n=%d): a(n)=floor(C(N,4)^(1/4))=%d, floor((N-3/2)/24^(1/4))=%d"%(N,n,a,g))
