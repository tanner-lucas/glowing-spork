{
\\ composite n with (n-1)^(n+1)+1 possibly prime must be n=2^p-1 composite (see proof in notes)
\\ brute check of the reduction for small n:
bad=List(); for(n=2,300, if(!isprime(n) && ispseudoprime((n-1)^(n+1)+1), listput(bad,n))); print("composite n<=300 with PRP: ",bad);
foreach([4,6,8,9,10,11,12], p, n=2^p-1; t=getabstime(); r=ispseudoprime((n-1)^(n+1)+1); print("p=",p," n=",n," isprime(n)=",isprime(n)," PRP=",r," time ",getabstime()-t,"ms"));
}
