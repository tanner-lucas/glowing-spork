// For each value v, find least k with phi(k)=v (scan k increasing). If least k is even and later an odd k' has phi(k')=v -> counterexample to "a(n) odd for odd n".
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  uint64_t K=atoll(argv[1]);
  uint32_t *phi=malloc((K+1)*4);
  for(uint64_t i=0;i<=K;i++) phi[i]=i;
  for(uint64_t i=2;i<=K;i++) if(phi[i]==i) for(uint64_t j=i;j<=K;j+=i) phi[j]-=phi[j]/i;
  uint8_t *seen=calloc(K/8+2,1), *evmin=calloc(K/8+2,1);
  uint32_t *firstk=NULL; // store first k for even-min values only via small hash? just report
  long cnt=0, evcount=0;
  for(uint64_t k=1;k<=K;k++){
    uint32_t v=phi[k];
    if(!(seen[v>>3]&(1<<(v&7)))){ seen[v>>3]|=1<<(v&7); if(!(k&1)){ evmin[v>>3]|=1<<(v&7); evcount++; fprintf(stderr,"even least preimage k=%llu v=%u\n",(unsigned long long)k,v);}  }
    else if((k&1) && (evmin[v>>3]&(1<<(v&7)))){ printf("COUNTEREX: odd k=%llu phi=%u has even least preimage\n",(unsigned long long)k,v); evmin[v>>3]&=~(1<<(v&7)); cnt++; if(cnt>20) break; }
  }
  fprintf(stderr,"K=%llu done, counterexamples=%ld, values with even least preimage=%ld\n",(unsigned long long)K,cnt,evcount);
}
