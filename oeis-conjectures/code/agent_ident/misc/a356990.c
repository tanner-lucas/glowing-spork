#include <stdio.h>
#include <stdlib.h>
int *a;
int main(int argc,char**argv){
  long N=atol(argv[1]); a=malloc(sizeof(int)*(N+2)); a[1]=1;
  for(long n=2;n<=N;n++){
    long x=n-1; for(int i=0;i<5;i++) x=a[x];
    long y=n-x; if(y<1||y>=n){printf("bad index at n=%ld\n",n);return 1;}
    for(int i=0;i<4;i++) y=a[y];
    a[n]=n-y;
    if(a[n]-a[n-1]<0||a[n]-a[n-1]>1){printf("not slow at %ld\n",n);}
  }
  // plateaus: maximal runs with equal values length>=2
  // A003269: 0,1,1,1,1,2,3,4,5,7,10,...
  long long t[200]; t[0]=0;t[1]=1;t[2]=1;t[3]=1; for(int i=4;i<200;i++) t[i]=t[i-1]+t[i-4];
  long n=1; int k=0; 
  while(n<=N){ long m=n; while(m+1<=N && a[m+1]==a[n]) m++; if(m>n && m<N){ printf("plateau height %d from n=%ld to %ld (len %ld)\n",a[n],n,m,m-n+1); } n=m+1; }
  return 0;
}
