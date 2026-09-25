# Exact-ish (high precision) inf/sup of D(n) = n*r - a(n), a(n) = position (1-indexed) of n-th occurrence of letter c
# in the (limiting) fixed point, computed over prefixes sigma^k(start) for large k via block recursion.
from mpmath import mp, mpf, sqrt
mp.dps=80
def analyze(i0,i1,mode,c,r,K=70):
    imgs={0:[int(x) for x in i0],1:[int(x) for x in i1]}
    kind,start=mode
    # level-0 blocks: single letters
    # For a word u: cnt(u)=#c in u, L(u)=len; off(u)=r*cnt-L ; G(u)=min over positions i with u_i=c of r*cnt(u[1..i]) - i ; H = max
    cnt={a:(1 if a==c else 0) for a in (0,1)}; L={0:1,1:1}
    G={a:(r*1-1 if a==c else mp.inf) for a in (0,1)}; H={a:(r*1-1 if a==c else -mp.inf) for a in (0,1)}
    res=[]
    for k in range(1,K+1):
        nc,nL,nG,nH={}, {}, {}, {}
        for a in (0,1):
            off=mpf(0); cc=0; ll=0; g=mp.inf; h=-mp.inf
            for b in imgs[a]:
                g=min(g, off+G[b]); h=max(h, off+H[b])
                cc+=cnt[b]; ll+=L[b]; off=r*cc-ll
            nc[a]=cc; nL[a]=ll; nG[a]=g; nH[a]=h
        cnt,L,G,H=nc,nL,nG,nH
        use = (kind=='fp') or (k%2==0)
        if use: res.append((k, L[start], G[start], H[start]))
    return res
import sys
cases={
 "A284654":("1","0110",('lim',0),0,(3+sqrt(3))/2,(-1,3)),
 "A285033":("10","001",('lim',0),1,1+sqrt(2),(-1,2)),
 "A285085":("10","011",('lim',1),1,(1+sqrt(5))/2,(-1,1)),
 "A285275":("10","0111",('lim',0),0,2+sqrt(2),(0,6)),
 "A285342":("10","1011",('fp',1),0,2+sqrt(2),(0,4)),
 "A285359":("10","1101",('fp',1),0,2+sqrt(2),(-1,1)),
 "A283967":("1","10101",('fp',1),0,(7+sqrt(17))/4,(-1,3)),
 "A284370":("1","1001",('fp',1),0,(3+sqrt(3))/2,(-3,4)),
 "A284678":("1","0111",('lim',1),0,(5+sqrt(13))/2,(2,4)),
 "A284774":("01","0010",('fp',0),1,1+sqrt(3),(-1,2)),
 "A284903":("01","1000",('fp',0),1,1+sqrt(3),(-4,6)),
 "A285420":("11","011",('lim',0),1,(1+sqrt(3))/2,(-2,2)),
 "A285141":("10","0010",('lim',0),1,1+sqrt(3),(-1,1)),
}
for A,(i0,i1,mode,c,r,b) in cases.items():
    res=analyze(i0,i1,mode,c,r)
    k,Lk,g,h=res[-1]
    k2,L2,g2,h2=res[len(res)//2]
    print(f"{A} bounds {b}: inf ~ {mp.nstr(g,15)}  sup ~ {mp.nstr(h,15)}  (at k={k}, len~{mp.nstr(mpf(Lk),5)});  at k={k2}: {mp.nstr(g2,15)} {mp.nstr(h2,15)}")
print("----")
for A,(i0,i1,mode,c,r,b) in {"A026364":("11","101",('fp',1),0,2+sqrt(3),(-1,4)), "A045671":("11","1110",('fp',1),1,(1+sqrt(17))/4,(-1,2))}.items():
    res=analyze(i0,i1,mode,c,r)
    k,Lk,g,h=res[-1]
    print(A,b,"inf",mp.nstr(g,15),"sup",mp.nstr(h,15))
