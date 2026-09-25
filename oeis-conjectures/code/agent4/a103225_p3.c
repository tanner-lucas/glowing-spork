// for primes p = 3 mod 4: a(p) = N(p)-1 where N(p)=#{x^2+y^2<p^2}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static ll isq(ll v){ ll r=(ll)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r;}
int main(int argc,char**argv){
  ll P=atoll(argv[1]); char*c=calloc(P+1,1); for(ll i=2;i*i<=P;i++) if(!c[i]) for(ll j=i*i;j<=P;j+=i) c[j]=1;
  const long double PI=3.141592653589793238462643383279502884L; int cnt=0, tot=0;
  for(ll p=3;p<=P;p+=4){ if(c[p]) continue; tot++;
    ll R=p*p-1, s=0; for(ll x=1;x<p;x++) s+=isq(R-x*x); ll N=4*s+4*(p-1)+1; // quadrants + axes + origin
    ll a=N-1; long double d=(long double)a-PI*(long double)p*(long double)p;
    if(d>0){ cnt++; printf("%lld %lld %.4Lf\n",p,a,d);} }
  fprintf(stderr,"primes 3 mod 4 up to %lld: %d, counterexamples %d\n",P,tot,cnt);
}
