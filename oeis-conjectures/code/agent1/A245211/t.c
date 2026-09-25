#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  uint16_t *tau=calloc(N+1,2); for(long d=1;d<=N;d++) for(long m=d;m<=N;m+=d) tau[m]++;
  uint64_t *G=calloc(N+1,8); for(long d=1;d<=N;d++){ uint64_t v=(uint64_t)d*tau[d]; for(long m=d;m<=N;m+=d) G[m]+=v; }
  for(long n=1;n<=26;n++) printf("%llu,",(unsigned long long)(G[n]-(uint64_t)n*tau[n])); printf("\n");
  for(long n=1;n<=N;n++) if(G[n]-(uint64_t)n*tau[n]==(uint64_t)n) printf("SOLUTION n=%ld\n",n);
  printf("done N=%ld\n",N);
}
