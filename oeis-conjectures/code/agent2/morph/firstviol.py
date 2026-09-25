import sys, math
from decimal import Decimal, getcontext
getcontext().prec=50
def gen(i0,i1,start,power,N):
    img={0:[int(c) for c in i0],1:[int(c) for c in i1]}
    w=[start]
    while len(w)<N*4:
        for _ in range(power):
            w=[c for x in w for c in img[x]]
    return w
def check(i0,i1,start,power,letter,r,lo,hi,N):
    w=gen(i0,i1,start,power,N)
    pos=[i+1 for i,c in enumerate(w) if c==letter][:N]
    for n,p in enumerate(pos,1):
        d=n*r-p
        if d<=lo or d>=hi: return n,p,d,pos[:40]
    return None,None,None,pos[:40]
s3=Decimal(3).sqrt()
print("A285135",check("10","0001",0,2,1,1+s3,-1,1,200000))
print("A285144",check("10","0010",1,2,1,1+s3,-1,s3,200000))
def allviol(i0,i1,start,power,letter,r,lo,hi,N,skip=1):
    w=gen(i0,i1,start,power,N)
    pos=[i+1 for i,c in enumerate(w) if c==letter][:N]
    v=[]
    for n,p in enumerate(pos,1):
        d=n*r-p
        if n>skip and (d<=lo or d>=hi): v.append((n,p,float(d)))
        if len(v)>=5: break
    return v
print("A285144 viol n>1:",allviol("10","0010",1,2,1,1+s3,-1,s3,300000))
print("A285135 viol n>1:",allviol("10","0001",0,2,1,1+s3,-1,1,300000))
s2=Decimal(2).sqrt()
print("A285374 with r=2+sqrt2:",allviol("10","1110",1,1,0,2+s2,-4,1,300000,0))
print("A285374 with r=sqrt2:",allviol("10","1110",1,1,0,s2,-4,1,300000,0))
