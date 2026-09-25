default(parisizemax, 1500000000);
cnt(n) = {my(P=bernpol(n), c=0, extra=0);
  \\ remove exact roots at 0,1/2,1 when present (odd n>=3); note root at 1 is on the circle, not inside
  if(n%2==1 && n>=3, P = P/(x*(x-1/2)*(x-1)); extra=2);
  localprec(max(60, 3*n)); my(R=polroots(P));
  for(i=1,#R, my(m=abs(R[i])); if(abs(m-1)<1e-20, print("near-circle root n=",n," |z|=",m)); if(m<1, c++));
  c+extra};
v=vector(80,n,cnt(n-1)); print(v);
bad=List(); for(n=64,500, my(c=cnt(n)); if(c != if(n%2,3,4), listput(bad,[n,c]))); print("violations n in [64,500]: ", bad);
quit;
