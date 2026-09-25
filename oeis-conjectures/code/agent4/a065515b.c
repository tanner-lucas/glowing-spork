#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long ull; typedef unsigned __int128 u128;
static int cmp(const void*a,const void*b){ull x=*(ull*)a,y=*(ull*)b; return x<y?-1:x>y;}
static ull ipow_sat(ull b,int k,ull lim){ u128 r=1; for(int i=0;i<k;i++){ r*=b; if(r>lim) return lim+1;} return (ull)r; }
int main(int argc,char**argv){
  ull N=strtoull(argv[1],0,10);
  ull S=(ull)sqrtl((long double)N); while(S*S>N) S--; while((S+1)*(S+1)<=N) S++;
  size_t cap=S+ (size_t)(3*cbrt((double)N))+100000; ull *pp=malloc(cap*8); size_t c=0;
  for(int k=2;k<64;k++){ for(ull b=2;;b++){ ull m=ipow_sat(b,k,N); if(m>N) break; pp[c++]=m; } if(ipow_sat(2,k+1,N)>N) break; }
  qsort(pp,c,8,cmp);
  size_t u=0; for(size_t i=0;i<c;i++) if(u==0||pp[i]!=pp[u-1]) pp[u++]=pp[i];
  ull L=S+u+10;
  uint32_t *pi=malloc((L+1)*4); uint8_t *comp=calloc(L+1,1);
  for(ull i=2;i*i<=L;i++) if(!comp[i]) for(ull j=i*i;j<=L;j+=i) comp[j]=1;
  uint32_t cnt=0; pi[0]=pi[1]=0; for(ull i=2;i<=L;i++){ if(!comp[i]) cnt++; pi[i]=cnt; }
  ull r[64]; for(int k=0;k<64;k++) r[k]=1;
  long viol=0; long long minmargin=1LL<<60; ull argmin=0;
  for(size_t i=0;i<u;i++){
    ull m=pp[i]; ull PPn=1+(i+1);
    ull Ssum=0;
    for(int k=2;k<64;k++){ while(ipow_sat(r[k]+1,k,m)<=m) r[k]++; if(r[k]<2) break; Ssum+=pi[r[k]]; }
    long long margin=(long long)Ssum-(long long)pi[PPn];
    if(margin<0){ viol++; if(viol<20) printf("VIOLATION n=%llu S=%llu pi(PP)=%u PP=%llu\n",m,Ssum,pi[PPn],PPn); }
    if(m>100000 && margin<minmargin){minmargin=margin;argmin=m;}
  }
  printf("N=%llu perfect powers=%zu violations=%ld min margin(n>1e5) %lld at %llu\n",N,u,viol,minmargin,argmin);
}
