#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
// a(n) = n - #{i<=n : n*i = a*b with 1<=a<=b<=n-1}
long long A(u64 n, unsigned char *mark){
  memset(mark,0,n+1);
  for(u64 a=1;a<n;a++){
    u64 g=gcd(a,n); u64 step=n/g; // b multiple of step
    u64 b0=((a+step-1)/step)*step;
    for(u64 b=b0;b<n;b+=step){ u64 i=(a/g)*(b/step); /* a*b/n = (a/g)*(b/(n/g)) */ mark[i]=1; }
  }
  long long c=0; for(u64 i=1;i<=n;i++) if(!mark[i]) c++;
  return c;
}
int main(int argc,char**argv){
  u64 maxn=0; for(int k=1;k<argc;k++){u64 v=strtoull(argv[k],0,10); if(v>maxn)maxn=v;}
  unsigned char *mark=malloc(maxn+2);
  if(argc>1 && strcmp(argv[1],"range")==0){
    u64 lo=strtoull(argv[2],0,10), hi=strtoull(argv[3],0,10);
    free(mark); mark=malloc(hi+2);
    double best=1e9;
    for(u64 n=lo;n<=hi;n++){ long long v=A(n,mark); double r=v/(n/log((double)n)); if(r<best){best=r; printf("n=%llu a=%lld ratio=%.5f\n",n,v,r); fflush(stdout);} }
    return 0;
  }
  for(int k=1;k<argc;k++){u64 n=strtoull(argv[k],0,10); long long v=A(n,mark); printf("%llu %lld ratio=%.5f\n",n,v,v/(n/log((double)n))); fflush(stdout);}
}
