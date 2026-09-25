{
n=1485607537; F47=fibonacci(47);
print("n = (F_47+1)/2 : ", n==(F47+1)/2, "   F_47 prime: ", isprime(F47));
print("F_65 = ", fibonacci(65), " = ", factor(fibonacci(65)));
q=14736206161; print("q prime: ", isprime(q), "  q > 2n: ", q>2*n, "  q | F_65: ", fibonacci(65)%q==0);
ok=1;
for(k=3,64, m=fibonacci(k); found=0;
  for(i=1,1, fordiv(m,d, for(s=1,3,for(t=1,3, u=d*s; v=(m/d)*t; if(u<v && (u-v)%2==0 && (u+v)/2<=n, found=[(v-u)/2,(u+v)/2]; break(3)))))); 
  if(found==0, ok=0; print("k=",k," NO collision"), if((found[2]^2-found[1]^2)%m, ok=0; print("bad cert k=",k))));
print("every F_k, 3<=k<=64, has an explicit collision i<j<=n: ", ok);
print("Fibonacci primes F_k, k<=100: ", select(k->isprime(fibonacci(k)), vector(98,i,i+2)));
}
