#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); // phi up to N, m up to N/2
  uint32_t *phi=malloc((N+1)*sizeof(uint32_t));
  for(long i=0;i<=N;i++) phi[i]=i;
  for(long p=2;p<=N;p++) if(phi[p]==(uint32_t)p) for(long j=p;j<=N;j+=p) phi[j]-=phi[j]/p;
  for(long m=1;2*m<=N;m++){ if(phi[2*m-1]%2==0 && (long)phi[2*m-1]/2 == (long)phi[2*m]-1) printf("%ld ",m); }
  printf("\n");
}
