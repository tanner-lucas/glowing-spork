import sys
from math import isqrt
N=int(sys.argv[1])
# p_le[j][s] partitions of s into at most j parts (= parts <= j)
J=isqrt(N)+1
p_le=[[0]*(N+1) for _ in range(J+1)]
p_le[0][0]=1
for j in range(1,J+1):
    row=p_le[j]; prev=p_le[j-1]
    for s in range(N+1):
        row[s]=prev[s]+(row[s-j] if s>=j else 0)
def A387737(n):
    tot=1  # k=1
    for k in range(2,isqrt(n)+1):
        lo=max(0,(n+1)//2-k); m=n-k*k
        for L in range(lo,m+1):
            tot+=p_le[k-1][m-L]
    return tot
# b[m][j]: partitions of m into parts <= j, gaps>=2, parts>=2
H=N//2+2
b=[[0]*(N+2) for _ in range(H+1)]
for j in range(N+2): b[0][j]=1
for m in range(1,H+1):
    bm=b[m]
    for j in range(2,N+2):
        bm[j]=bm[j-1]+(b[m-j][j-2] if m>=j and j-2>=0 else 0)
def bb(m,j):
    if m<0: return 0
    if j<0: j=0
    return b[m][min(j,N+1)] if m>0 else 1
def A387736(n):
    tot=0
    for L in range(max(2,(n+1)//2),n+1):
        m=n-L
        # parts of rest <= L-2
        tot+=bb(m,L-2) if L-2>=0 else (1 if m==0 else 0)
    return tot
d37=[1,1,1,2,2,3,3,4,4,5,5,7,7,9,9,12,12,15,15,19,19,23,23,29,29,35,35,43,43,52,52,63,63,75,75,90,90,106,106,126,126,148,148,174,174,203,203,238,238,276,276,321,321,371,371,429,429,493,493,568,568,650]
d36=[0,0,1,1,1,1,2,2,3,3,4,4,6,6,8,8,11,11,14,14,18,18,22,22,28,28,34,34,42,42,51,51,62,62,74,74,89,89,105,105,125,125,147,147,173,173,202,202,237,237,275,275,320,320,370,370,428,428,492,492,567,567,649]
print([A387737(n) for n in range(1,len(d37)+1)]==d37)
print([A387736(n) for n in range(0,len(d36))]==d36)
bad=0
for n in range(4,N+1):
    x=A387737(n); y=A387736(n)
    if x!=y+1:
        print("DIFF n=",n,x,y); bad+=1
        if bad>5: break
print("checked to",N)
