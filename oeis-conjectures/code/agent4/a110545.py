import gmpy2, sys
from gmpy2 import mpq
N=int(sys.argv[1])
H=[None]; h=mpq(0)
nums=[0]; dens=[1]
for m in range(1,N+1):
    h+=mpq(1,m); nums.append(h.numerator); dens.append(h.denominator)
res=[]
bad=[]
for n in range(1,N+1):
    a=None
    for m in range(1,N+1):
        if nums[m]%n==0 or dens[m]%n==0: a=m; break
    res.append(a)
    if a is None or a>n: bad.append((n,a))
print(res[:30])
print('violations',bad[:20])
