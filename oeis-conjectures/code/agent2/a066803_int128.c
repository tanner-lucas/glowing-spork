/* third independent check with plain 128-bit arithmetic, no libraries */
#include <stdio.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 sq_iter(u64 x,int k,u64 m){for(int i=0;i<k;i++)x=mulmod(x,x,m);return x;}
int main(){
  u64 ps[2]={3ULL*(1ULL<<41)+1, 21ULL*(1ULL<<41)+1}; int ks[2]={38,39};
  for(int t=0;t<2;t++){u64 p=ps[t];int k=ks[t];
    /* trial-division primality (p < 2^46, sqrt < 2^23) */
    int prime=1; for(u64 d=2;d*d<=p;d++) if(p%d==0){prime=0;break;}
    printf("p=%llu prime=%d  2^(2^%d) mod p = %llu  3^(2^%d) mod p = %llu  p-1=%llu\n",p,prime,k,sq_iter(2,k,p),k,sq_iter(3,k,p),p-1);
  }
}
