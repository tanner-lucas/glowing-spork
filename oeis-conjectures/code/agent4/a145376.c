#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long ull;
static ull isq(ull v){ ull r=(ull)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r; }
static int istri(ull t){ ull d=8*t+1, s=isq(d); return s*s==d; }
static ull Tge(ull x){ // smallest triangular >= x
  ull k=(isq(8*x+1)-1)/2; ull t=k*(k+1)/2; while(t<x){k++; t=k*(k+1)/2;} return t; }
int main(int argc,char**argv){
  int N=atoi(argv[1]); int L=20000000; char*c=calloc(L,1); int *pr=malloc(sizeof(int)*2000000); int np=0;
  for(int i=2;i<L;i++) if(!c[i]){ pr[np++]=i; for(long j=(long)i*i;j<L;j+=i) c[j]=1; }
  int prev=0; long viol=0;
  for(int n=1;n<=N;n++){ ull p=pr[n-1]; int a=-1;
    for(int i=0;i<np;i++){ ull q=pr[i]; ull x=q*p; if(istri(Tge(x)-x)){ a=q; break; } }
    if(n<=25) printf("%d,",a);
    if(n>=3 && a<prev){ viol++; if(viol<10) printf("\nDECREASE n=%d a(n-1)=%d a(n)=%d\n",n,prev,a); }
    prev=a;
  }
  printf("\nN=%d decreases=%ld\n",N,viol);
}
