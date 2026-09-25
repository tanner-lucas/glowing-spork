#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  int N=atoi(argv[1]); uint64_t M=(uint64_t)atoll(argv[2]);
  uint32_t *phi=malloc((M+1)*4); for(uint64_t i=0;i<=M;i++) phi[i]=i;
  for(uint64_t i=2;i<=M;i++) if(phi[i]==i) for(uint64_t j=i;j<=M;j+=i) phi[j]-=phi[j]/i;
  // primes
  int *p=malloc(sizeof(int)*(N+2)); int np=0; for(uint64_t i=2;np<N;i++) if(phi[i]==i-1) p[np++]=i;
  int cnt[4096]={0}; uint64_t maxv=0;
  for(int n=1;n<=N;n++){
    uint64_t t=phi[p[n-1]];
    for(int k=n-2;k>=0;k--){ uint64_t x=p[k]+t; if(x>M){fprintf(stderr,"overflow n=%d\n",n);return 1;} if(x>maxv) maxv=x; t=phi[x]; }
    if(n<=25) printf("%llu,",(unsigned long long)t);
    if(t<4096) cnt[t]++; else printf("\nlarge value n=%d a=%llu\n",n,(unsigned long long)t);
    if(n>=187 && t!=20 && t!=64) printf("\nConj2 violation n=%d a=%llu\n",n,(unsigned long long)t);
  }
  printf("\nvalue counts:"); for(int v=0;v<4096;v++) if(cnt[v]) printf(" %d:%d",v,cnt[v]); printf("\nmax arg %llu\n",(unsigned long long)maxv);
}
