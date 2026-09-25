a(n) = for(k=1, oo, if(Mod(2, n)^k==k, return(k)))
{
foreach([6298, 51169], n, t=getabstime(); v=a(n); print("n=",n,"  a(n)=",v,"  prime(n)=",prime(n),"  a(n)<prime(n)? ",v<prime(n), "  check (2^a-a)%n=",(Mod(2,n)^v-v), "  factor(n)=",factor(n), "  time ",getabstime()-t,"ms"));
}
