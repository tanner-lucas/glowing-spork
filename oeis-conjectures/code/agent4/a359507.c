#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64;
// a(n) = min k>=1: n ^ (n+k) in span{n+1..n+k-1}
static int inspan(u64 *basis, u64 v){ for(int b=63;b>=0;b--) if((v>>b)&1){ if(!basis[b]) return 0; v^=basis[b]; } return 1; }
static void add(u64 *basis, u64 v){ for(int b=63;b>=0;b--) if((v>>b)&1){ if(!basis[b]){ basis[b]=v; return;} v^=basis[b]; } }
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10); long bad=0;
  for(u64 n=1;n<=N;n++){
    u64 basis[64]={0}; u64 k;
    for(k=1;;k++){ if(k>=2) add(basis,n+k-1); if(inspan(basis, n^(n+k))) break; }
    if(n<=40) printf("%llu,",(unsigned long long)k);
    u64 m=k-1; if(m==0 || (m&(m-1))){ bad++; if(bad<20) printf("\nNOT 2^j+1: n=%llu a=%llu\n",(unsigned long long)n,(unsigned long long)k); }
  }
  printf("\nN=%llu violations=%ld\n",(unsigned long long)N,bad);
}
