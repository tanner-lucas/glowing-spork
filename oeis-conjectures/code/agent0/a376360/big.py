from math import isqrt
def lastsq(n):
    while n>0:
        s=isqrt(n)
        if s==1: return n
        n%=s*s
    return 0
def check(L,g,c):
    ok = lastsq(L)==c and lastsq(L+g)==c and all(lastsq(L+j)!=c for j in range(1,g))
    return ok,[lastsq(L+j) for j in range(g+1)]
# digit 1: gap 7 at t=26563
t,tp=26563,26570
assert lastsq(t)==1 and lastsq(tp)==1 and all(lastsq(x)!=1 for x in range(t+1,tp))
s=13285; tc=s*s+t; tcp=s*s+tp
assert tcp<= (s+1)**2 and 2*s>=tp
print("copy:",tc,tcp, check(tc,7,1))
s2=(tcp-1)//2; L=s2*s2+tc
print("A376358 gap-8 candidate L=",L, check(L,8,1))
# digit 2: gap 10 at t=33116
t,tp=33116,33126
assert lastsq(t)==2 and lastsq(tp)==2 and all(lastsq(x)!=2 for x in range(t+1,tp))
s=16563; tc=s*s+t; tcp=s*s+tp
print("copy:",tc,tcp, check(tc,10,2))
s2=(tcp-1)//2; L=s2*s2+tc
print("A376359 gap-12 candidate L=",L, check(L,12,2))
# A376360 direct
print("A376360 gap-12 at 336391:", check(336391,12,3))
print("A376360 gap-16 at 1833303:", check(1833303,16,3))
