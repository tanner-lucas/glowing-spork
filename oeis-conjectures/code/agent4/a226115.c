#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
int main(int argc,char**argv){
  int N=atoi(argv[1]);
  // primes
  int LIM=N*25+100; char *c=calloc(LIM,1); ll *p=malloc(sizeof(ll)*(N+2)); int np=0;
  for(int i=2;i<LIM&&np<=N;i++){ if(!c[i]){ p[++np]=i; for(ll j=(ll)i*i;j<LIM;j+=i) c[j]=1; } }
  // alternating prefix: A[i]=sum_{j<=i} (-1)^j p_j
  ll *A=malloc(sizeof(ll)*(N+2)); A[0]=0; for(int i=1;i<=N;i++) A[i]=A[i-1]+((i&1)?-p[i]:p[i]);
  ll B=2*p[N]+10; uint8_t *seen=calloc(B/8+2,1);
  ll mex=1; double minf=1e9; int argf=0; int oddviol=0;
  for(int m=2;m<=N;m++){
    for(int k=1;k<m;k++){
      // S = p_m - p_{m-1} + ... +- p_k = (-1)^m (A[m]-A[k-1])
      ll S=((m&1)?-1:1)*(A[m]-A[k-1]);
      if(S>0 && S<B) seen[S>>3]|=1<<(S&7);
    }
    while(seen[mex>>3]&(1<<(mex&7))) mex++;
    ll a=mex; int n=m;
    if(n<=24) printf("%lld,",a);
    double f=sqrt(2.0*a)-sqrt((double)p[n])+0.7;
    if(f<minf && n!=651){minf=f;argf=n;}
    if(f<=0) printf("\nVIOLATION f n=%d a=%lld p=%lld f=%g\n",n,a,p[n],f);
    if(n>7 && (a&1)){ oddviol++; if(oddviol<10) printf("\nODD a(n) n=%d a=%lld\n",n,a);}
    if(n==651) printf("\n n=651 a=%lld f=%.6f\n",a,f);
  }
  printf("\nN=%d min f (excluding 651) = %.6f at n=%d, odd violations %d\n",N,minf,argf,oddviol);
}
