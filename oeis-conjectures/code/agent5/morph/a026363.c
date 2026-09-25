#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// a(1)=1; a(n)=a(n-1)+2 if n even and n/2 not in sequence, else a(n-1)+1  (Cloitre's formula in A026363)
int main(int argc,char**argv){ long long N=atoll(argv[1]); char *in=calloc(N+2,1); long long *a=malloc(sizeof(long long)*(N+1));
 long double r=(1.0L+sqrtl(3.0L))/2.0L, mn=1e9, mx=-1e9; long long amn=0,amx=0;
 a[1]=1; in[1]=1;
 for(long long n=2;n<=N;n++){ long long v; if(n%2==0 && (n/2<=N && in[n/2])) v=a[n-1]+2; else v=a[n-1]+1; a[n]=v; if(v<=N) in[v]=1; }
 for(long long n=1;n<=N;n++){ long double D=n*r-a[n]; if(D<mn){mn=D;amn=n;} if(D>mx){mx=D;amx=n;} }
 printf("N=%lld min D=%.12Lf at %lld  max D=%.12Lf at %lld\n",N,mn,amn,mx,amx);
 for(int i=1;i<=25;i++) printf("%lld,",a[i]); printf("\n"); return 0;}
