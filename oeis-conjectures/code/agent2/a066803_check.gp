p = 3*2^41+1;
print("p = ", p, "  isprime: ", isprime(p), "  (BPSW) ; isprime(p,1) certificate: ", isprime(p,1));
print("Mod(2,p)^(2^38) = ", lift(Mod(2,p)^(2^38)), "   (p-1 = ", p-1, ")");
print("Mod(3,p)^(2^38) = ", lift(Mod(3,p)^(2^38)));
print("znorder(Mod(2,p)) = ", znorder(Mod(2,p)), " = 2^", valuation(znorder(Mod(2,p)),2));
print("znorder(Mod(3,p)) = ", znorder(Mod(3,p)), " = 2^", valuation(znorder(Mod(3,p)),2));
\\ direct gcd for small k
for(k=0,20, N=2^k; g=gcd(2^N+1,3^N+1); print("k=",k," a(2^k)=",g));
