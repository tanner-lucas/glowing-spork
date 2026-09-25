import numpy as np, math, sys
from mpmath import mp, sqrt as msqrt
def word(w0,w1,iters_parity,length,start=0):
    s=np.array([start],dtype=np.int8); imgs=[np.array(w0,dtype=np.int8),np.array(w1,dtype=np.int8)]
    k=0
    while True:
        lens=np.where(s==0,len(w0),len(w1)).astype(np.int64)
        out=np.empty(int(lens.sum()),dtype=np.int8)
        pos=np.concatenate(([0],np.cumsum(lens)[:-1]))
        for c in (0,1):
            idx=pos[s==c]
            for j,ch in enumerate(imgs[c]): out[idx+j]=ch
        s=out; k+=1
        if len(s)>=length and k%2==iters_parity%2: return s[:length]
def test(name,w0,w1,parity,letter,r,lo,hi,length,data=None):
    s=word(w0,w1,parity,length)
    p=np.nonzero(s==letter)[0].astype(np.float64)+1
    if data is not None:
        ok = [int(x) for x in p[:len(data)]]==data
    else: ok=None
    n=np.arange(1,len(p)+1,dtype=np.float64)
    d=n*r-p
    bad=np.nonzero((d<=lo)|(d>=hi))[0]
    print(f"{name}: data_ok={ok} N={len(p)} min={d.min():.6f}@{d.argmin()+1} max={d.max():.6f}@{d.argmax()+1} claimed ({lo:.4f},{hi:.4f}) first_viol={(bad[:3]+1).tolist()} {d[bad[:3]].tolist()}")
    return d
if __name__=='__main__':
    L=int(float(sys.argv[1])) if len(sys.argv)>1 else 10**7
    s3=math.sqrt(3); s13=math.sqrt(13); s2=math.sqrt(2); phi=(1+5**.5)/2
    test('A086398',[1,0],[1,0,0,0],10,1,1+s3,-1,4,L,[1,5,7,9,11,15,17,21,23,27,29,33,35,37,39,43,45,49,51,53,55,59,61,65])
    test('A283965',[1],[1,0,1,0],10,1,s3,-1,2,L)
    test('A284368u',[1],[1,0,1,1],10,0,(5+s13)/2,1,3,L)
    test('A284368v',[1],[1,0,1,1],10,1,(-1+s13)/2,-1,1,L)
    test('A284507',[1],[1,1,0,0],16,1,s3,-2,4,L)
    test('A284675',[1],[0,1,1,1],6,0,(5+s13)/2,2,4,L)
    test('A284930',[0,1],[1,0,1,1],6,0,2+s2,1,4,L)
    test('A284941',[0,1],[1,1,0,1],6,1,s2,-1,2,L)
    test('A285082',[1,0],[0,1,1],14,1,phi,-1,1,L)
    test('A285138',[1,0],[0,0,0,1],11,1,1+s3,-1,s3,L)
    test('A285209',[1,0],[0,1,0,0],11,0,1+math.sqrt(1/3),-1,1,L)
    test('A285302',[1,0],[1,0,0,0],10,0,1+math.sqrt(1/3),-2,2,L)
