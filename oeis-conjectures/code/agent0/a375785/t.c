#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long ll;
uint32_t *spf;
int divs(ll m, ll *d){ int cnt=1; d[0]=1; while(m>1){ ll p=spf[m]; int e=0; while(m%p==0){m/=p;e++;} int c0=cnt; ll pk=1; for(int k=1;k<=e;k++){ pk*=p; for(int i=0;i<c0;i++) d[cnt++]=d[i]*pk; } } return cnt; }
int main(int argc,char**argv){
  ll NMAX=atoll(argv[1]); ll LIM=4*NMAX*NMAX+10;
  spf=calloc(LIM+1,sizeof(uint32_t));
  for(ll i=2;i<=LIM;i++) if(!spf[i]){ spf[i]=i; if(i*i<=LIM) for(ll j=i*i;j<=LIM;j+=i) if(!spf[j]) spf[j]=i; }
  ll *d=malloc(100000*sizeof(ll)); int data[]={1,1,3,3,5,5,5,7,9,9,9,13,9,9,19,15,13,19,13,23,19,19,17,29,25,19,27};
  int even=0;
  for(ll n=1;n<=NMAX;n++){
    ll N=3*n*n, cnt=0;
    for(ll x=1;3*x*x<=N;x++){ ll M=N+x*x; int k=divs(M,d);
      for(int i=0;i<k;i++){ ll dd=d[i]; if(dd>=2*x && dd*dd<=M){ ll e=M/dd; ll y=dd-x, z=e-x; if(y>=x && z>=y) cnt++; } } }
    if(n<=27 && cnt!=data[n-1]) printf("MISMATCH n=%lld cnt=%lld\n",n,cnt);
    if(cnt%2==0){ even++; if(even<20) printf("EVEN a(%lld)=%lld\n",n,cnt);} 
  }
  printf("checked n<=%lld, even terms=%d\n",NMAX,even);
}
