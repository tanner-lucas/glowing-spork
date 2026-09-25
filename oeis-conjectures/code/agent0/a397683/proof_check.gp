\\ witness mod p^k (p>=5, p!=7): consecutive primitive roots g,g+1 mod p, lifted so both are primitive roots mod p^2
wpk(p,k)={ my(q=p^k);
  for(g=1,p-2, if(znorder(Mod(g,p))==p-1 && znorder(Mod(g+1,p))==p-1,
     for(t=0,p-1, my(x=g+t*p); if(Mod(x,p^2)^(p-1)!=1 && Mod(x+1,p^2)^(p-1)!=1, return(x%q)))));
  error("no witness p=",p);
}
build(m)={ my(f=factor(m),a=0,b=0,res=[],mods=[]);
  for(i=1,#f~, my(p=f[i,1],k=f[i,2]);
     if(p==3, a=k, if(p==7, b=k, res=concat(res,[Mod(wpk(p,k),p^k)]))));
  my(s=m/(3^a*7^b));
  if(a>=1 && b>=1, if(a==1, res=concat(res,[Mod(1,3),Mod(3,7^b)]), res=concat(res,[Mod(4,3^a),Mod(5,7^b)])),
   if(a>=1, res=concat(res,[if(a==1,Mod(1,3),Mod(4,3^a))]));
   if(b>=1, res=concat(res,[Mod(3,7^b)])));
  lift(chinese(res));
}
bad=0; cnt=0;
{forstep(m=3,200001,2, my(f=factor(m),x); if(#f~==1 && (f[1,1]==3||f[1,1]==7), next);
  x=build(m); cnt++;
  if(gcd(x,m)!=1||gcd(x+1,m)!=1||znorder(Mod(x,m))!=znorder(Mod(x+1,m)), bad++; print("FAIL m=",m," x=",x)));}
print("constructed witnesses checked for ",cnt," odd m<=200001 (non 3/7-powers); failures=",bad);
\\ brute force f(m) for m powers of 3 and 7
f(m)=sum(x=1,m-1,(gcd(x,m)==1)&&(gcd(x+1,m)==1)&&(znorder(Mod(x,m))==znorder(Mod(x+1,m))));
print("f(3^k), k=1..9: ",vector(9,k,f(3^k)));
print("f(7^k), k=1..5: ",vector(5,k,f(7^k)));
\\ reproduce data
print(vector(40,n,if(n==1,1,f(2*n-1))));
quit
