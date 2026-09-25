default(nbthreads,1);
a(n)=lift(Mod(binomial(2*n,n)-binomial(2*n-2,n-1),n^2))-n-2;
z=select(n->a(n)==0, vector(3000,n,n)); print("zeros n<=3000 that are not odd primes: ", select(n->!(isprime(n)&&n>2), z));
print(vector(20,n,a(n)));
