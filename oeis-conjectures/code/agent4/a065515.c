#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long ull;
static ull iroot(ull n,int k){ ull r=(ull)pow((long double)n,1.0L/k); while(r>0){ // adjust
    long double t=powl((long double)r,k); if(t>(long double)n) r--; else break;} 
  while(1){ long double t=powl((long double)(r+1),k); if(t<=(long double)n) r++; else break;} return r;}
static int cmp(const void*a,const void*b){ull x=*(ull*)a,y=*(ull*)b; return x<y?-1:x>y;}
int main(int argc,char**argv){
  ull N=strtoull(argv[1],0,10);
  ull S=iroot(N,2);
  // enumerate perfect powers m in [4,N]
  size_t cap=S+ (size_t)(3*pow((double)N,1.0/3))+100000; ull *pp=malloc(cap*8); size_t c=0;
  for(int k=2;k<64;k++){ ull r=iroot(N,k); if(r<2) break; for(ull b=2;b<=r;b++){ ull m=1; for(int i=0;i<k;i++) m*=b; pp[c++]=m; } }
  qsort(pp,c,8,cmp);
  size_t u=0; for(size_t i=0;i<c;i++) if(u==0||pp[i]!=pp[u-1]) pp[u++]=pp[i];
  ull L=S+u+10; // pi table up to L
  uint32_t *pi=malloc((L+1)*4); uint8_t *comp=calloc(L+1,1);
  for(ull i=2;i*i<=L;i++) if(!comp[i]) for(ull j=i*i;j<=L;j+=i) comp[j]=1;
  uint32_t cnt=0; pi[0]=pi[1]=0; for(ull i=2;i<=L;i++){ if(!comp[i]) cnt++; pi[i]=cnt; }
  long viol=0; double minmargin=1e18; ull argmin=0;
  // check at each perfect power m (and n from m to next-1 same values). Also n<4: PP=1, pi(1)=0, S>=0 ok.
  for(size_t i=0;i<u;i++){
    ull m=pp[i]; ull PPn=1+(i+1); // include 1
    ull Ssum=0; for(int k=2;k<64;k++){ ull r=iroot(m,k); if(r<2) break; Ssum+=pi[r]; }
    long long margin=(long long)Ssum-(long long)pi[PPn];
    if(margin<0){ viol++; if(viol<20) printf("VIOLATION n=%llu S=%llu pi(PP)=%u PP=%llu\n",m,Ssum,pi[PPn],PPn); }
    if(m>1000 && (double)margin/ (double)(pi[iroot(m,3)]+1) < minmargin){minmargin=(double)margin/(pi[iroot(m,3)]+1); argmin=m;}
  }
  printf("N=%llu perfect powers=%zu violations=%ld min relative margin %.4f at %llu\n",N,u,viol,minmargin,argmin);
}
