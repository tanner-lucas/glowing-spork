import numpy as np, sys
def run(rule,T):
    W=2*T+5; C=T+2
    a=np.zeros(W,dtype=np.uint8); a[C]=1; bg=0
    lut=np.array([(rule>>i)&1 for i in range(8)],dtype=np.uint8)
    rows=[a.copy()]; bgs=[0]
    for n in range(T):
        l=np.roll(a,1); r=np.roll(a,-1)
        idx=4*l+2*a+r
        b=lut[idx]
        nbg=lut[7*bg]
        b[0]=nbg; b[-1]=nbg
        a=b; bg=nbg
        rows.append(a.copy())
    return rows,C
if __name__=="__main__":
    rule=int(sys.argv[1]); T=int(sys.argv[2])
    rows,C=run(rule,T)
    mid=[int(r[C]) for r in rows]
    print("mid",''.join(map(str,mid[:200])))
