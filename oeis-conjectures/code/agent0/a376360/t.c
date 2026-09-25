// last digit of greedy representation in base of squares (A007961) and triangular numbers (A000462)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static ll isq(ll n){ ll s=(ll)sqrtl((long double)n); while(s*s>n) s--; while((s+1)*(s+1)<=n) s++; return s; }
static int lastsq(ll n){ // greedy: repeatedly take largest square s^2<=n, digit floor(n/s^2), n %= s^2; last digit = coefficient of 1
  while(n>0){ ll s=isq(n); if(s==1) return (int)n; n%= s*s; } return 0; }
static ll itri(ll n){ ll k=(ll)((sqrtl(8.0L*n+1)-1)/2); while(k*(k+1)/2>n) k--; while((k+1)*(k+2)/2<=n) k++; return k; }
static int lasttri(ll n){ while(n>0){ ll k=itri(n); if(k==1) return (int)n; n%= k*(k+1)/2; } return 0; }
int main(int argc,char**argv){
  ll N=atoll(argv[1]);
  for(int base=0;base<2;base++){
    int nd = base==0?4:3;
    for(int c=0;c<nd;c++){
      ll prev=-1, idx=0; int seen[200]={0}; ll firstpos[200]={0}; ll firstidx[200]={0};
      for(ll n=1;n<=N;n++){ int d = base==0? lastsq(n): lasttri(n); if(d!=c) continue; idx++;
        if(prev>0){ ll g=n-prev; if(g<200 && !seen[g]){ seen[g]=1; firstpos[g]=prev; firstidx[g]=idx-1; } }
        prev=n; }
      printf("%s digit %d: gaps seen:", base==0?"squares":"triang", c);
      for(int g=1;g<200;g++) if(seen[g]) printf(" %d(@a(%lld)=%lld)",g,firstidx[g],firstpos[g]);
      printf("\n");
    }
  }
}
