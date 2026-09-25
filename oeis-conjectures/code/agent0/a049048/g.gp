B=2500; F=vector(B,n,n!-1); cnt=0;
{for(n2=3,B, for(n1=2,n2-1,
  my(g=gcd(F[n1],F[n2]));
  if(g>1, forprime(p=2,n2, while(g%p==0, g/=p));
    if(g>1 && !ispseudoprime(g), cnt++; print("CANDIDATE n1=",n1," n2=",n2," cofactor=",g)))));}
print("done B=",B," candidates=",cnt);
quit
