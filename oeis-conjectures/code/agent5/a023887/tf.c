// Search prime factors q = 2k*7^7+1 of Phi_{7^7}(7) = sigma_{7^6}(7^6): need 7^(7^7) == 1 mod q and 7^(7^6) != 1 mod q
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
int main(int argc,char**argv){
  u64 K0=strtoull(argv[1],0,10), K1=strtoull(argv[2],0,10);
  const u64 P7=823543ULL, P6=117649ULL;
  int sp[]={3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}; int ns=sizeof(sp)/sizeof(int);
  u64 found=0;
  for(u64 k=K0;k<=K1;k++){
    u64 q=2*k*P7+1; int skip=0;
    for(int i=0;i<ns;i++) if(q%sp[i]==0){skip=1;break;}
    if(skip) continue;
    if(powm(7,P7,q)==1 && powm(7,P6,q)!=1){ printf("FACTOR q=%llu (k=%llu)\n",(unsigned long long)q,(unsigned long long)k); fflush(stdout); found++; }
  }
  printf("done k=%llu..%llu found=%llu\n",(unsigned long long)K0,(unsigned long long)K1,(unsigned long long)found);
  return 0;
}
