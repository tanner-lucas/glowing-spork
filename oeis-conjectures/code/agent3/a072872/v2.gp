a(n) = for(k=1, oo, if(Mod(2, n)^k==k, return(k)))
{
n=148755; v=a(n); print("n=",n,"  a(n)=",v,"  prime(n)=",prime(n),"  a(n)>prime(n)? ",v>prime(n),"  factor(n)=",factor(n));
}
