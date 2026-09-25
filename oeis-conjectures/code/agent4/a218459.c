#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static ll isq(ll v){ ll r=(ll)sqrt((double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r;}
static int lpf(ll d){ for(ll q=2;q*q<=d;q++) if(d%q==0) return q; return d;}
int main(int argc,char**argv){
  ll P=atoll(argv[1]); char*c=calloc(P+1,1); for(ll i=2;i*i<=P;i++) if(!c[i]) for(ll j=i*i;j<=P;j+=i) c[j]=1;
  static int seenbad[100000]; long cnt=0; ll maxd=0;
  for(ll p=23;p<=P;p+=24){ if(c[p]) continue; cnt++;
    ll d;
    for(d=1;;d++){ int ok=0; for(ll y=1; d*y*y<p; y++){ ll r=p-d*y*y; ll s=isq(r); if(s*s==r){ok=1;break;} } if(ok) break; }
    if(d>maxd) maxd=d;
    if((d&1) && lpf(d)!=d && d>1){ // odd composite
      int inA = (d%4==3) && (lpf(d)%4==1);
      if(!inA && d<100000 && !seenbad[d]){ seenbad[d]=1; printf("odd composite d=%lld NOT in A176255, first p=%lld (d mod 4=%lld, lpf=%d)\n",d,p,d%4,lpf(d)); }
    }
  }
  fprintf(stderr,"P=%lld primes 23 mod 24: %ld, max d=%lld\n",P,cnt,maxd);
}
