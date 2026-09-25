from fractions import Fraction
def mul(a,b,N):
    r=[0]*(N+1)
    for i,x in enumerate(a):
        if x==0 or i>N: continue
        for j,y in enumerate(b[:N+1-i]):
            if y: r[i+j]+=x*y
    return r
def comp(a,b,N):  # a(b(x)), b[0]==0
    r=[0]*(N+1); p=[1]+[0]*N
    for k in range(N+1):
        if k>0: p=mul(p,b,N)
        if k<len(a) and a[k]:
            for i in range(N+1): r[i]+=a[k]*p[i]
    return r
def solve(eqfun, init, N, deg_of):
    A=init[:]+[0]*(N+1-len(init))
    for n in range(len(init),N+1):
        A[n]=0; e0=eqfun(A,deg_of(n))[deg_of(n)]
        A[n]=1; e1=eqfun(A,deg_of(n))[deg_of(n)]
        s=e1-e0; val=Fraction(-e0,s); assert val.denominator==1; A[n]=int(val)
    return A
N=40
C=[0]*(N+3); C[1]=1
for it in range(N+3):
    C=[0,1]+[0]*(N+1); 
# Catalan C = x + C^2
C=[0]*(N+3); C[1]=1
for _ in range(N+3): 
    sq=mul(C,C,N+2); C=[0,1]+sq[2:N+3]
def eq374570(A,d): return [u-v for u,v in zip(mul(A,A,d), comp(A, mul(A,C,d), d))]
A=solve(eq374570,[0,1],N,lambda n:n+1)
print("A374570",A[1:13]); print(" odd n:",[n for n in range(1,N+1) if A[n]%2])
def eq389540(A,d):
    B=[2*(1 if i==1 else 0)-2*A[i] for i in range(d+1)]
    L=mul(A,A,d); R=comp(A,B,d)
    return [2*u-v for u,v in zip(L,R)]
A=solve(eq389540,[0,1],N,lambda n:n)
print("A389540",A[1:13]); print(" odd n:",[n for n in range(1,N+1) if A[n]%2])
