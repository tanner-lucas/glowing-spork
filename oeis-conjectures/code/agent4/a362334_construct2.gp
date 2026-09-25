default(parisize, 10^8);
default(nbthreads,1);
{
\\ second part: phi(2n)+phi(2n+2) >= phi(2n+1)+phi(2n+3); need 2n+1 = 0 mod A1, 2n+3 = 0 mod A2; 3 must be in A1
B = 150;
P = select(p->p>2, primes([3,B]));
P1=List(); P2=List(); r1=1.; r2=1.;
listput(P1,3); r1*=2/3;
for(i=2,#P, p=P[i]; if(r1>=r2, listput(P1,p); r1*=(1-1/p), listput(P2,p); r2*=(1-1/p)));
A1=prod(i=1,#P1,P1[i]); A2=prod(i=1,#P2,P2[i]);
c = chinese([Mod(lift(Mod(-1,A1)/2),A1), Mod(lift(Mod(-3,A2)/2),A2), Mod(1,4)]);
M = c.mod; n0 = lift(c);
for(t=0, 10^7, n = n0 + t*M; s=(n+1)/2;
  if(!ispseudoprime(n), next); if(!ispseudoprime(s), next);
  q1=(2*n+1)/A1; q2=(2*n+3)/A2;
  if(!ispseudoprime(q1) || !ispseudoprime(q2), next);
  k=2*n; lhs = eulerphi(k)+eulerphi(k+2); rhs = eulerphi(k+1)+eulerphi(k+3);
  print("n=",n); print("k=2n=",k); print("isprime n,s,q1,q2: ",isprime(n),isprime(s),isprime(q1),isprime(q2));
  print("P1=",Vec(P1)," q1=",q1); print("P2=",Vec(P2)," q2=",q2);
  print("a(k)=",lhs); print("a(k+1)=",rhs); print("a(k) < a(k+1)? ", lhs<rhs, "  ratio a(k+1)/a(k)=",1.*rhs/lhs);
  break);
}
