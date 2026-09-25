// 3D Integer Lunar Lander, rest-to-rest: min N s.t. exists path a_0=0..a_N=0, |da|<=1,
// sum a_k = 0 and sum k*a_k = n.  DP over k with state (a, s1) -> bitset of moments.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int N;
int AM, SM, MM, W; // bounds
#define IDX(a,s) (((a)+AM)*(2*SM+1)+((s)+SM))
static inline void orshift(uint64_t*dst,const uint64_t*src,long sh){ // dst |= src << sh (sh may be negative), W words
  if(sh>=0){long ws=sh>>6,bs=sh&63; for(long i=W-1;i>=ws;i--){uint64_t v=src[i-ws]<<bs; if(bs&&i-ws-1>=0)v|=src[i-ws-1]>>(64-bs); dst[i]|=v;}}
  else{sh=-sh;long ws=sh>>6,bs=sh&63; for(long i=0;i+ws<W;i++){uint64_t v=src[i+ws]>>bs; if(bs&&i+ws+1<W)v|=src[i+ws+1]<<(64-bs); dst[i]|=v;}}
}
int main(int argc,char**argv){
  N=atoi(argv[1]);
  AM=N/2+1; SM=N*N/4+2; MM=N*N*N/8+N*N+10; W=(2*MM+1+63)/64;
  long ns=(long)(2*AM+1)*(2*SM+1);
  uint64_t*cur=calloc(ns*W,8),*nxt=calloc(ns*W,8);
  char*alive=calloc(ns,1),*alive2=calloc(ns,1);
  if(!cur||!nxt){fprintf(stderr,"oom\n");return 1;}
  // moment offset MM
  cur[IDX(0,0)*W + (MM>>6)] |= 1ULL<<(MM&63); alive[IDX(0,0)]=1;
  for(int k=1;k<=N;k++){
    memset(nxt,0,ns*W*8); memset(alive2,0,ns);
    int rem=N-k;
    for(int a=-AM;a<=AM;a++)for(int s=-SM;s<=SM;s++){ if(!alive[IDX(a,s)])continue;
      for(int d=-1;d<=1;d++){int a2=a+d; if(abs(a2)>rem||abs(a2)>AM)continue; int s2=s+a2; if(abs(s2)>SM)continue;
        // prune: remaining steps must bring s2 to 0: max change ~ rem^2/4 + |a2|*rem
        long lim=(long)rem*rem/4+ (long)abs(a2)*rem + rem; if(labs(s2)>lim)continue;
        orshift(nxt+IDX(a2,s2)*W, cur+IDX(a,s)*W, (long)k*a2); alive2[IDX(a2,s2)]=1; }}
    uint64_t*t=cur;cur=nxt;nxt=t; char*t2=alive;alive=alive2;alive2=t2;
  }
  uint64_t*b=cur+IDX(0,0)*W;
  for(long m=0;m<=MM;m++){ long p=m+MM; if(b[p>>6]>>(p&63)&1) printf("%ld ",m);} printf("\n");
  return 0;}
