#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long ull; typedef unsigned __int128 u128;
int main(int argc,char**argv){
  ull N=strtoull(argv[1],0,10); long long S=0; ull firstpos[200]={0}, firstneg[200]={0};
  for(ull k=1;k<=N;k++){
    u128 t=(u128)2*k*k; ull r=(ull)sqrtl((long double)t);
    while((u128)r*r>t) r--; while((u128)(r+1)*(r+1)<=t) r++;
    S += (r&1)? -1 : 1;
    if(S>0 && S<200 && !firstpos[S]) firstpos[S]=k;
    if(S<0 && -S<200 && !firstneg[-S]) firstneg[-S]=k;
  }
  printf("first occurrences of +n: "); for(int i=1;i<200&&firstpos[i];i++) printf("%llu ",firstpos[i]); printf("\n");
  printf("first occurrences of -n: "); for(int i=1;i<200&&firstneg[i];i++) printf("%llu ",firstneg[i]); printf("\n");
}
