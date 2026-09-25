import numpy as np
from morph import iterate, positions
import re
def seqdata(A):
    s=open(f"/home/user/work/oeisdata/seq/{A[:4]}/{A}.seq").read()
    t="".join(re.findall(r"^%[STU] "+A+r" (.*)$",s,re.M))
    return [int(x) for x in t.replace(" ","").split(",") if x]
for A,W,i0,i1,c,r,(lo,hi),off in [("A026364","A285430","11","101",0,2+3**.5,(-1,4),1),("A045671","A285671","11","1110",1,(1+17**.5)/4,(-1,2),0)]:
    w=iterate(i0,i1,1,14)
    assert list(w[:len(seqdata(W))])==seqdata(W)
    a=positions(w,c)
    if off==0: a=np.concatenate(([0],a)); n=np.arange(0,len(a),dtype=float)
    else: n=np.arange(1,len(a)+1,dtype=float)
    d=seqdata(A); print(A,"data ok",list(a[:len(d)])==d, "N",len(a))
    D=n*r-a; print("  minD",D.min(),"maxD",D.max())
