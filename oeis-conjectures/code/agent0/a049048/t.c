// For primes r<=R: F_r = {n in [2,r-1]: n! == 1 mod r}. Find composite c=q*r (q<r primes) or q^2 with two n (2<=n<q) in F_q ∩ F_r (resp. n!==1 mod q^2).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
int main(int argc,char**argv){
  long R=atol(argv[1]);
  char *comp=calloc(R+1,1); for(long i=2;i*i<=R;i++) if(!comp[i]) for(long j=i*i;j<=R;j+=i) comp[j]=1;
  // store pairs (n, r) for n in F_r, n <= r-1; we need for each n, list of primes r
  long cap=1<<20, cnt=0; long *pn=malloc(cap*sizeof(long)), *pr=malloc(cap*sizeof(long));
  long sq=0;
  for(long r=3;r<=R;r++){ if(comp[r]) continue;
    u64 f=1; u64 m2=(u64)r*r; u64 f2=1;
    for(long n=2;n<=r-1;n++){ f=f*n%r; f2=(u64)((u128)f2*n%m2);
      if(f==1){ if(cnt==cap){cap*=2; pn=realloc(pn,cap*sizeof(long)); pr=realloc(pr,cap*sizeof(long));} pn[cnt]=n; pr[cnt]=r; cnt++; }
      if(f2==1 && n>=2) { sq++; printf("n!==1 mod r^2: n=%ld r=%ld\n",n,r); }
    }
  }
  fprintf(stderr,"pairs %ld\n",cnt);
  // for each prime q, list its F_q elements (< q); for each pair n1<n2 in F_q, find primes r>q with both in F_r.
  // Build index by n: for each n, sorted list of r (pairs already sorted by r).
  long maxn=R; long *start=calloc(maxn+2,sizeof(long)), *len=calloc(maxn+2,sizeof(long));
  for(long i=0;i<cnt;i++) len[pn[i]]++;
  long s=0; for(long n=0;n<=maxn;n++){ start[n]=s; s+=len[n]; }
  long *byn=malloc(cnt*sizeof(long)); long *fill=calloc(maxn+2,sizeof(long));
  for(long i=0;i<cnt;i++){ long n=pn[i]; byn[start[n]+fill[n]++]=pr[i]; }
  // F_q lists: pairs grouped by r in order
  long i=0, found=0;
  while(i<cnt){ long q=pr[i]; long j=i; while(j<cnt && pr[j]==q) j++;
    for(long a=i;a<j;a++) for(long b=a+1;b<j;b++){ long n1=pn[a], n2=pn[b]; // n1<n2<q
        // intersect lists for n1 and n2, r>q
        long *A=byn+start[n1], la=len[n1], *B=byn+start[n2], lb=len[n2]; long x=0,y=0;
        while(x<la && y<lb){ if(A[x]<B[y]) x++; else if(A[x]>B[y]) y++; else { if(A[x]>q){ printf("COUNTEREXAMPLE c=%ld*%ld n1=%ld n2=%ld\n",q,A[x],n1,n2); found++;} x++;y++; } }
      }
    i=j; }
  printf("R=%ld done, found=%ld, squares-hits=%ld\n",R,found,sq);
}
