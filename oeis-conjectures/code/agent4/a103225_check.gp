\p 60
n=6203;
print("isprime: ", isprime(n), "  n%4=", n%4);
\\ direct: count z=x+y*I with |z|<n and gcd(n,z)==1 using PARI's Gaussian gcd on a sample band, and full count by column sums
\\ Full count: since n is a Gaussian prime, gcd(n,z)!=1 iff n | z; only z=0 in disc.
cnt=sum(x=-n+1,n-1, 2*sqrtint(n^2-1-x^2)+1) - 1;
print("a(6203) = ", cnt);
print("Pi*n^2  = ", Pi*n^2);
print("a - Pi*n^2 = ", cnt - Pi*n^2);
\\ spot-check that PARI's gcd agrees that n is a Gaussian prime: factor over Z[i]
print("factor(n+0*I) = ", factor(n+0*I));
