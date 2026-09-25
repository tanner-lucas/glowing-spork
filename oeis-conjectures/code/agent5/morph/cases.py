import mpmath as mp, subprocess, sys, re
mp.mp.dps=40
S=mp.sqrt
# (A-number, img0, img1, iterations_in_mathematica, target letter, stated r, lo, hi)
cases=[
 ("A283967",'1','10101',10,0,(7+S(17))/4,-1,3),   # u(n) positions of 0 (conjecture in A283966)
 ("A284015",'1','10101',10,1,(-1+S(17))/2,-1,2),  # v(n) positions of 1
 ("A284370",'1','1001',15,0,(3+S(3))/2,-3,4),
 ("A284371",'1','1001',15,1,S(3),-2,3),
 ("A284676",'1','0111',6,1,(-1+S(13))/2,-1,4),
 ("A284773",'01','0010',6,0,(3+S(3))/3,-1,2),
 ("A284902",'01','1000',6,0,(3+S(3))/3,-3,3),
 ("A284931",'01','1011',6,1,S(2),-1,1),
 ("A284945",'01','1110',6,0,2+S(2),-4,3),
 ("A285032",'10','001',8,0,1+S(mp.mpf(1)/2),-1,2),
 ("A285084",'10','011',13,0,(3+S(5))/2,0,(3+S(5))/2),
 ("A285129",'10','0000',13,0,mp.mpf('1.3903882032022076'),-1,1),
 ("A285140",'10','0010',12,0,(3+S(3))/3,-1,1),
 ("A285210",'10','0100',11,1,1+S(3),0,3),
 ("A285419",'11','011',10,0,2+S(3),-1,5),
 ("A285670",'11','1101',9,1,(1+S(17))/4,-1,4),
]
def seqdata(a):
    d=a[1:5]
    txt=open(f"/home/user/work/oeisdata/seq/A{d[:3]}/{a}.seq").read()
    s=''.join(l.split(' ',2)[2].strip() for l in txt.splitlines() if l[:2] in('%S','%T','%U'))
    return [int(x) for x in s.split(',') if x]
def word(i0,i1,k):
    w='0'
    for _ in range(k): w=''.join(i0 if c=='0' else i1 for c in w)
    return w
for (a,i0,i1,k,c,r,lo,hi) in cases:
    # Perron frequencies
    M=mp.matrix([[i0.count('0'),i1.count('0')],[i0.count('1'),i1.count('1')]])
    ev,er=mp.eig(M)
    j=max(range(2),key=lambda t: mp.re(ev[t]))
    v=[mp.re(er[0,j]),mp.re(er[1,j])]; f=v[c]/(v[0]+v[1])
    other=[e for t,e in enumerate(ev) if t!=j][0]
    # reproduce data
    kk=k
    w=word(i0,i1,kk)
    while len(w)<5000: kk+=2; w=word(i0,i1,kk)
    pos=[i+1 for i,ch in enumerate(w) if ch==str(c)]
    try:
        dat=seqdata(a); ok = pos[:len(dat)]==dat
    except Exception as e: dat=None; ok=str(e)
    print(a, "data match:",ok, "len",len(dat) if dat else None, " stated r=",mp.nstr(r,12)," 1/freq=",mp.nstr(1/f,12)," |lambda2|=",mp.nstr(abs(other),5))

if len(sys.argv)>1:
    maxlen=int(float(sys.argv[1]))
    for (a,i0,i1,k,c,r,lo,hi) in cases:
        # find k' of same parity with length >= maxlen
        M=mp.matrix([[i0.count('0'),i1.count('0')],[i0.count('1'),i1.count('1')]])
        v=mp.matrix([1,0]); kk=0; L=1
        while not (kk%2==k%2 and L>=maxlen and kk>=k):
            v=M*v; kk+=1; L=v[0]+v[1]
        rs=[None,None]; los=[-1e18,-1e18]; his=[1e18,1e18]
        rs[c]=r; los[c]=lo; his[c]=hi
        # other letter: its inverse frequency, wide bounds
        ev,er=mp.eig(M); j=max(range(2),key=lambda t: mp.re(ev[t]))
        vv=[mp.re(er[0,j]),mp.re(er[1,j])]; rs[1-c]=(vv[0]+vv[1])/vv[1-c]
        args=["./disc",i0,i1,"0",str(kk),str(maxlen)]
        for t in range(2): args+= [mp.nstr(rs[t],30), mp.nstr(mp.mpf(los[t]),30), mp.nstr(mp.mpf(his[t]),30)]
        print("=== ",a," k=",kk," target letter",c, flush=True)
        out=subprocess.run(args,capture_output=True,text=True).stdout
        print(out, flush=True)
