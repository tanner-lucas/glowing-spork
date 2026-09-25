N=2^30;
print("2^49-1 == 127*4432676798593 : ", 2^49-1 == 127*4432676798593);
print("isprime(4432676798593) : ", isprime(4432676798593), "  (proof-level, PARI isprime is APR-CL/ECPP certified)");
print("4432676798593 > 2*N : ", 4432676798593 > 2*N);
print("M31 collision: ((2^30)^2-(2^30-1)^2) % (2^31-1) = ", ((2^30)^2-(2^30-1)^2) % (2^31-1));
\\ explicit collisions for every m in [2,48]: pick divisor pair d<e with (d+e)/2 <= N
ok=1;
for(m=2,48, M=2^m-1; found=0;
  fordiv(M,d, if(d*d<M && (d+M/d)/2<=N, e=M/d; j=(d+e)/2; i=(e-d)/2;
     if(i>=1 && j<=N && (j^2-i^2)%M==0, found=[i,j]; break)));
  if(found==0, ok=0; print("m=",m," no collision found"), print("m=",m,"  ",found[2],"^2 == ",found[1],"^2 mod 2^",m,"-1")));
print("all m<=48 have collisions within 1..2^30: ", ok);
