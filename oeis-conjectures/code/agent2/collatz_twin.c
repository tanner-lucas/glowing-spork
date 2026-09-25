/* Find twin prime pairs (p,p+2), p+2 <= N, such that one element lies in the Collatz trajectory of the other.
   Then for each such linked pair report the downstream trajectory's twin-pair count (A319227 value of the upstream element). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint8_t *comp; static uint64_t N;
static int isprime_small(uint64_t x){ if(x<2) return 0; if(x<=N) return !comp[x]; for(uint64_t d=2;d*d<=x;d++) if(x%d==0) return 0; return 1; }
/* twin pairs in trajectory of n: count pairs (q,q+2) both in trajectory */
static int count_pairs(uint64_t n){ static uint64_t tr[20000]; int L=0; uint64_t x=n; tr[L++]=x; while(x!=1){ x = (x&1)? 3*x+1 : x>>1; tr[L++]=x; }
  int c=0; for(int i=0;i<L;i++){ uint64_t q=tr[i]; if(!(q&1)) continue; if(!isprime_small(q)||!isprime_small(q+2)) continue; for(int j=0;j<L;j++) if(tr[j]==q+2){c++;break;} } return c; }
static int in_traj(uint64_t from, uint64_t target){ uint64_t x=from; while(x!=1){ if(x==target) return 1; if(x > 0x5555555555555555ULL){fprintf(stderr,"overflow risk %lu\n",from); exit(1);} x=(x&1)?3*x+1:x>>1; } return target==1; }
int main(int argc,char**argv){ N=strtoull(argv[1],0,10); comp=calloc(N+3,1); comp[0]=comp[1]=1;
  for(uint64_t i=2;i*i<=N+2;i++) if(!comp[i]) for(uint64_t j=i*i;j<=N+2;j+=i) comp[j]=1;
  long pairs=0, linked=0;
  for(uint64_t p=3;p+2<=N;p+=2){ if(comp[p]||comp[p+2]) continue; pairs++;
    int a=in_traj(p,p+2), b=in_traj(p+2,p);
    if(a||b){ linked++; uint64_t up = a? p : p+2; printf("linked pair (%lu,%lu): %s ; A319227(%lu)=%d\n",p,p+2,a?"p+2 in traj(p)":"p in traj(p+2)",up,count_pairs(up)); }
  }
  printf("N=%lu twin pairs=%ld linked=%ld\n",N,pairs,linked);
}
