#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(){ uint32_t N=200000000; uint16_t *t=malloc((N+2)*2); for(uint32_t i=0;i<=N+1;i++) t[i]=0;
  for(uint32_t i=1;i<=N+1;i++) for(uint32_t j=i;j<=N+1;j+=i) t[j]++;
  int first[200]={0}; long oddcnt[200]={0};
  for(uint32_t k=2;k<=N;k++) if(t[k-1]==t[k+1] && (t[k-1]%2==0)){ int n=t[k-1]/2; if(n<200){ if(!first[n]) first[n]=k; if(k&1) oddcnt[n]++; } }
  int pr[]={3,5,7,11,13,17,19,23}; for(int i=0;i<8;i++){int p=pr[i]; printf("p=%d least k<=2e8: %d, number of odd k<=2e8 with d(k-1)=d(k+1)=2p: %ld\n",p,first[p],oddcnt[p]);} }
