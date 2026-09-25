#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  uint64_t N=atoll(argv[1]); uint64_t M=4*N+10;
  uint32_t *phi=malloc(M*4);
  for(uint64_t i=0;i<M;i++) phi[i]=i;
  for(uint64_t i=2;i<M;i++) if(phi[i]==i) for(uint64_t j=i;j<M;j+=i) phi[j]-=phi[j]/i;
  uint64_t a=1; double mn=1e9,mx=0; uint64_t amn=0,amx=0;
  for(uint64_t n=1;n<=N;n++){
    if(a>=M){printf("overflow at n=%llu\n",(unsigned long long)n);return 1;}
    a=n+phi[a];
    if(n<=25) printf("%llu ",(unsigned long long)a);
    double r=(double)a/n;
    if(r<mn){mn=r;amn=n;} if(r>mx){mx=r;amx=n;}
    if(4*a<=5*n || a>=4*n) printf("\nVIOLATION n=%llu a=%llu\n",(unsigned long long)n,(unsigned long long)a);
    if(n>=1000 && (n&(n-1))==0) { printf("\n n=%llu min ratio so far %.6f at %llu, max %.6f at %llu",(unsigned long long)n,mn,(unsigned long long)amn,mx,(unsigned long long)amx);}
  }
  printf("\nfinal min %.6f at %llu max %.6f at %llu\n",mn,(unsigned long long)amn,mx,(unsigned long long)amx);
}
