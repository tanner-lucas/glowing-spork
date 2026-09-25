from math import isqrt
def itri(n):
    k=(isqrt(8*n+1)-1)//2
    return k
def lasttri(n):
    while n>0:
        k=itri(n)
        if k==1: return n
        n%= k*(k+1)//2
    return 0
def rep(n):
    k=itri(n); d=[]
    for j in range(k,0,-1):
        T=j*(j+1)//2; d.append(n//T); n%=T
    return d
print([int("".join(map(str,rep(n)))) for n in range(1,17)])
def check(L,g,c): return lasttri(L)==c and lasttri(L+g)==c and all(lasttri(L+j)!=c for j in range(1,g))
print("A376355 gap 7 at 2598054:", check(2598054,7,1))
print("A376356 gap 10 at 5256895:", check(5256895,10,2))
# reproduce data prefixes
S0=[n for n in range(1,70) if lasttri(n)==0]; S1=[n for n in range(1,75) if lasttri(n)==1]; S2=[n for n in range(1,85) if lasttri(n)==2]
print(S0[:24]); print(S1[:24]); print(S2[:24])
