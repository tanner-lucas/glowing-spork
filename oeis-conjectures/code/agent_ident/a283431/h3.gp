a(n)=my(H=polhermite(n)); polsturm(H,[-1,1]) - (subst(H,x,1)==0) - (subst(H,x,-1)==0);
T(N)=my(v=List()); for(r=0,N, for(k=-r,r, listput(v, (r+k-(r+k)%2)/2 + (r-k-(r-k)%2)/2))); Vec(v);
t=T(200);
B(m)=t[m+1];
for(n=2,400, if(a(n)!=B(n+4), print("first failure of a(n)=A257564(n+4): n=",n," a=",a(n)," T=",B(n+4)); break));
for(n=2,400, if(a(n)!=B(n+2), print("first failure of a(n)=A257564(n+2): n=",n," a=",a(n)," T=",B(n+2)); break));
