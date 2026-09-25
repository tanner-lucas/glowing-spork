\\ Independent re-verification of the counterexamples reported in README.md.
\\ Run:  gp -q verify_counterexamples.gp     (PARI/GP >= 2.13; takes a minute or two)
default(realprecision, 120);
ok(name, cond) = print(if(cond, "PASS  ", "FAIL  "), name);

\\ A100682: floor(binomial(N,4)^(1/4)) = floor((N-3/2)/24^(1/4)) conjectured except N in {0,1,6,17,2403,5318}
{c = sqrtn(24,4);
 foreach([634027531, 1705327318, 55292025086], N,
   ok(Str("A100682 new exception N=", N), sqrtnint(binomial(N,4),4) != floor((N-3/2)/c)));}

\\ A071622: a(n) = -Sum_{k<=n} (-1)^floor((4/3)^k); conjecture a(n) > log(n)^2 for n > 2300
{my(a=0, first=0, zero=0);
 for(k=1, 18966, a -= (-1)^(4^k \ 3^k);
   if(k>2300 && !first && a <= log(k)^2, first=[k,a]);
   if(k>2300 && !zero && a==0, zero=k));
 ok(Str("A071622 first failure n=", first[1], " a=", first[2], " log(n)^2=", strprintf("%.4f", log(first[1])^2)), first[1]==16954);
 ok(Str("A071622 a(18966)=0"), zero==18966);}

\\ A066803: a(n) = gcd(2^n+1, 3^n+1); conjecture a(2^k) = 1 for k != 1
{my(p=3*2^41+1);
 ok("A066803: p=3*2^41+1 prime, 2^(2^38) = 3^(2^38) = -1 mod p  => a(2^38) >= p",
    isprime(p) && Mod(2,p)^(2^38)==-1 && Mod(3,p)^(2^38)==-1);
 p=21*2^41+1;
 ok("A066803: p=21*2^41+1 likewise divides a(2^39)",
    isprime(p) && Mod(2,p)^(2^39)==-1 && Mod(3,p)^(2^39)==-1);}

\\ A103225: # Gaussian integers z, |z|<n, gcd(n,z)=1; conjecture a(n) < Pi*n^2.
\\ n=6203 is a rational prime = 3 mod 4, hence a Gaussian prime, so a(n) = #{z : |z|<n} - 1.
{my(n=6203, a);
 a = sum(x=-n+1, n-1, 2*sqrtint(n^2-1-x^2)+1) - 1;
 ok(Str("A103225 a(6203)=", a, " > Pi*6203^2=", strprintf("%.4f", Pi*n^2)), isprime(n) && n%4==3 && a > Pi*n^2);}

\\ A284364/5/6 and A220956 need long computations; see code/ (C programs) and README.md.
