{
N=2^30; ok=1;
for(m=2,48, M=2^m-1; found=0;
  fordiv(M,d, if(d*d<M && (d+M/d)/2<=N, e=M/d; j=(d+e)/2; i=(e-d)/2;
     if(i>=1 && j<=N && (j^2-i^2)%M==0, found=[i,j]; break)));
  if(found==0, ok=0; print("m=",m," no collision found"), print("m=",m,"  ",found[2],"^2 == ",found[1],"^2 mod 2^",m,"-1")));
print("all m<=48 have collisions within 1..2^30: ", ok);
}
