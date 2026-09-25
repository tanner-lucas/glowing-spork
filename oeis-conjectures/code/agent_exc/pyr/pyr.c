#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
// min number of k-gonal pyramidal numbers P_k(m)=m(m+1)((k-2)m-(k-5))/6 (m>=1) summing to n, n<=N
int main(int argc,char**argv){
  int k0=atoi(argv[1]), k1=atoi(argv[2]); long N=atol(argv[3]);
  unsigned char *d=malloc(N+1);
  for(int k=k0;k<=k1;k++){
    long v[5000]; int nv=0;
    for(long m=1;;m++){ long P=m*(m+1)*((k-2)*m-(k-5))/6; if(P>N) break; v[nv++]=P; }
    d[0]=0; for(long n=1;n<=N;n++){ int best=255; for(int i=0;i<nv && v[i]<=n;i++){ int t=d[n-v[i]]+1; if(t<best) best=t; } d[n]=best; }
    int mx=0; long arg=0, cntbad=0, lastbad=0; for(long n=1;n<=N;n++){ if(d[n]>mx){mx=d[n];arg=n;} if(d[n]>k+2){cntbad++; lastbad=n;} }
    printf("k=%d max=%d at n=%ld (k+2=%d) #n needing >k+2: %ld, largest %ld\n",k,mx,arg,k+2,cntbad,lastbad);
    if(cntbad){ printf("  first few:"); int c=0; for(long n=1;n<=N&&c<15;n++) if(d[n]>k+2){printf(" %ld(%d)",n,d[n]);c++;} printf("\n"); }
    fflush(stdout);
  }
}
