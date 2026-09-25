import math
def g(J): return 0 if J==0 else 1+math.isqrt(4*J-3)
def T(i,j): return i+g(j+i*(i-1)//2)
N=1500; viol=set()
for i in range(N):
    for j in range(N):
        for di in (-1,0,1):
            for dj in (-1,0,1):
                a,b=i+di,j+dj
                if a<0 or b<0: continue
                if abs(T(a,b)-T(i,j))>3: viol.add(tuple(sorted([(i,j),(a,b)])))
print(viol)
# A360925 differences
a=[T(n,0) for n in range(0,200000)]
d=[a[n+1]-a[n] for n in range(len(a)-1)]
print(d[:8], set(d[2:]), sum(1 for x in d[2:] if x==3)/len(d[2:]))
