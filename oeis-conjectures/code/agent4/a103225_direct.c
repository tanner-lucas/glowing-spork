// Direct count for a single n: all z=x+iy with x^2+y^2<n^2 and Gaussian gcd(n,z) a unit.
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll rdiv(ll u, ll v){ // round(u/v), v>0
  ll q = u>=0 ? (2*u+v)/(2*v) : -((-2*u+v)/(2*v)); return q; }
static ll gnorm_gcd(ll ar, ll ai, ll br, ll bi){
  while(br!=0||bi!=0){
    ll nb=br*br+bi*bi;
    ll xr=ar*br+ai*bi, xi=ai*br-ar*bi; // a*conj(b)
    ll qr=rdiv(xr,nb), qi=rdiv(xi,nb);
    ll rr=ar-(qr*br-qi*bi), ri=ai-(qr*bi+qi*br);
    ar=br; ai=bi; br=rr; bi=ri;
  }
  return ar*ar+ai*ai;
}
int main(int argc,char**argv){
  ll n=atoll(argv[1]); ll c=0;
  for(ll x=-n+1;x<n;x++) for(ll y=-n+1;y<n;y++) if(x*x+y*y<n*n && gnorm_gcd(n,0,x,y)==1) c++;
  printf("%lld %lld\n",n,c);
  return 0;
}
