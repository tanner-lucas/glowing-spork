#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// a(0)=1, a(n+1)=a(floor(n/a(n)))+1 ; report record positions up to N
int main(int argc,char**argv){
  long long N=atoll(argv[1]); long long M=N/4+10; // store indices < M
  uint8_t *a=malloc(M); a[0]=1; int cur=1, rec=1;
  printf("record %d at 0\n",cur);
  for(long long n=0;n<N;n++){
    long long idx=n/cur; if(idx>=M){fprintf(stderr,"idx overflow at n=%lld\n",n);return 1;}
    int nx=a[idx]+1; // a(n+1)
    if(n+1<M) a[n+1]=nx;
    cur=nx;
    if(cur>rec){rec=cur; printf("record %d at %lld\n",cur,n+1); fflush(stdout);}
  }
  return 0;
}
