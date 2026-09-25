#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// a(0)=1, a(n)=a(floor((n-1)/a(n-1)))+2
int main(int argc,char**argv){
  long long N=atoll(argv[1]); long long M=N/3+10;
  uint8_t *a=malloc(M); a[0]=1; int cur=1, rec=1;
  printf("record %d at 0\n",cur);
  for(long long n=1;n<=N;n++){
    long long idx=(n-1)/cur; if(idx>=M){fprintf(stderr,"idx overflow at n=%lld\n",n);return 1;}
    int nx=a[idx]+2;
    if(n<M) a[n]=nx;
    cur=nx;
    if(cur>rec){rec=cur; printf("record %d at %lld\n",cur,n); fflush(stdout);}
  }
  return 0;
}
