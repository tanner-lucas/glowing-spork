\\ H(m) = least j such that i^2 == j^2 (mod m) for some 1<=i<j ; squares 1..n distinct mod m iff n < H(m)
H(m)={my(best=oo);fordiv(m,d,for(s=1,3,for(t=1,3,my(u=d*s,v=(m/d)*t);if(u<v && (u-v)%2==0, best=min(best,(u+v)/2)))));best}
{
for(k=3,100, F=fibonacci(k); h=H(F); print(k," ",F," ",isprime(F)," ",h));
}
