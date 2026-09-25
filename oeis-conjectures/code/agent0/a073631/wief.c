// Search primes 5<=p<=LIM for (3/2)^(p-1) == 1 mod p^2, using Montgomery arithmetic mod m=p^2 (<2^64).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
static inline u64 mont_inv(u64 m){ u64 x=m; for(int i=0;i<6;i++) x*=2-m*x; return x; } // m^{-1} mod 2^64
static inline u64 redc(u128 T,u64 m,u64 minv){ u64 Tl=(u64)T, Th=(u64)(T>>64); u64 q=Tl*(-minv); u128 qm=(u128)q*m; u64 Qh=(u64)(qm>>64); u128 r=(u128)Th+Qh+(Tl!=0); if(r>=m) r-=m; return (u64)r; }
int main(int argc,char**argv){
  u64 LIM=strtoull(argv[1],0,10);
  u64 S=1; while(S*S<=LIM) S++;
  // small primes for segmented sieve
  char *small=calloc(S+1,1); u64 *sp=malloc(sizeof(u64)*S); int ns=0;
  for(u64 i=2;i<=S;i++) if(!small[i]){ sp[ns++]=i; for(u64 j=i*i;j<=S;j+=i) small[j]=1; }
  const u64 SEG=1<<22; char *seg=malloc(SEG);
  u64 cnt=0;
  for(u64 lo=0; lo<=LIM; lo+=SEG){
    u64 hi=lo+SEG-1; if(hi>LIM) hi=LIM;
    memset(seg,0,SEG);
    for(int k=0;k<ns;k++){ u64 p=sp[k]; if(p*p>hi) break; u64 st=((lo+p-1)/p)*p; if(st<p*p) st=p*p; for(u64 j=st;j<=hi;j+=p) seg[j-lo]=1; }
    for(u64 n=(lo<5?5:lo); n<=hi; n++){ if(seg[n-lo]) continue; if(n<=S && small[n]) continue;
      u64 p=n; u64 m=p*p; cnt++;
      // compute x = 3 * inv2 mod m; inv2=(m+1)/2
      u128 x128 = ((u128)3*((m+1)/2))%m; u64 x=(u64)x128;
      // Montgomery: R=2^64 mod m
      u64 minv=mont_inv(m);
      u64 R = (u64)(((u128)1<<64)%m); u64 R2=(u64)(((u128)R*R)%m);
      // to mont
      u64 xm = (u64)(((u128)x*R)%m);
      u64 res = R; // 1 in mont
      u64 e=p-1;
      while(e){ if(e&1){ u128 T=(u128)res*xm; u64 r=redc(T,m,minv); if(r>=m) r-=m; res=r;} u128 T=(u128)xm*xm; u64 r=redc(T,m,minv); if(r>=m) r-=m; xm=r; e>>=1; }
      // from mont
      u64 out=redc((u128)res,m,minv); if(out>=m) out-=m;
      if(out==1){ printf("FOUND p=%llu\n",(unsigned long long)p); fflush(stdout);} 
    }
  }
  fprintf(stderr,"primes tested %llu up to %llu\n",(unsigned long long)cnt,(unsigned long long)LIM);
}
