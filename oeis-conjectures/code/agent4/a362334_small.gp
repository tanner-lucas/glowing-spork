default(parisize, 10^8);
default(nbthreads,1);
\\ try to find smaller counterexample to a(2n) <= a(2n-1): best balanced partition via exhaustive search over subsets for small B
best(B)={ my(P=select(p->p>3, primes([5,B])), n=#P, bestv=10., bestS=0, v1, v2);
  for(mask=0, 2^n-1, v1=1.; v2=2/3; for(i=1,n, if(bittest(mask,i-1), v1*=(1-1/P[i]), v2*=(1-1/P[i]))); if(v1+v2<bestv, bestv=v1+v2; bestS=mask));
  [bestv, bestS, P] }
{
for(B=61, 97, if(!isprime(B), next);
  my(r=best(B), P=r[3], S=r[2], A1=1, A2=3);
  for(i=1,#P, if(bittest(S,i-1), A1*=P[i], A2*=P[i]));
  my(c=chinese([Mod(lift(Mod(1,A1)/2),A1), Mod(lift(Mod(-1,A2)/2),A2), Mod(1,4)]), M=c.mod, n0=lift(c), hit=0);
  for(t=0, 2*10^6, my(n=n0+t*M); if(n<3, next);
     my(k=2*n, lhs=eulerphi(k)+eulerphi(k+2));
     if(!ispseudoprime(n), next);
     my(rhs=eulerphi(k-1)+eulerphi(k+1));
     if(lhs>rhs, print("B=",B," sum rho=",r[1]," n=",n," (",#digits(n)," digits)  a(k)=",lhs," a(k-1)=",rhs); hit=1; break));
  if(!hit, print("B=",B," sum rho=",r[1]," none")));
}
