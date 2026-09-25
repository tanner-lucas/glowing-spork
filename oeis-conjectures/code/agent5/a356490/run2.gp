default(nbthreads,1); default(parisizemax, 2*10^9);
P=primes(3000);
T(n)=matrix(n,n,i,j,P[abs(i-j)+1]);
for(n=201,600, d=abs(matdet(T(n))); if(d>1 && ispseudoprime(d), print("n=",n," |det| PRP, digits=",#digits(d))); if(n%25==0, print("done n=",n," digits=",#digits(d))));
