N=1200; x='x+O('x^(N+1)); v=Vec(serlaplace(cosh(x)/(1-2*sinh(x))));
print(vector(8,i,v[i]));
b1=[]; forprime(p=3,N, if((v[p+1]-2)%p, b1=concat(b1,p))); print("primes p<=",N," with a(p)!=2 mod p: ",b1);
b2=[]; for(m=1,10, if(2^m<=N && (v[2^m+1]-1)%(2^m), b2=concat(b2,m))); print("m with a(2^m)!=1 mod 2^m: ",b2);
quit
