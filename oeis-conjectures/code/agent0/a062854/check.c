#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
long long A(u64 n, unsigned char *mark){
  memset(mark,0,n+1);
  for(u64 a=1;a<n;a++){ u64 g=gcd(a,n); u64 step=n/g; u64 b0=((a+step-1)/step)*step;
    for(u64 b=b0;b<n;b+=step){ mark[(a/g)*(b/step)]=1; } }
  long long c=0; for(u64 i=1;i<=n;i++) if(!mark[i]) c++; return c;
}
int isprime(u64 x){ if(x<2) return 0; for(u64 d=2;d*d<=x;d++) if(x%d==0) return 0; return 1;}
int main(){
  int N=20000; unsigned char *mark=malloc(N+2); int bad=0; double minr=1e9; int argmin=0;
  for(u64 n=3;n<=N;n++){
    long long v=A(n,mark);
    // lower bound L = #{p prime, sqrt(n) < p <= n, p does not divide n}
    long long L=0; for(u64 p=1;p<=n;p++) if(p*p>n && isprime(p) && n%p) L++;
    if(v<L){printf("LOWER BOUND FAILS n=%llu a=%lld L=%lld\n",n,v,L);bad=1;}
    double r=v/(n/log((double)n)); if(r<minr){minr=r;argmin=n;}
    if(!(v> n/log((double)n))){printf("CONJ FAILS n=%llu\n",n);bad=1;}
  }
  printf("checked n=3..%d, bad=%d, min ratio %.6f at n=%d\n",N,bad,minr,argmin);
}
