#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
  long N = atol(argv[1]);
  int *a = calloc(N+1,sizeof(int)); a[0]=1;
  long L0=2, L1=1; long L[100]; int m=0; L[m++]=2; L[m++]=1;
  while(1){ long t=L0+L1; L0=L1; L1=t; if(t>N) break; L[m++]=t; }
  for(int k=0;k<m;k++){ long l=L[k]; for(long i=N;i>=l;i--) a[i]-=a[i-l]; }
  int mn=0,mx=0; long imn=0,imx=0;
  for(long i=0;i<=N;i++){ if(a[i]<mn){mn=a[i];imn=i;} if(a[i]>mx){mx=a[i];imx=i;} }
  printf("N=%ld  factors=%d  min=%d at %ld  max=%d at %ld\n",N,m,mn,imn,mx,imx);
  for(int i=0;i<30;i++) printf("%d,",a[i]); printf("\n");
  long first=-1; for(long i=0;i<=N;i++) if(a[i]>2||a[i]<-2){first=i;break;}
  printf("first |a|>2: %ld\n", first);
  return 0;
}
