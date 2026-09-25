default(nbthreads,1);
vp(m,p)=my(s=0);while(m,m\=p;s+=m);s;
a(n)=my(best=oo);forprime(p=2,n,best=min(best,vp(n^2,p)\vp(n,p)));best;
print(vector(25,n,a(n+1)));
bad=0; for(n=2,20000, t=(a(n)==n+1); if(t!=(isprimepower(n)>0), bad++; print("mismatch ",n)); if(a(n)<n+1, print("below n+1 at ",n))); print("mismatches: ",bad);
