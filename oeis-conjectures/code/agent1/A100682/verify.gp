\p 100
f(N) = sqrtnint(binomial(N,4),4);
g(N) = floor((N-3/2)/24^(1/4));
{
for(i=1,1,
  foreach([6,17,2403,5318,634027531,1705327318,55292025086], N,
    print(N, "  sqrtnint(C(N,4),4)=", f(N), "  floor((N-3/2)/24^(1/4))=", g(N), "  (N-3/2)/24^(1/4)=", (N-3/2)/24^(1/4)*1.0));
  \\ direct certificate: k^4 > C(N,4) while 384*k^4 <= (2N-3)^4
  foreach([[634027531,286454273],[1705327318,770468590],[55292025086,24980992325]], v, N=v[1]; k=v[2];
    print(N, ": C(N,4) < k^4 ? ", binomial(N,4) < k^4, "   384*k^4 <= (2N-3)^4 ? ", 384*k^4 <= (2*N-3)^4, "  C(N,4) >= (k-1)^4 ? ", binomial(N,4) >= (k-1)^4));
)}
\\ brute force independent check of all N up to 2*10^6
{
my(ex=List(), c=24^(1/4));
for(N=2, 2*10^6, if(sqrtnint(binomial(N,4),4) != floor((N-3/2)/c), listput(ex,N)));
print("exceptions N in [2,2e6]: ", ex);
}
