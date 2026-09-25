# Generalized exact inf/sup of D(n) = n*r - pos_c(n) for the coding tau(w), w = limit of sigma^K(root), K ≡ parity (or any if None)
import mpmath as mp
mp.mp.dps=60
def analyze(i0,i1,tau0,tau1,c,root=0,parity=None,T=500):
    img={0:[int(ch) for ch in i0],1:[int(ch) for ch in i1]}
    tau={0:[int(ch) for ch in tau0],1:[int(ch) for ch in tau1]}
    M=mp.matrix([[i0.count('0'),i1.count('0')],[i0.count('1'),i1.count('1')]])
    tr=M[0,0]+M[1,1]; det=M[0,0]*M[1,1]-M[0,1]*M[1,0]
    disc=mp.sqrt(tr**2-4*det); l1=(tr+disc)/2; l2=(tr-disc)/2
    if M[0,1]!=0: v=[M[0,1], l1-M[0,0]]
    else: v=[l1-M[1,1], M[1,0]]
    # frequency of letter c in tau(w)
    cntc=v[0]*tau[0].count(c)+v[1]*tau[1].count(c); L=v[0]*len(tau[0])+v[1]*len(tau[1])
    r=L/cntc
    def h(word): return r*word.count(c)-len(word)
    def H(wword): # h(tau(wword))
        return sum(h(tau[b]) for b in wword)
    for a in (0,1): assert abs(H(img[a])-l2*H([a]))<mp.mpf(10)**-40
    INF=mp.inf
    # bottom: next letter b of w; inside tau(b), prefix u followed by c
    Gmin={}; Gmax={}
    for b in (0,1):
        vals=[h(tau[b][:j])+r-1 for j in range(len(tau[b])) if tau[b][j]==c]
        Gmin[b]=min(vals) if vals else INF; Gmax[b]=max(vals) if vals else -INF
    best=[INF,-INF]
    for t in range(T):
        w=l2**t; nmin={}; nmax={}
        for b in (0,1):
            mn=INF; mx=-INF
            for j in range(len(img[b])):
                val=w*H(img[b][:j]); nxt=img[b][j]
                if Gmin[nxt]<INF: mn=min(mn,val+Gmin[nxt])
                if Gmax[nxt]>-INF: mx=max(mx,val+Gmax[nxt])
            nmin[b]=mn; nmax[b]=mx
        Gmin,Gmax=nmin,nmax
        if parity is None or (t+1)%2==parity%2:
            best[0]=min(best[0],Gmin[root]); best[1]=max(best[1],Gmax[root])
    return r,l2,best[0],best[1]
if __name__=="__main__":
    # sanity: reproduce earlier A284371
    print("A284371", [mp.nstr(x,20) for x in analyze('1','1001','0','1',1,0,15)])
    print("A285140", [mp.nstr(x,20) for x in analyze('10','0010','0','1',0,0,12)])
    # A026363: positions of 1 in fixed point of 0->11,1->101 (from 1); bounds -1 < n r - a(n) < 2, r=(1+sqrt3)/2
    print("A026363", [mp.nstr(x,20) for x in analyze('11','101','0','1',1,0,None)])
    # A287724: positions of 1 in tau(Fibonacci word), sigma: 0->01,1->0 ; tau: 0->1, 1->011; bounds 0 < n r - a(n) < 3, r=4-sqrt5
    print("A287724", [mp.nstr(x,20) for x in analyze('01','0','1','011',1,0,None)], "4-sqrt5=",mp.nstr(4-mp.sqrt(5),20))
