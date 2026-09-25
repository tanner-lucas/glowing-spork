#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 f(u64 k, u64 m){ u128 k2=(u128)k*k%m; u128 k3=k2*k%m; u128 v=(u128)33*k2%m*((k3+1)%m)%m; return (u64)v; }
int isprime(u64 x){ if(x<2) return 0; for(u64 d=2;d*d<=x;d++) if(x%d==0) return 0; return 1; }
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10);
  u64 cap=1<<20; unsigned int *stamp=calloc(cap,sizeof(unsigned)); unsigned cur=0;
  u64 m=1; int data[]={1,4,7,7,13,13,13,13,13,31,41,41,61,61,61,61,61,61,61,73,101,137,137};
  for(u64 n=1;n<=N;n++){
    for(;;){
      if(m>=cap){ while(cap<=m) cap*=2; free(stamp); stamp=calloc(cap,sizeof(unsigned)); cur=0; }
      cur++; if(cur==0){ memset(stamp,0,cap*sizeof(unsigned)); cur=1; }
      int ok=1; for(u64 k=1;k<=n;k++){ u64 v=f(k,m); if(stamp[v]==cur){ok=0;break;} stamp[v]=cur; }
      if(ok) break; m++;
    }
    if(n<=23 && m!=(u64)data[n-1]) printf("MISMATCH n=%llu m=%llu\n",n,m);
    if(n>2 && !isprime(m)) { printf("COMPOSITE a(%llu)=%llu\n",n,m); fflush(stdout);} 
    if(n%10000==0){ printf("n=%llu a=%llu\n",n,m); fflush(stdout);} 
  }
}
