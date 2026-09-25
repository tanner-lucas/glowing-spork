v=readvec("/home/user/work/agent5/b050414.vec");
print(#v, " max ", vecmax(v));
for(i=1,#v, n=v[i]; if(n%2==0 && issquare(n/2,&m) && isprime(n+1), print("hit n=",n," m=",m)));
