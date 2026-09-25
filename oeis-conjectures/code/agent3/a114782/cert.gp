{
p=48247; print("isprime(p)=",isprime(p),"  p%3=",p%3,"  primepi(p)=",primepi(p));
for(r=0,5, print("k==",r," mod 6: ", vector(4,i,[7,11,13,37][i]) , " divides? ", vector(4,i,(10^r+p)%[7,11,13,37][i]==0)));
print("orders of 10 mod 7,11,13,37: ", [znorder(Mod(10,7)),znorder(Mod(10,11)),znorder(Mod(10,13)),znorder(Mod(10,37))]);
\\ brute check k = 5..3000 directly: every 10^k+p has a factor in {7,11,13,37}
ok=1; for(k=5,3000, N=10^k+p; if(N%7 && N%11 && N%13 && N%37, ok=0; print("uncovered k=",k))); print("direct check k=5..3000 all covered: ",ok);
}
