first(n, lim) = { my(tp=1, t); for(x=2, lim, t=numdiv(x); if(t % tp == 0 && t/tp == n, return(x)); tp=t); 0 }
{
foreach([34,23], n, x = first(n, 70000000);
print("n=",n,": smallest x = ", x, "  factor(x)=", factor(x), "  numdiv(x)=", numdiv(x), "  x-1=", x-1, " factor=", factor(x-1), " isprime(x-1)=", isprime(x-1)));
}
