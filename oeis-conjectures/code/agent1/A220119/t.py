from math import comb
import sys
def direct(n):
    B=[comb(n,j)**2*comb(n+j,n) for j in range(n+1)]
    return sum(B[j]*B[k]*comb(j+k,n) for j in range(n+1) for k in range(n+1) if j+k>=n)
N=int(sys.argv[1])
a=[1,12]
for n in range(2,N+1):
    num = 3*(2*n-1)*(3*n*n-3*n+1)*(15*n*n-15*n+4)*a[n-1] + 3*(n-1)**3*(3*n-4)*(3*n-2)*a[n-2]
    q,r = divmod(num, n**5); assert r==0
    a.append(q)
for n in range(0,41): assert a[n]==direct(n), n
print("recurrence matches direct sum for n<=40")
bad=[n for n in range(1,N+1) if a[n] % ((n+1)*(n+2))]
print("failures of (n+1)(n+2) | a(n), n<=%d:"%N, bad[:20])
