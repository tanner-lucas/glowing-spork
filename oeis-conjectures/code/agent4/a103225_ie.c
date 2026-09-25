// a(n) = sum over squarefree Gaussian divisors d of n (up to units) of mu(d)*C(n^2/N(d)),
// C(t) = #{(x,y) in Z^2 : x^2+y^2 < t}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static ll isqrtll(ll v){ if(v<0) return -1; ll r=(ll)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r;}
static ll Cstrict(ll n2, ll D){ // #{x^2+y^2 < n2/D} = #{D*(x^2+y^2) < n2}
  ll M=(n2+D-1)/D-1; // s < n2/D  <=> s <= ceil(n2/D)-1
  if(M<0) return 0;
  ll r=isqrtll(M), s=0;
  for(ll x=-r;x<=r;x++) s+=2*isqrtll(M-x*x)+1;
  return s;
}
int main(int argc,char**argv){
  ll NMAX=atoll(argv[1]); ll from=argc>2?atoll(argv[2]):1;
  const long double PI=3.141592653589793238462643383279502884L;
  for(ll n=from;n<=NMAX;n++){
    // factor n
    ll m=n; ll ps[20]; int k=0;
    for(ll p=2;p*p<=m;p++) if(m%p==0){ps[k++]=p; while(m%p==0) m/=p;}
    if(m>1) ps[k++]=m;
    // build list of (D, sign) terms
    ll Ds[1<<12]; int sg[1<<12]; int t=1; Ds[0]=1; sg[0]=1;
    for(int i=0;i<k;i++){
      ll p=ps[i]; int t0=t;
      if(p==2){ for(int j=0;j<t0;j++){Ds[t]=Ds[j]*2; sg[t]=-sg[j]; t++;} }
      else if(p%4==3){ for(int j=0;j<t0;j++){Ds[t]=Ds[j]*p*p; sg[t]=-sg[j]; t++;} }
      else { for(int j=0;j<t0;j++){ Ds[t]=Ds[j]*p; sg[t]=-sg[j]; t++; Ds[t]=Ds[j]*p; sg[t]=-sg[j]; t++; Ds[t]=Ds[j]*p*p; sg[t]=sg[j]; t++; } }
    }
    ll a=0, n2=n*n;
    for(int j=0;j<t;j++) a+=sg[j]*Cstrict(n2,Ds[j]);
    long double d=(long double)a-PI*(long double)n2;
    if(argc>3) printf("%lld %lld\n",n,a);
    else if(d>0) printf("COUNTEREX n=%lld a=%lld a-pi*n^2=%.6Lf\n",n,a,d);
  }
  return 0;
}
