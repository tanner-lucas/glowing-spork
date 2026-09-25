# Independent implementation mimicking the OEIS Mathematica code: cyclic ListConvolve on a (2*stages+1)^2 torus.
import numpy as np, sys
def run(code, stages):
    rule=[(code>>i)&1 for i in range(10)]   # rule[k] = new state for index k = 2*sum+center
    g=2*stages+1
    a=np.zeros((g,g),dtype=np.int64); a[g//2,g//2]=1
    out=[a.copy()]
    lut=np.array(rule,dtype=np.int64)
    for n in range(stages+1):
        s=np.roll(a,1,0)+np.roll(a,-1,0)+np.roll(a,1,1)+np.roll(a,-1,1)
        a=lut[2*s+a]
        out.append(a.copy())
    k=g//2
    res=[]
    for n in range(stages):
        row=out[n][k, k-n:k+1]   # stage n, x=-n..0
        rrow=out[n][k, k:k+n+1]
        res.append((''.join(map(str,row)).lstrip('0') or '0', ''.join(map(str,rrow)).lstrip('0') or '0', int(out[n][k-n:k+n+1, k-n:k+n+1].sum())))
    return res
if __name__=="__main__":
    code=int(sys.argv[1]); T=int(sys.argv[2])
    for n,(L,R,c) in enumerate(run(code,T)): print(n,'L',L,'R',R,'ON',c)
