default(parisizemax, 2*10^9);
P=primes(2000);
T(n)=matrix(n,n,i,j,P[abs(i-j)+1]);
\\ reproduce data
print(vector(13,n,matdet(T(n-1+(n==1)))));
for(n=1,700, d=abs(matdet(T(n))); if(d>1 && ispseudoprime(d), print("n=",n," |det| PRP, digits=",#digits(d))); if(n%50==0, print("done n=",n," digits=",#digits(d))));
