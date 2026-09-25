#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  int *phi=malloc((N+1)*sizeof(int));
  for(long i=0;i<=N;i++) phi[i]=i;
  for(long p=2;p<=N;p++) if(phi[p]==p) for(long m=p;m<=N;m+=p) phi[m]-=phi[m]/p;
  long double S=0, c=3.0L/(M_PI*M_PI);
  double mn=1e9,mx=-1e9; long cntHi=0,cntLo=0; long amn=0,amx=0;
  double hist[40]={0};
  for(long k=1;k<=N;k++){ S+=phi[k]; if(k<1000) continue;
    double e=(double)((S - c*(long double)k*k)/k);
    if(e<mn){mn=e;amn=k;} if(e>mx){mx=e;amx=k;}
    int b=(int)floor((e+1.0)*10); if(b<0)b=0; if(b>39)b=39; hist[b]++;
  }
  printf("min e=%.4f at %ld, max e=%.4f at %ld\n",mn,amn,mx,amx);
  for(int b=0;b<40;b++) if(hist[b]>0) printf("[%.1f,%.1f): %.0f\n",b/10.0-1,(b+1)/10.0-1,hist[b]);
}
