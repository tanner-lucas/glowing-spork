import numpy as np, sys
def fixed_word(w0,w1,length,iters_even=True,start=0):
    # iterate sigma on [start]; use even number of iterations (fixed point of sigma^2) if iters_even
    s=np.array([start],dtype=np.int8)
    imgs=[np.array(w0,dtype=np.int8),np.array(w1,dtype=np.int8)]
    k=0
    while True:
        lens=np.where(s==0,len(w0),len(w1))
        out=np.empty(int(lens.sum()),dtype=np.int8)
        pos=np.concatenate(([0],np.cumsum(lens)[:-1]))
        for c in (0,1):
            idx=pos[s==c]
            for j,ch in enumerate(imgs[c]):
                out[idx+j]=ch
        s=out; k+=1
        if len(s)>=length and (k%2==0 or not iters_even): break
    return s[:length]
if __name__=='__main__':
    s=fixed_word([1,0],[0,0,0,0],10**7)
    print(''.join(map(str,s[:40])))
    pos1=np.nonzero(s==1)[0]+1
    print('first positions of 1:',pos1[:23].tolist())
    rstar=(3+17**0.5)/2
    n=np.arange(1,len(pos1)+1)
    d=n*rstar-pos1
    print('true r*=',rstar)
    for N in [10,100,1000,10**4,10**5,10**6,len(pos1)]:
        dd=d[:N]; print(N,'min',dd.min(),'at',dd.argmin()+1,'max',dd.max(),'at',dd.argmax()+1)
    r=3.5621
    d2=n*r-pos1
    bad=np.nonzero((d2<=-3)|(d2>=0))[0]
    print('r=3.5621 first violations n=',(bad[:5]+1).tolist(), d2[bad[:5]].tolist())
