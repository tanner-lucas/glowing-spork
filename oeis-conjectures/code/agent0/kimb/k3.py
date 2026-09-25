from mpmath import mp, sqrt, mpf, nstr
import exactdp
mp.dps=80
for c,r,name in [(1,sqrt(2),'A284946 (letter 1) with r=sqrt2'),(0,2+sqrt(2),'A284945 (letter 0) with r=2+sqrt2')]:
    res=exactdp.analyze("01","1110",('fp',0),c,r)
    k,L,g,h=res[-1]
    print(name,"inf",nstr(g,12),"sup",nstr(h,12))
