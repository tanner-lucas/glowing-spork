{
U=[2971, 9811, 15817, 20089, 25609, 28909, 33331, 35311, 35839, 37159, 37357];
\\ primes q whose order of 10 divides L, collected from factorizations of 10^d-1, d|L
for(t=1,1, 
foreach([12,18,24,30,36,40,48,60,72,120,144], L,
  Q=[]; fordiv(L,d, f=factor(polcyclo(d,10))[,1]; Q=concat(Q,f~)); Q=Set(Q); Q=setminus(Q,[3]);
  foreach(U,p, cov=vector(L); foreach(Q,q, if(q==2||q==5,next); for(k=0,L-1, if(!cov[k+1] && (Mod(10,q)^k+p)==0, cov[k+1]=1)));
     if(vecmin(cov)==1, print("p=",p," COVERED with L=",L)));
  print("done L=",L," #Q=",#Q)));
}
