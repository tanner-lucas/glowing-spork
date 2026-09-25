import sys, math
from sympy import factorint
def divisors_from_f(f):
    ds=[1]
    for p,e in f.items():
        ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def a(n):
    fn=factorint(n)
    cnt=0
    for i in range(1,n+1):
        f=dict(fn)
        for p,e in factorint(i).items(): f[p]=f.get(p,0)+e
        ok=True
        # check any divisor in (i,n)
        for d in divisors_from_f(f):
            if i<d<n: ok=False;break
        if ok: cnt+=1
    return cnt
# verify first terms
data=[1,2,3,3,5,4,7,5,6,6,11,6,13,8,9,8,17,9,19,10,12,12,23,10,16,14,15,13,29,12,31,15,18,18,20,13,37,20,21,16,41,17,43,20,21,24,47,17,31,22,27,23,53,22,31,22,30,30,59,19,61,32,28,26,36,26,67,30,36,26,71,23,73,38]
assert [a(n) for n in range(1,len(data)+1)]==data
print("ok")
for n in [int(x) for x in sys.argv[1:]]:
    v=a(n); print(n, v, n/math.log(n), v/(n/math.log(n)), flush=True)
