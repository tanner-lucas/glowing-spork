\\ Construct n with phi(2n)+phi(2n+2) > phi(2n-1)+phi(2n+1)  (violates a(2n) <= a(2n-1) in A362334)
default(parisize, 10^8);
{
B = 150;
P = select(p->p>2, primes([3,B]));
P1=List(); P2=List(); r1=1.; r2=1.;
listput(P2,3); r2*=2/3;
for(i=2,#P, p=P[i]; if(r1>=r2, listput(P1,p); r1*=(1-1/p), listput(P2,p); r2*=(1-1/p)));
A1=prod(i=1,#P1,P1[i]); A2=prod(i=1,#P2,P2[i]);
print("P1=",Vec(P1)); print("P2=",Vec(P2));
print("ratio1=",r1," ratio2=",r2," sum=",r1+r2);
c = chinese([Mod(lift(Mod(1,A1)/2),A1), Mod(lift(Mod(-1,A2)/2),A2), Mod(1,4)]);
M = c.mod; n0 = lift(c);
print("M has ", #digits(M), " digits");
found=0;
for(t=0, 10^7, n = n0 + t*M; s=(n+1)/2;
  if(!ispseudoprime(n), next); if(!ispseudoprime(s), next);
  q1=(2*n-1)/A1; q2=(2*n+1)/A2;
  if(!ispseudoprime(q1) || !ispseudoprime(q2), next);
  lhs = eulerphi(2*n)+eulerphi(2*n+2); rhs = eulerphi(2*n-1)+eulerphi(2*n+1);
  print("t=",t); print("n=",n); print("q1=",q1); print("q2=",q2); print("lhs=",lhs); print("rhs=",rhs); print("lhs>rhs: ", lhs>rhs, "  rhs/lhs=", 1.*rhs/lhs);
  found=1; break);
if(!found, print("none found"));
}
