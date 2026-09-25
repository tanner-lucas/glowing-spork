a(n) = for(k=n+1, oo, if(Mod(n,k)^k==Mod(n,k), return(k)))
b(n) = for(k=n+1, oo, if(Mod(n,k)^(k-1)==Mod(1,k), return(k)))
{
print("data check: ", vector(74,n,a(n)));
foreach([363,801,2115,3145], n, print("n=",n,"  a(n)=",a(n),"  conj value=",b(n),"  gcd(n,a(n))=",gcd(n,a(n)),"  n^a mod a = ", lift(Mod(n,a(n))^a(n)), "  factor(a(n))=",factor(a(n))));
c=0; for(n=1,1000, if(a(n)!=b(n), c++)); print("number of n<=1000 with a(n)!=conj: ",c);
}
