default(parisizemax, 2000000000);
N=160; x='x+O('x^(N+1));
S=sum(k=0,N, tanh(k*x)^k);
v=Vec(serlaplace(S));
print(vector(9,i,v[i]));
for(i=1,#v, if(denominator(v[i])!=1, print("nonint at ",i-1)));
res=[];
forprime(p=3,79, my(ok=1); for(n=1,N-(p-1), if((v[n+1]-v[n+p])%p, ok=0; print("A221077 p=",p," fails at n=",n); break)); res=concat(res,[[p,ok]]));
print(res);
\\ A195415: a(n) = A221077(n)/4^(n-1)
w=vector(N,n,v[n+1]/4^(n-1)); for(n=1,N, if(denominator(w[n])!=1, print("A195415 nonint ",n)));
res2=[]; forprime(p=3,79, my(ok=1); for(n=1,N-(p-1), if((w[n]-w[n+p-1])%p, ok=0; print("A195415 p=",p," fails at n=",n); break)); res2=concat(res2,[[p,ok]])); print(res2);
quit
