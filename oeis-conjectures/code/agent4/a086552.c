#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  uint64_t N=atoll(argv[1]);
  uint16_t *t=malloc((N+1)*2);
  for(uint64_t i=0;i<=N;i++) t[i]=1;
  // tau via sieve of smallest prime powers: use divisor-count multiplicative sieve with spf
  uint32_t *spf=calloc(N+1,4);
  for(uint64_t i=2;i<=N;i++) if(!spf[i]) for(uint64_t j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
  for(uint64_t n=2;n<=N;n++){ uint64_t p=spf[n], m=n; int e=0; while(m%p==0){m/=p;e++;} t[n]=t[m]*(e+1); }
  free(spf);
  uint64_t first[2000]={0};
  for(uint64_t x=2;x<=N;x++){ if(t[x]%t[x-1]==0){ uint32_t r=t[x]/t[x-1]; if(r<2000 && !first[r]) first[r]=x; } }
  for(int r=2;r<2000;r++) if(first[r]){ uint64_t x=first[r]; printf("n=%d x=%llu tau(x)=%u tau(x-1)=%u %s\n",r,(unsigned long long)x,t[x],t[x-1], t[x-1]==2?"":"<-- x-1 NOT prime"); }
}
