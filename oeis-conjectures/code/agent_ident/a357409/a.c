#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
// count odd x in [lo, hi] (inclusive)
static ll countodd(ll lo, ll hi){ if(hi<lo) return 0; // odd numbers: x=2j+1
  // j in [ceil((lo-1)/2), floor((hi-1)/2)]
  ll a=lo-1, b=hi-1; ll jlo = (a>=0)? (a+1)/2 : -((-a)/2); ll jhi = (b>=0)? b/2 : -((-b+1)/2);
  return jhi>=jlo ? jhi-jlo+1 : 0; }
// window: odd numbers s, s+2, ..., e=s+2(n-1)
static ll pairs(ll s, ll n){ ll e=s+2*(n-1); ll c=0;
  for(ll T=2; T<=2*e; T*=2){ // x<y, x+y=T, x>=s, y<=e -> x>=T-e ; x < T/2 -> x <= T/2 - 1 (x odd, T/2 integer)
    ll lo = s> T-e ? s : T-e; ll hi = T/2 - 1; // x < T/2 strictly
    // x = T/2 would mean y=x, excluded; if T/2 odd, x<=T/2-2 as odd automatically handled by countodd
    c += countodd(lo, hi);
  }
  return c; }
static ll positives(ll s, ll n){ ll e=s+2*(n-1); if(e<=0) return 0; ll lo = s>1? s:1; return countodd(lo,e); }
int main(int argc,char**argv){
  ll N=atoll(argv[1]); int check=argc>2;
  for(ll n=1;n<=N;n++){
    ll best=-1, bp=-1, bestpos_s=0;
    for(ll k=0;k<=n+1;k++){ ll s=1-2*k; ll c=pairs(s,n); ll p=positives(s,n);
      if(c>best){best=c;bp=p;} else if(c==best && p>bp) bp=p; }
    if(check){ // also windows starting at larger odd numbers
      for(ll s=3; s<=4*n+64; s+=2){ ll c=pairs(s,n); if(c>best) printf("n=%lld: window at s=%lld beats: %lld > %lld\n",n,s,c,best); }
    }
    // conjecture: A274089(n) + 2^t - 1
    ll m=n+1; int k2=0; while((1LL<<(k2+1))<=m) k2++; ll q=m+k2; ll a274=(q + ((q>>(k2+1))&1))>>1;
    int t=0; for(int k=1;k<30;k++){ ll thr=(1LL<<(2*(k+1)+1)) - (1LL<<(k+1)) - 1; if(n>=thr) t++; }
    ll conj=a274 + (1LL<<t) - 1;
    printf("%lld %lld %lld %lld\n",n,bp,conj,best);
  }
}
