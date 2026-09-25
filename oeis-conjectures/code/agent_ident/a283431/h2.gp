a(n)=my(H=polhermite(n)); polsturm(H,[-1,1]) - (subst(H,x,1)==0) - (subst(H,x,-1)==0);
T(N)=my(v=List()); for(r=0,N, for(k=-r,r, listput(v, (r+k-(r+k)%2)/2 + (r-k-(r-k)%2)/2))); Vec(v);
t=T(200);
A=vector(301,i,a(i-1));
for(s=0,6, f=-1; for(n=0,300, if(A[n+1]!=t[n+s+1], f=n; break)); print("shift ",s," first failure n=",f));
print(vector(40,i,A[80+i]));
print(vector(40,i,t[84+i]));
