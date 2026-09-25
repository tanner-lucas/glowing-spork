import numpy as np
N=2000000+2100
phi=np.arange(N,dtype=np.int64)
for p in range(2,N):
    if phi[p]==p:  # prime
        phi[p::p]-=phi[p::p]//p
js=list(range(3,2000,6))
hits=set()
for j in js:
    k=np.arange(1,2000000)
    m=np.nonzero(phi[k+j]==phi[k]+phi[j])[0]
    for x in m: hits.add((j,int(k[x])))
c=set(tuple(map(int,l.split())) for l in open('hits_small.txt'))
print(len(hits),len(c),hits==c)
# least k vs A066426 data
S="2,1,0,4,4,4,14,6,6,4,16,6,14,6,0,5,8,6,6,8,0,4,46,12,10,8,6,12,26,12,62,6,12,4,16,12,28,6,0,10,24,24,86,8,0,6,38,6,62,25,12,16,24,18,32,24,0,4,118,24,80,6,12,10,28,12,134,8,0,35,142,24,146,8,30,12,8,24,46,20,6"
a=[int(x) for x in S.split(',')]
least={}
for j,k in sorted(c):
    least.setdefault(j,k)
ok=all((least.get(n,0)==a[n-1]) for n in range(3,len(a)+1,6))
print('A066426 odd multiples of 3 match:',ok)
unres=[j for j in js if j not in least]
print(len(unres),unres[:60])
