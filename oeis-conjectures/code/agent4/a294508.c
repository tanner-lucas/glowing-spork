#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static uint64_t *bits; static uint32_t *cum; 
static inline uint32_t PI(uint64_t x){ uint64_t w=x>>6; uint64_t mask = (x&63)==63 ? ~0ULL : ((1ULL<<((x&63)+1))-1); return cum[w]+__builtin_popcountll(bits[w]&mask); }
int main(int argc,char**argv){
  int N=atoi(argv[1]); int F=atoi(argv[2]); uint64_t L=(uint64_t)N*N*F+(uint64_t)N*N+100;
  uint64_t W=L/64+2; bits=calloc(W,8); cum=malloc(W*4);
  char *comp=calloc(L+1,1); for(uint64_t i=2;i*i<=L;i++) if(!comp[i]) for(uint64_t j=i*i;j<=L;j+=i) comp[j]=1;
  for(uint64_t i=2;i<=L;i++) if(!comp[i]) bits[i>>6]|=1ULL<<(i&63); free(comp);
  uint32_t c=0; for(uint64_t w=0;w<W;w++){ cum[w]=c; c+=__builtin_popcountll(bits[w]); }
  long viol=0;
  for(long n=1;n<=N;n++){
    long mn=1L<<40; for(long m=1;m<=n;m++){ long t=(long)PI(n*m)-(long)PI(n)*PI(m); if(t<mn) mn=t; }
    long worst=1L<<40, argM=0;
    for(long M=n+1;M<=(long)F*n;M++){ long t=(long)PI(n*M)-(long)PI(n)*PI(M); if(t<worst){worst=t;argM=M;} if(t<mn){ viol++; if(viol<30) printf("VIOL n=%ld M=%ld T=%ld min=%ld\n",n,M,t,mn);} }
    if(n%500==0) fprintf(stderr,"n=%ld min=%ld worstM=%ld at M=%ld\n",n,mn,worst,argM);
  }
  printf("N=%d F=%d violations=%ld\n",N,F,viol);
}
