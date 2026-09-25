from math import isqrt
import sys
N=int(sys.argv[1])
def A003231(n): return (5*n+isqrt(5*n*n))//2
def G(x): return (isqrt(5*(x+1)**2)-(x+1))//2
def A249115(m): return (5*m-isqrt(5*m*m)-1)//2
def A003258(n):
    y=G(A003231(n))
    m=int(y/1.3819660112501051)-3
    while A249115(m)<y: m+=1
    if A249115(m)!=y: return None
    return m
def A078489(n):
    # least j>=2 with j^2+(n-1)j-n(n+1)>=0
    j=max(2,int(n*0.618)-3)
    while j*j+(n-1)*j-n*(n+1)<0: j+=1
    # verify minimal
    assert j==2 or (j-1)*(j-1)+(n-1)*(j-1)-n*(n+1)<0
    return j
data=[2,3,5,7,8,10,12,13,15,16,18,20,21,23,24,26,28,29,31,33,34,36,37,39]
print([A003258(n) for n in range(1,25)]==data)
d2=[2,2,3,4,4,5,6,6,7,7,8,9,9,10,10,11,12,12,13,14,14,15,15,16,17,17,18]
print([A078489(n) for n in range(1,28)]==d2)
bad=0
for n in range(1,N+1):
    a=A003258(n); b=A078489(n)+n-1
    if a!=b:
        print("DIFF",n,a,b); bad+=1
        if bad>20: break
print("done",N)
