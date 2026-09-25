#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
// pi(x) table for x <= L via bitset of primes + block counts
static uint64_t *bits; static uint32_t *blk; static long long L;
static inline long long pix(long long x){ long long b=x>>6; uint64_t w=bits[b] & (x%64==63? ~0ULL : ((1ULL<<((x&63)+1))-1)); return blk[b]+__builtin_popcountll(w); }
int main(int argc,char**argv){
  int NMAX=atoi(argv[1]); long long MMAX=atoll(argv[2]); L=(long long)NMAX*MMAX+64;
  char *s=calloc(L+1,1); // composite flags
  s[0]=s[1]=1; for(long long i=2;i*i<=L;i++) if(!s[i]) for(long long j=i*i;j<=L;j+=i) s[j]=1;
  long long nb=L/64+2; bits=calloc(nb,8); blk=calloc(nb,4);
  for(long long i=0;i<=L;i++) if(!s[i]) bits[i>>6]|=1ULL<<(i&63);
  free(s);
  uint32_t c=0; for(long long b=0;b<nb;b++){ blk[b]=c; c+=__builtin_popcountll(bits[b]); }
  for(int n=1;n<=NMAX;n++){
    long long pn=pix(n), amin=1LL<<60;
    for(long long m=1;m<=n;m++){ long long f=pix(n*m)-pn*pix(m); if(f<amin) amin=f; }
    for(long long m=n+1;m<=MMAX;m++){ long long f=pix(n*m)-pn*pix(m); if(f<amin){ printf("n=%d: m=%lld gives f=%lld < a(n)=%lld\n",n,m,f,amin); break; } }
  }
  printf("done NMAX=%d MMAX=%lld\n",NMAX,MMAX);
  return 0;
}
