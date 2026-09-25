default(parisizemax, 1000000000);
f(m) = my(F=factor(m)); sum(i=1,#F~, F[i,1]+F[i,2]);
\\ A008474: every m in [5,10^6] reaches 5
ok=1; for(m=5,10^6, my(v=m, c=0); while(v!=5, v=f(v); c++; if(c>1000 || v<5, ok=0; print("fail ",m); break))); print("A008474 all m in [5,1e6] reach 5: ", ok);
\\ A160628: denominators of Laguerre(n,4) odd, n<=400
print("A160628 odd denominators n<=400: ", prod(n=0,400, denominator(subst(pollaguerre(n),x,4))%2==1), "  data: ", vector(10,n,denominator(subst(pollaguerre(n-1),x,4))));
\\ A363152: cubefree
B1(j) = if(j==1, 1/2, bernfrac(j));
a363(n) = denominator(sum(j=0,2*n, B1(j)*B1(2*n-j)));
print("A363152 data: ", vector(8,n,a363(n-1)), "  cubefree n<=300: ", prod(n=0,300, my(F=factor(a363(n))); #F~==0 || vecmax(F[,2])<=2));
\\ A361033: odd iff n=2^k-1
a361(n) = 3*(4*n)!/(n!*(n+1)!^3);
print("A361033 data ", vector(5,n,a361(n-1)), " parity ok n<=500: ", prod(n=0,500, (a361(n)%2==1) == (hammingweight(n+1)==1)));
\\ A239293: a(n)=n+1 iff n+1 odd composite
a239(n) = my(c=n+1); while(isprime(c) || c<4 || Mod(n,c)^c != n, c++); c;
print("A239293 data ", vector(12,n,a239(n)), " claim ok n<=5000: ", prod(n=1,5000, (a239(n)==n+1) == (n%2==0 && n+1>1 && !isprime(n+1) && n+1>=9)));
\\ A081320
a081(n) = my(F=fibonacci(n)); 2^valuation(F,2)*3^valuation(F,3);
print("A081320 data ", vector(12,n,a081(n)), " claim ok n<=3000: ", prod(n=13,3000, if(n%12, a081(n)==a081(n-12), a081(n)==144*2^valuation(n/12,2)*3^valuation(n/12,3))));
quit;
