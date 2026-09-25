import numpy as np, re
from morphtest import word
L=2*10**7
tm=word([0,1],[1,0],1,L); w=''.join('01'[x] for x in tm)
w1=w.replace('110','1')  # python replace is left-to-right non-overlapping, same as StringReplace single rule
p=np.array([i+1 for i,ch in enumerate(w1) if ch=='1']); n=np.arange(1,len(p)+1)
print('A286051 2n-a(n) values:', sorted(set((2*n-p).tolist())), len(p))
# A285354
s=word([1,0],[1,1,0,0],13,L)
u=np.nonzero(s==0)[0]+1; nu=np.arange(1,len(u)+1)
t1=2*nu+1-u
print('t1 values',sorted(set(t1.tolist())))
pos1=np.nonzero(t1==1)[0]+1; m=np.arange(1,len(pos1)+1)
vals=3*m/2+0.5-pos1
print('A285354 data', pos1[:24].tolist())
print('A285354 3n/2+1/2-a(n) values', sorted(set(vals.tolist())), len(pos1))
# A284795: s = fixed pt of 0->01, 1->0011 (7 iters, odd), d=Differences
s=word([0,1],[0,0,1,1],7,L).astype(np.int64); d=np.diff(s)
P0=np.nonzero(d==0)[0]+1; k=np.arange(1,len(P0)+1)
print('A284795 data',P0[:23].tolist())
print('a(n)-3n+3 set',sorted(set((P0-3*k+3).tolist())))
Pm=np.nonzero(d==-1)[0]+1; Pp=np.nonzero(d==1)[0]+1
k1=np.arange(1,len(Pm)+1); k2=np.arange(1,len(Pp)+1)
print('3n+2-A284795?? using -1 positions set',sorted(set((3*k1+2-Pm).tolist()))[:10],' 3n-2 - (+1 positions)', sorted(set((3*k2-2-Pp).tolist()))[:10])
