\\ A302975: all terms squares
b=0; for(n=1,100000, my(t=numdiv(n), d=denominator(t^n/n^t)); if(!issquare(d), b++; print("A302975 nonsquare n=",n))); print("A302975 checked n<=1e5, bad=",b);
\\ A270096: a(n)<=n/3 for 8<n<=2e5
a270096(n)={my(m=0); while(Mod(2,n)^m!=Mod(2,n)^n, m++); m};
b=0; for(n=9,20000, if(3*a270096(n)>n, b++; print("A270096 fail ",n))); print("A270096 checked 9..20000 bad=",b);
\\ A305214: A305212(n)!=0 iff 7|n or 9|n
s2c(n)={my(c=Set(vector(n,x,(x-1)^3%n)), S=Set()); for(i=1,#c, for(j=i,#c, S=setunion(S,[(c[i]+c[j])%n]))); n-#S};
b=0; for(n=1,1500, my(z=(s2c(n)!=0)); if(z!=(n%7==0||n%9==0), b++; print("A305214 fail ",n))); print("A305214 checked n<=1500 bad=",b);
\\ A195986 via LTE
b=0; for(n=1,2000, my(v=valuation(5^n-3^n,2), w=valuation(3^n-1,2)); if(v!=if(w==1,1,w+1), b++)); print("A195986 check (A090740 as v2(3^n-1)) bad=",b);
\\ A160627 numerators odd
b=0; for(n=0,600, my(L=sum(k=0,n,binomial(n,k)*(-4)^k/k!)); if(numerator(L)%2==0, b++)); print("A160627 n<=600 even numerators: ",b);
\\ A363151 cubefree
b=0; for(n=0,400, my(s=sum(j=0,n,subst(bernpol(j),x,1)*subst(bernpol(n-j),x,1)), d=denominator(s), f=factor(d)); if(#f~ && vecmax(f[,2])>=3, b++)); print("A363151 n<=400 non-cubefree: ",b);
quit
