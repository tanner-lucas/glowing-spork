// Exact DP for 3D Integer Lunar Lander from start (a0,v0,h0): N moves suffice iff there is a slow walk
// a_0=a0,...,a_N=0 (|a_k-a_{k-1}|<=1) with sum_{k=1..N} a_k = -v0 and sum_{k=1..N} k*a_k = h0 - v0.
// Prints 1 if feasible with exactly N moves (idling at origin allowed => monotone in N).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int AM,SM; long MM; long W;
#define IDX(a,s) (((long)(a)+AM)*(2L*SM+1)+((s)+SM))
static inline void orshift(uint64_t*dst,const uint64_t*src,long sh){
  if(sh>=0){long ws=sh>>6,bs=sh&63; for(long i=W-1;i>=ws;i--){uint64_t v=src[i-ws]<<bs; if(bs&&i-ws-1>=0)v|=src[i-ws-1]>>(64-bs); dst[i]|=v;}}
  else{sh=-sh;long ws=sh>>6,bs=sh&63; for(long i=0;i+ws<W;i++){uint64_t v=src[i+ws]>>bs; if(bs&&i+ws+1<W)v|=src[i+ws+1]<<(64-bs); dst[i]|=v;}}
}
int feasible(int N,int a0,long v0,long h0){
  AM=abs(a0)+N/2+2; SM=(int)((long)AM*N+5); MM=(long)AM*N*(N+1)/2+10; W=(2*MM+1+63)/64;
  long target1=-v0, target2=h0-v0; if(labs(target2)>MM||labs(target1)>SM) return 0;
  long ns=(2L*AM+1)*(2L*SM+1);
  uint64_t*cur=calloc(ns*W,8),*nxt=calloc(ns*W,8); char*al=calloc(ns,1),*al2=calloc(ns,1);
  if(!cur||!nxt){fprintf(stderr,"oom N=%d\n",N);exit(1);}
  cur[IDX(a0,0)*W+(MM>>6)]|=1ULL<<(MM&63); al[IDX(a0,0)]=1;
  for(int k=1;k<=N;k++){ memset(nxt,0,ns*W*8); memset(al2,0,ns); int rem=N-k;
    for(int a=-AM;a<=AM;a++)for(int s=-SM;s<=SM;s++){ if(!al[IDX(a,s)])continue;
      for(int d=-1;d<=1;d++){int a2=a+d; if(abs(a2)>rem||abs(a2)>AM)continue; long s2=s+a2; if(labs(s2)>SM)continue;
        long lim=(long)rem*rem/4+(long)abs(a2)*rem+rem; if(labs(s2-target1)>lim)continue;
        orshift(nxt+IDX(a2,s2)*W,cur+IDX(a,s)*W,(long)k*a2); al2[IDX(a2,s2)]=1;}}
    uint64_t*t=cur;cur=nxt;nxt=t;char*t2=al;al=al2;al2=t2;}
  int r=0; if(labs(target1)<=SM && al[IDX(0,target1)]){long p=target2+MM; r=(cur[IDX(0,target1)*W+(p>>6)]>>(p&63))&1;}
  free(cur);free(nxt);free(al);free(al2); return r;}
int main(int c,char**v){ int mode=atoi(v[1]); int nmax=atoi(v[2]);
  for(int n=0;n<=nmax;n++){ int a0=0; long v0=0,h0=0; if(mode==0)h0=n; else if(mode==1)a0=n; else v0=n;
    int N=0; while(!feasible(N,a0,v0,h0))N++; printf("%d ",N); fflush(stdout);} printf("\n"); return 0;}
