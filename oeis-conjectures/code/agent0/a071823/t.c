#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  uint8_t *cls=calloc(N+1,1); // class of largest prime factor: 1 -> 4k+1, 3 -> 4k+3, 2 -> p=2, 0 -> n=1
  // sieve largest prime factor mod 4: iterate primes ascending, overwrite
  uint8_t *comp=calloc(N+1,1);
  for(long p=2;p<=N;p++){ if(comp[p]) continue; for(long j=p*p;j<=N && j>0;j+=p) comp[j]=1; uint8_t c=(p==2)?2:(p%4); for(long j=p;j<=N;j+=p) cls[j]=c; }
  long a=0; double minv=1e18; long argmin=0; long fails=0; long firstfail=0;
  int data[]={0,0,1,1,1,2,3,3,4,4,5,6,6,7,7,7,7,8,9,9,10,11,12,13,13,13,14,15,15};
  for(long n=1;n<=N;n++){ if(cls[n]==3) a++; if(n<=29 && a!=data[n-1]) printf("MISMATCH %ld\n",n);
    if(n>1000){ double v=(a-n/2.0)-sqrt((double)n); if(v<minv){minv=v;argmin=n;} if(v<=0){fails++; if(!firstfail) firstfail=n;} } }
  printf("N=%ld min (a(n)-n/2-sqrt(n)) over n>1000: %.3f at n=%ld; fails=%ld first=%ld\n",N,minv,argmin,fails,firstfail);
}
