import sys
from functools import lru_cache
from sympy import divisors
from collections import Counter
LIM=int(float(sys.argv[1]))
PR=[2,3,5,7,11,13,17,19,23,29,31,37]
# canonical numbers (non-increasing exponents) up to LIM
canon=[]
def gen(i,maxe,cur):
    canon.append(cur)
    p=PR[i]; v=cur
    for e in range(1,maxe+1):
        v*=p
        if v>LIM: break
        gen(i+1,e,v)
gen(0,64,1)
canon.sort()
def facs(n, mind=2):
    # yield factorizations as lists of nondecreasing factors >= mind
    if n==1: yield []; return
    for d in divisors(n):
        if d<mind: continue
        if d*d>n and d!=n: continue
        for rest in facs(n//d, d): yield [d]+rest
def a(n):
    c=0
    for f in facs(n):
        if not f: continue
        cnt=Counter(f); m=max(cnt.values())
        if sum(1 for v in cnt.values() if v==m)==1: c+=1
    return c
vals={}
for n in canon[1:]:
    v=a(n); vals.setdefault(v,[]).append(n)
print('values found (value: smallest canonical n):')
print(sorted((v,ns[0]) for v,ns in vals.items())[:60])
print('9 present?', 9 in vals)
