// Independent brute force: are 1^2,2^2,...,N^2 pairwise distinct mod M ?
// squares computed incrementally (k^2 = (k-1)^2 + 2k-1), residues bucketed by r % P, each bucket sorted.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int cmp(const void*a,const void*b){uint64_t x=*(uint64_t*)a,y=*(uint64_t*)b;return x<y?-1:x>y;}
int main(int argc,char**argv){
  uint64_t M=strtoull(argv[1],0,10), N=strtoull(argv[2],0,10); int P=atoi(argv[3]);
  size_t cap=(size_t)(N/P*1.05)+1000; uint64_t*buf=malloc(cap*8);
  long dups=0;
  for(int p=0;p<P;p++){
    size_t cnt=0; uint64_t s=0;
    for(uint64_t k=1;k<=N;k++){
      s+=2*k-1; while(s>=M) s-=M;   // s = k^2 mod M
      if((int)((s*0x9E3779B97F4A7C15ULL)>>58)%P==p){ if(cnt>=cap){cap=cap*3/2; buf=realloc(buf,cap*8); if(!buf){fprintf(stderr,"oom\n");return 2;}} buf[cnt++]=s; }
    }
    qsort(buf,cnt,8,cmp);
    for(size_t i=1;i<cnt;i++) if(buf[i]==buf[i-1]){ dups++; if(dups<=3) printf("collision residue %llu in bucket %d\n",(unsigned long long)buf[i],p);}
    fprintf(stderr,"pass %d done cnt=%zu dups=%ld\n",p,cnt,dups);
  }
  printf("M=%llu N=%llu duplicate residues found: %ld\n",(unsigned long long)M,(unsigned long long)N,dups);
  return 0;
}
