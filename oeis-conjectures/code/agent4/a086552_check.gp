first(n, lim) = { my(tp=1, t); for(x=2, lim, t=numdiv(x); if(t % tp == 0 && t/tp == n, return(x)); tp=t); 0 }
{
x = first(17, 1000000);
print("n=17: smallest x = ", x, "  factor(x)=", factor(x), "  numdiv(x)=", numdiv(x), "  x-1=", x-1, " factor=", factor(x-1), " numdiv=", numdiv(x-1), " isprime(x-1)=", isprime(x-1));
\\ numbers < x with tau = 34 and x-1 prime would be the natural candidates; list tau=34 numbers below x and their x-1 factorizations
forstep(q=2, 20, 1, if(isprime(q), my(y=2^16*q); if(y<x, print("  2^16*",q,"=",y," y-1=",y-1," factor=",factor(y-1)))));
}
