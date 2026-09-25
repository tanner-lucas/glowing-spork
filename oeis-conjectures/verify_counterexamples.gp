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


\\ A073631: nonprimes k with k | 3^(k-1)-2^(k-1); conjecture: nonsquarefree terms are multiples of 23^2
{my(p=3842760169, k=p^2);
 ok("A073631: k=3842760169^2 is a term, nonsquarefree, not a multiple of 529",
    isprime(p) && Mod(3,k)^(k-1)==Mod(2,k)^(k-1) && k%529!=0);}

\\ A376360: positions of numbers in A007961 (greedy base of squares) ending in 3; conjecture: gap 12 never occurs
lastdig(n)={my(r=n); forstep(m=sqrtint(n),2,-1, r%=m^2); r};
{my(L=[n | n<-[336391..336403], lastdig(n)==3]);
 ok(Str("A376360: consecutive terms 336391, 336403 (gap 12); terms in between: ", L), L==[336391,336403]);}

\\ A225577 (Z.-W. Sun): a(n) = least m>1 with 1^2..n^2 pairwise incongruent mod 2^m-1.
\\ Conjecture: a(n) = least p with 2^p-1 a Mersenne prime > 2n-1. At n=2^30 that predicts 61 (2^31-1 = 2n-1).
coll(M,n)={my(D=divisors(M)); for(t=1,#D, my(d=D[t],e=M/d); if(d<e && (d+e)%2==0 && (e+d)/2<=n, return(1))); 0};
{my(n=2^30, f=factor(2^49-1), okc=1);
 for(m=2,48, if(!coll(2^m-1,n), okc=0));
 ok("A225577: collisions mod 2^m-1 for all m<=48, none mod 2^49-1 (prime factor 4432676798593 > 2n) => a(2^30)=49, not 61",
    okc && f[#f~,1] > 2*n && 2^31-1 == 2*n-1);
 \\ Sun's Fibonacci version: n=(F(47)+1)/2; least Fibonacci modulus is composite F(65), not F(83)
 n=(fibonacci(47)+1)/2; okc=1;
 for(k=48,64, if(!coll(fibonacci(k),n) && !(k==51||k==57||k==63), okc=0));
 foreach([[51,6374424,6377618],[57,229255976,229257570],[63,599069104,599080050]], v,
   if((v[3]^2-v[2]^2)%fibonacci(v[1]) || v[3]>n, okc=0));
 f=factor(fibonacci(65));
 ok("A225577 (Fibonacci): collisions mod F(48..64), none mod F(65)=5*233*14736206161 => least is F(65), not F(83)",
    okc && f[#f~,1] > 2*n && isprime(fibonacci(47)) && fibonacci(47)==2*n-1);}

\\ A126762 (Ordowski): least k>n with n^k=n (mod k) conjectured to equal least k>n with n^(k-1)=1 (mod k)
a1(n)={my(k=n+1); while(Mod(n,k)^k!=Mod(n,k), k++); k};
a2(n)={my(k=n+1); while(Mod(n,k)^(k-1)!=Mod(1,k), k++); k};
{ok("A126762: n=363 gives 366 vs 367", a1(363)==366 && a2(363)==367);}

\\ A072872 (Cloitre): a(n) = least k with n | 2^k-k; conjecture a(n) < prime(n) for n > 47
a072872(n)={for(k=1,oo, if(Mod(2,n)^k==k, return(k)))};
{ok(Str("A072872: a(6298)=", a072872(6298), " > prime(6298)=", prime(6298)), a072872(6298) > prime(6298));}

\\ A114782 (Murthy): conjecture a(n)=0 iff prime(n)+1 = 0 (mod 3). p=48247=prime(4966) is 1 mod 3,
\\ but 10^k+p is always divisible by one of 7,11,13,37 (covering set, period 6), so a(4966)=0.
{my(p=48247);
 ok("A114782: prime(4966)=48247, p=1 mod 3, covering set {7,11,13,37} for 10^k+p",
    prime(4966)==p && p%3==1 && #[j | j<-[0..5], #[q | q<-[7,11,13,37], Mod(10,q)^j+p==0]==0]==0);}

\\ A362334: a(n)=phi(n)+phi(n+2); conjecture a(2n) <= a(2n-1) and a(2n) < a(2n+1). CRT-built counterexamples:
{my(n=134012348126107206688690603701275719891017841718586793654900333, k=2*n, A(x)=eulerphi(x)+eulerphi(x+2));
 ok("A362334 part 1: a(k) > a(k-1) for a 63-digit even k", A(k) > A(k-1));
 n=539414769491017837931500222298531509788246672344348812944989101; k=2*n;
 ok("A362334 part 2: a(k) >= a(k+1) for a 63-digit even k", A(k) >= A(k+1));}
