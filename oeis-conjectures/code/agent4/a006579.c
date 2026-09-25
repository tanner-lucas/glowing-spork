// search composite n with Pillai(n) == -1 (mod n), i.e. A006579(n) = Pillai(n)-n == -1 mod n
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long ull; typedef unsigned __int128 u128;
int main(int argc,char**argv){
  uint32_t N=(uint32_t)atoll(argv[1]);
  uint32_t *spf=calloc((size_t)N+1,4);
  for(uint64_t i=2;i<=N;i++) if(!spf[i]){ for(uint64_t j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i; }
  long cnt=0;
  for(uint64_t n=4;n<=N;n++){
    if(spf[n]==n) continue; // prime
    // Pillai multiplicative: P(p^k) = (k+1)p^k - k p^(k-1); compute mod n
    uint64_t m=n; u128 P=1;
    while(m>1){ uint64_t p=spf[m]; int k=0; uint64_t pk=1; while(m%p==0){m/=p;k++;pk*=p;}
      uint64_t val=(uint64_t)(k+1)*pk - (uint64_t)k*(pk/p); P=(P*(val%n))%n; }
    if((uint64_t)P==n-1){ printf("n=%llu\n",(ull)n); cnt++; }
  }
  fprintf(stderr,"done N=%u found=%ld\n",N,cnt);
  return 0;
}
