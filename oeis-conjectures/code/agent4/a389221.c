#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long ll;
static uint32_t *spf;
static int divisors(ll n, ll *d){ // n <= sieve limit
  int c=1; d[0]=1;
  while(n>1){ ll p=spf[n]; int e=0; while(n%p==0){n/=p;e++;}
    int c0=c; ll pk=1; for(int i=1;i<=e;i++){ pk*=p; for(int j=0;j<c0;j++) d[c++]=d[j]*pk; } }
  return c;
}
static ll gcdl(ll a,ll b){ while(b){ll t=a%b;a=b;b=t;} return a;}
// count distinct repeated values for k
#define HS 4096
static ll hk[HS]; static int hstamp[HS]; static int stamp=0;
static int insert(ll key){ unsigned h=(unsigned)((key*0x9E3779B97F4A7C15ULL)>>52)&(HS-1); while(hstamp[h]==stamp){ if(hk[h]==key) return 0; h=(h+1)&(HS-1);} hstamp[h]=stamp; hk[h]=key; return 1; }
static int count(ll k){
  static ll D[20000], B[20000];
  stamp++;
  int nd=divisors(2*k,D); int cnt=(k>=2)?1:0; // value 0 repeated (m=1,2)
  for(int i=0;i<nd;i++) for(int j=0;j<nd;j++){ ll g1=D[i], g2=D[j]; if(g1>=g2) continue; if(g2>k) continue;
      ll c1=2*k/g1, c2=2*k/g2, diff=c1-c2; ll bmax=k/g2; if(bmax<2) continue;
      int nb=divisors(diff,B);
      for(int t=0;t<nb;t++){ ll b=B[t]; if(b<2||b>bmax) continue; if(gcdl(b,c1)!=1) continue;
        ll key=b*4000000000LL + (c1%b); if(insert(key)) cnt++; } }
  return cnt;
}
int main(int argc,char**argv){
  ll N=atoll(argv[1]); int check=argc>2;
  ll L=2*N+10; spf=calloc(L+1,4); for(ll i=2;i<=L;i++) if(!spf[i]) for(ll j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i;
  for(ll k=1;k<=N;k++){
    int c=count(k);
    if(check){ printf("%lld %d\n",k,c); continue; }
    // A389221: c==4 ; conj: for k>80, c==4 iff k=4p, p prime>13
    int is4p = (k%4==0) && spf[k/4]==k/4 && k/4>13;
    int is3p = (k%3==0) && spf[k/3]==k/3 && k/3>7;
    if(k>80 && ((c==4)!=is4p)) printf("A389221 mismatch k=%lld c=%d is4p=%d\n",k,c,is4p);
    if(k>52 && ((c==3)!=is3p)) printf("A390100 mismatch k=%lld c=%d is3p=%d\n",k,c,is3p);
  }
  fprintf(stderr,"done N=%lld\n",N);
}
