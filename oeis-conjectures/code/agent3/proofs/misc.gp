default(parisizemax, 2*10^9)
sq(n)=my(f=factor(n));prod(i=1,#f[,1],if(f[i,1]==2,2^f[i,2]\6+2,f[i,1]^(f[i,2]+1)\(2*f[i,1]+2)+1))
a277(n)=my(ph=eulerphi(n));for(m=0,4*n,my(ok=1);for(b=0,n-1,if(Mod(b,n)^m!=Mod(b,n)^ph,ok=0;break));if(ok,return(m)))
{
\\ A000224 formula vs brute for n<=300
print("sq formula ok: ", vector(300,n, #Set(vector(n,k,k^2%n)))==vector(300,n,sq(n)));
T=select(n->sq(n)==ceil((n+1)/4), vector(2*10^5,i,i)); print("A123723 first terms: ",T[1..20]);
bad=select(t->t%4==0 && t>4 && !isprime(t/4), T); print("terms divisible by 4, >4, with t/4 not prime (<=2e5): ",bad);
print("A277030 brute vs lambda for n<=400: exceptions ", select(n->a277(n)>lcm(znstar(n).cyc), vector(399,i,i+1)));
}
