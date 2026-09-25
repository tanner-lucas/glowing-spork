// A072872: a(n) = least k>=1 with n | 2^k - k. Conjecture: n>47 => a(n) < prime(n).
// For each n search k up to prime(n); report n with no k < prime(n) (i.e. a(n) >= prime(n)).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); int printfirst=argc>2?atoi(argv[2]):0;
  // primes up to ~ N*(ln N + ln ln N)+100
  long L=(long)(N*25.0)+1000; char*c=calloc(L+1,1); long*pr=malloc(sizeof(long)*(N+2)); long np=0;
  for(long i=2;i<=L && np<=N;i++){ if(!c[i]){ pr[np++]=i; for(long j=i*i;j<=L;j+=i) c[j]=1; } }
  if(np<N){fprintf(stderr,"sieve too small\n");return 1;}
  for(long n=1;n<=N;n++){
    long P=pr[n-1]; // prime(n)
    uint64_t t=2%n, km=1%n; long k=1; long found=0;
    long lim = (n<=printfirst)? 100000000L : P-1;
    for(k=1;k<=lim;k++){ if(t==km){found=k;break;} t<<=1; if(t>=(uint64_t)n) t-=n; km++; if(km==(uint64_t)n) km=0; }
    if(n<=printfirst) printf("%ld ",found);
    else if(!found && n>47) { printf("\nn=%ld: a(n) >= prime(n)=%ld\n",n,P); fflush(stdout);} 
  }
  printf("\ndone N=%ld\n",N);
}
