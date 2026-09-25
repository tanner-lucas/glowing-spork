default(parisize,2*10^8); default(nbthreads,1);
a(m)=eulerphi(m)+eulerphi(m+2);
{
n=134012348126107206688690603701275719891017841718586793654900333;
k=2*n;
print("k = ",k);
print("isprime(n)=",isprime(n)," isprime((n+1)/2)=",isprime((n+1)/2));
print("factor(k-1) = ",factor(k-1));
print("factor(k+1) = ",factor(k+1));
print("factor(k)   = ",factor(k));
print("factor(k+2) = ",factor(k+2));
print("a(k)   = ",a(k));
print("a(k-1) = ",a(k-1));
print("a(k) > a(k-1): ", a(k)>a(k-1), "   difference = ", a(k)-a(k-1));
}
