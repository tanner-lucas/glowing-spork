import numpy as np
tab={48:b'1',49:b'101010'}
w=b'1'
while len(w)<12_000_000: w=b''.join(tab[c] for c in w)
arr=np.frombuffer(w,dtype=np.uint8)
ones=np.flatnonzero(arr==49)+1
n=2977771; an=int(ones[n-1]); print("A284366(%d) = %d"%(n,an))
R=2*an+4+n; print("n*sqrt(21) >= 2a(n)+4+n ?", 21*n*n>=R*R, " (21n^2-R^2 =",21*n*n-R*R,")")
ns=np.arange(1,len(ones)+1,dtype=np.float64); d=ns*(np.sqrt(21)-1)/2-ones
print("first n with d>=2-1e-6:",(np.flatnonzero(d>=2-1e-6)[:3]+1), "min d:",d.min())
# check data of A284366
S=open('/home/user/work/oeisdata/seq/A284/A284366.seq').read()
data=[int(x) for x in "".join(l[11:] for l in S.splitlines() if l[:2] in('%S','%T','%U')).replace('\n','').split(',') if x.strip()]
print("data match:", list(ones[:len(data)])==data)
