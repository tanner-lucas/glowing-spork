import sys
def ispow2(x): return x>0 and (x&(x-1))==0
def count(W):
    # W sorted list of odd ints; count unordered pairs of distinct members summing to a power of 2
    S=set(W); c=0
    mx=2*max(W)
    for x in W:
        T=1
        while T<=mx:
            y=T-x
            if y>x and y in S: c+=1
            T*=2
    return c
def a(n, extra=0):
    best=-1; bp=-1; bs=None
    starts=[1-2*k for k in range(0,n+1)] + [3+2*j for j in range(extra)]
    for s in starts:
        W=list(range(s, s+2*n, 2))
        c=count(W); p=sum(1 for x in W if x>0)
        if c>best or (c==best and p>bp):
            if c>best: best=c; bp=p; bs=s
            else: bp=p; bs=s
    return bp,best,bs
N=int(sys.argv[1])
res={}
for line in open('out30000.txt'):
    n,bp,conj,best=map(int,line.split()); res[n]=(bp,best)
bad=0
for n in list(range(1,N+1)):
    bp,best,bs=a(n, extra=2*n)
    if (bp,best)!=res[n]: print("MISMATCH",n,(bp,best),res[n]); bad+=1
print("checked",N,"bad",bad)
for n in [57,119,120,241,495]:
    print(n, a(n))
