#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); long M=2*N+8;
  uint32_t *s=calloc(M+1,4);
  for(long d=1;d<=M;d++) for(long m=d;m<=M;m+=d) s[m]+=d;
  printf("A067730 (sigma(n-1)+sigma(n+1)=sigma(2n)): ");
  long ev=0;
  for(long n=2;n<=N;n++){ if((uint64_t)s[n-1]+s[n+1]==s[2*n]){ if(n<5000000) printf("%ld,",n); if(n%2==0){printf(" EVEN:%ld ",n); ev++;} } }
  printf("\nA067129 (sigma(k-3)+sigma(k+3)=sigma(2k)): ");
  for(long k=4;k<=N;k++){ if((uint64_t)s[k-3]+s[k+3]==s[2*k]){ if(k<20000) printf("%ld,",k); if(k%2==0){printf(" EVEN:%ld ",k); ev++;} } }
  printf("\nN=%ld even solutions=%ld\n",N,ev);
}
