# Exact inf/sup of D_c(n) = n*r_c - pos_c(n) over the whole limiting word, via Dumont-Thomas prefix decomposition DP.
import mpmath as mp, sys
mp.mp.dps=60
def analyze(i0,i1,k0,c,T=400):
    img={0:[int(ch) for ch in i0],1:[int(ch) for ch in i1]}
    M=mp.matrix([[i0.count('0'),i1.count('0')],[i0.count('1'),i1.count('1')]])
    tr=M[0,0]+M[1,1]; det=M[0,0]*M[1,1]-M[0,1]*M[1,0]
    disc=mp.sqrt(tr**2-4*det); l1=(tr+disc)/2; l2=(tr-disc)/2
    # Perron right eigenvector
    v0=M[0,1]; v1=l1-M[0,0]   # (M-l1 I) v = 0 -> (M00-l1) v0 + M01 v1 = 0 -> v=(M01, l1-M00)
    if v0==0 and v1==0: v0=l1-M[1,1]; v1=M[1,0]
    rc=(v0+v1)/(v0 if c==0 else v1)
    def h(word):  # h(x) = rc*x_c - |x|
        return rc*word.count(c)-len(word)
    # check left-eigen property: h(sigma(a)) = l2*h(a)
    for a in (0,1):
        assert abs(h(img[a]) - l2*h([a]))<mp.mpf(10)**-40, (a,h(img[a]),l2*h([a]))
    # DP from bottom: G_t(b) = min over proper prefixes q of sigma(b) (q = img[b][:j], j<len) of l2^t*h(q) + G_{t-1}(img[b][j])
    INF=mp.inf
    Gmin={0:(0 if c==0 else INF),1:(0 if c==1 else INF)}   # G_{-1}: next letter must be c
    Gmax={0:(0 if c==0 else -INF),1:(0 if c==1 else -INF)}
    best_min=INF; best_max=-INF
    for t in range(0,T):
        w=l2**t
        nmin={}; nmax={}
        for b in (0,1):
            mn=INF; mx=-INF
            for j in range(len(img[b])):
                q=img[b][:j]; nxt=img[b][j]
                val=w*h(q)
                if Gmin[nxt]<INF: mn=min(mn,val+Gmin[nxt])
                if Gmax[nxt]>-INF: mx=max(mx,val+Gmax[nxt])
            nmin[b]=mn; nmax[b]=mx
        Gmin,Gmax=nmin,nmax
        # G_t(0) corresponds to prefixes of sigma^{t+1}(0); parity: word = lim sigma^K(0), K = t+1 ≡ k0 mod 2
        if (t+1)%2==k0%2:
            best_min=min(best_min,Gmin[0]); best_max=max(best_max,Gmax[0])
    return rc,l2,best_min+rc-1,best_max+rc-1
if __name__=="__main__":
    S=mp.sqrt
    cases=[("A283967",'1','10101',10,0,-1,3),("A284015",'1','10101',10,1,-1,2),
     ("A284370",'1','1001',15,0,-3,4),("A284371",'1','1001',15,1,-2,3),
     ("A284676",'1','0111',6,1,-1,4),("A284773",'01','0010',6,0,-1,2),
     ("A284902",'01','1000',6,0,-3,3),("A284931",'01','1011',6,1,-1,1),
     ("A284945",'01','1110',6,0,-4,3),("A285032",'10','001',8,0,-1,2),
     ("A285084",'10','011',13,0,0,(3+S(5))/2),("A285140",'10','0010',12,0,-1,1),
     ("A285210",'10','0100',11,1,0,3),("A285419",'11','011',10,0,-1,5),
     ("A285670",'11','1101',9,1,-1,4)]
    for (a,i0,i1,k0,c,lo,hi) in cases:
        rc,l2,inf,sup=analyze(i0,i1,k0,c)
        print(a,"r=",mp.nstr(rc,15),"l2=",mp.nstr(l2,6)," inf D=",mp.nstr(inf,25)," sup D=",mp.nstr(sup,25)," bounds",(lo,mp.nstr(hi,8)), "OK" if (inf>lo and sup<hi) else "CHECK")
