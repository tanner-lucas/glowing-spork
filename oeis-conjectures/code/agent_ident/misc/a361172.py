import sys
N=int(sys.argv[1])
# a(n): smallest positive not among terms between a(n-1) and previous occurrence of a(n-1) inclusive; if a(n-1) first occurrence, a(n)=1
a=[0,1]; last={1:1}; prevlast={}
first={1:1}
# terms between two adjacent 1s strictly increasing => segment is sorted; we can compute mex of window by scanning; windows can be long though
import bisect
for n in range(2,N+1):
    x=a[n-1]
    if x not in prevlast:
        v=1
    else:
        p=prevlast[x]
        s=set(a[p:n])
        v=1
        while v in s: v+=1
    a.append(v)
    if v in last: prevlast[v]=last[v]
    last[v]=n
    if v not in first: first[v]=n
fo=[first[k] for k in sorted(first)]
# A060432 partial sums of A002024 (n appears n times)
from math import isqrt
def A002024(n): return (isqrt(8*n)+1)//2
S=[];s=0
for n in range(1,len(fo)+1): s+=A002024(n); S.append(s)
print(a[1:40]); print(fo[:20]); print(S[:20])
m=[i for i in range(len(fo)) if fo[i]!=S[i]]
print("mismatch indices:",m[:5], "checked", len(fo))
