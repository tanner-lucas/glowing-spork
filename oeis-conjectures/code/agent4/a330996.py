N=20000
p=[0]*(N+1); p[0]=1
# Euler pentagonal recurrence for p(n)
for n in range(1,N+1):
    s=0; k=1
    while True:
        g1=k*(3*k-1)//2
        if g1>n: break
        sg=1 if k%2 else -1
        s+=sg*p[n-g1]
        g2=k*(3*k+1)//2
        if g2<=n: s+=sg*p[n-g2]
        k+=1
    p[n]=s
q=[0]*(N+1); q[0]=1
for k in range(1,N+1):
    for n in range(N,k-1,-1): q[n]+=q[n-k]
bad=[n for n in range(6,N) if p[n+1]*q[n] < p[n]*q[n+1]]
print('p(1..10)',p[1:11],'q(1..10)',q[1:11])
print('decreases of P/Q for n>5 up to',N,':',bad[:10])
