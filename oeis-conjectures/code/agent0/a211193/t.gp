N=600; x='x+O('x^(N+1)); v=Vec(serlaplace(exp((1+x)^(1+x)-1)));
print(vector(12,i,v[i]));
bad=[]; for(n=2,N, if((v[n+1]-1)%n!=0, bad=concat(bad,n))); print("n<=",N," with a(n)!=1 mod n: ", bad);
quit
