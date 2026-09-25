import numpy as np, re, math
from morph import iterate, positions
def seqdata(A):
    s=open(f"/home/user/work/oeisdata/seq/{A[:4]}/{A}.seq").read()
    t="".join(re.findall(r"^%[STU] "+A+r" (.*)$",s,re.M))
    return [int(x) for x in t.replace(" ","").split(",") if x]
def build(i0,i1,mode,N=3_000_000):
    # mode: ('fp',letter) fixed point of sigma starting with letter; ('lim',letter) limit of sigma^{2k}(letter)
    kind,let=mode
    w=np.array([let],dtype=np.uint8); steps=0
    while len(w)<N:
        w=iterate(i0,i1,let,steps+ (1 if kind=='fp' else 2)); steps+= (1 if kind=='fp' else 2)
        if steps>80: break
    return w
cases=[
 ("A283967","A283966","1","10101",('fp',1),0,(7+17**.5)/4,(-1,3)),
 ("A284370","A284369","1","1001",('fp',1),0,(3+3**.5)/2,(-3,4)),
 ("A284654","A284653","1","0110",('lim',0),0,(3+3**.5)/2,(-1,3)),
 ("A284678","A284677","1","0111",('lim',1),0,(5+13**.5)/2,(2,4)),
 ("A284774","A284772","01","0010",('fp',0),1,1+3**.5,(-1,2)),
 ("A284903","A284901","01","1000",('fp',0),1,1+3**.5,(-4,6)),
 ("A284946","A284944","01","1110",('fp',0),1,2+2**.5,(-1,3)),
 ("A285033","A285031","10","001",('lim',0),1,1+2**.5,(-1,2)),
 ("A285085","A285083","10","011",('lim',1),1,(1+5**.5)/2,(-1,1)),
 ("A285141","A285139","10","0010",('lim',0),1,1+3**.5,(-1,1)),
 ("A285275","A285274","10","0111",('lim',0),0,2+2**.5,(0,6)),
 ("A285342","A285341","10","1011",('fp',1),0,2+2**.5,(0,4)),
 ("A285359","A285358","10","1101",('fp',1),0,2+2**.5,(-1,1)),
 ("A285420","A285418","11","011",('lim',0),1,(1+3**.5)/2,(-2,2)),
 ("A285130","A285128","10","0000",('lim',1),1,3.5621,(-1,3)),
]
for A,W,i0,i1,mode,letter,r,(lo,hi) in cases:
    w=build(i0,i1,mode)
    wd=seqdata(W); ad=seqdata(A)
    okw = list(w[:len(wd)])==wd
    a=positions(w,letter)
    oka = list(a[:len(ad)])==ad
    n=np.arange(1,len(a)+1,dtype=np.float64)
    D=n*r-a
    bad=np.nonzero((D<=lo)|(D>=hi))[0]
    fv = (int(bad[0])+1, int(a[bad[0]]), float(D[bad[0]])) if len(bad) else None
    print(f"{A}: word ok={okw} pos ok={oka} N={len(a)} minD={D.min():.4f} maxD={D.max():.4f} bounds=({lo},{hi}) firstviol={fv}")
