#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  int N=atoi(argv[1]); uint64_t M=(uint64_t)atoll(argv[2]);
  uint32_t *phi=malloc((M+1)*4); for(uint64_t i=0;i<=M;i++) phi[i]=i;
  for(uint64_t i=2;i<=M;i++) if(phi[i]==i) for(uint64_t j=i;j<=M;j+=i) phi[j]-=phi[j]/i;
  int *p=malloc(sizeof(int)*(N+2)); int np=0; for(uint64_t i=2;np<N;i++) if(phi[i]==i-1) p[np++]=i;
  uint32_t *prev=calloc(N+2,4); // prev[k] = value t_k for previous n's chain (0 = none)
  uint32_t *res_at=calloc(N+2,4); // not needed
  int cnt[4096]={0}; uint64_t maxv=0; long steps=0; uint32_t lastres=0;
  for(int n=1;n<=N;n++){
    uint64_t t=phi[p[n-1]]; int k=n-2; int merged=0;
    // chain value at level n-1 is t
    for(;k>=0;k--){ uint64_t x=p[k]+t; if(x>M){fprintf(stderr,"overflow n=%d\n",n);return 1;} if(x>maxv) maxv=x; t=phi[x]; steps++;
      if(prev[k]==t){ merged=1; break; } prev[k]=t; }
    uint32_t a = merged ? lastres : (uint32_t)t;
    // if merged, lower levels identical to previous chain -> same result; prev[] below k stays valid
    lastres=a;
    if(a<4096) cnt[a]++; else printf("large value n=%d a=%u\n",n,a);
    if(n>=187 && a!=20 && a!=64) printf("Conj2 violation n=%d a=%u\n",n,a);
    if(n<=25) printf("%u,",a);
  }
  printf("\nvalue counts:"); for(int v=0;v<4096;v++) if(cnt[v]) printf(" %d:%d",v,cnt[v]); printf("\nmax arg %llu steps %ld\n",(unsigned long long)maxv,steps);
}
