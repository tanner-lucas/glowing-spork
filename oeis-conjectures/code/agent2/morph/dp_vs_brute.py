import mpmath as mp
from exact_extremes import analyze, cases
mp.mp.dps=30
def brute(i0,i1,start,power,t,K):
    img={0:i0,1:i1}
    tau={c:str(c) for c in (0,1)}
    for _ in range(power): tau={c:"".join(img[int(x)] for x in tau[c]) for c in (0,1)}
    w=str(start)
    for _ in range(K): w="".join(tau[int(x)] for x in w)
    return w
for (aid,i0,i1,st,pw,t,lo,hi) in cases:
    l1,l2,r,h=analyze(i0,i1,st,pw,t,K=40)
    # choose K such that length ~ 2e5
    K=1
    while len(brute(i0,i1,st,pw,t,K))<150000: K+=1
    w=brute(i0,i1,st,pw,t,K)
    n=0; vals=[]
    for N,c in enumerate(w,1):
        if c==str(t):
            n+=1; vals.append(n*r-N)
    print(f"{aid:9s} K={K} len={len(w)} brute min/max = {mp.nstr(min(vals),12)} / {mp.nstr(max(vals),12)} ; DP_K min/max = {mp.nstr(h[K-1][0],12)} / {mp.nstr(h[K-1][1],12)}")
