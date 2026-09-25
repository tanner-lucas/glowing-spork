\\ a(n) = least m with sum_{j=k+1}^{k+m} j^n == 0 mod n for all k
A(n)=my(P=n); fordiv(n,d, my(ok=1); for(x=0,n-1, if(Mod(x+d,n)^n!=Mod(x,n)^n, ok=0;break)); if(ok, P=d; break)); my(s=sum(j=1,P,Mod(j,n)^n)); P*(n/gcd(n,lift(s)));
B(n)=if(n%2, 1, my(k=n/2); denominator(bernfrac(2*k)/(2*k))/denominator(bernfrac(2*k)));
rad(n)=factorback(factor(n)[,1]);
d=[1,4,3,8,5,36,7,16,3,20,11,72,13,28,15,32,17,108,19,200,21,44,23,144];
print(vector(#d,n,A(n))==d);
print(vector(24,n,B(n)));
c=0; for(n=1,3000, a=A(n); b=rad(n)*B(n); if(a!=b, print("n=",n," a=",a," conj=",b); c++; if(c>10,break))); print("done");
