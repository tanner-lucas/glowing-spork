// A294646: a(n) = (1/2)^(2n) mod (2n+1). Conjecture: a(n) never 2, 2n, 2n-2.
// With m=2n+1: a = 2^{-(m-1)} mod m.  a==2 <=> 2^m==1 (mod m); a==m-1 <=> 2^(m-1)==-1; a==m-3 <=> 3*2^(m-1)==-1 (mod m)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint64_t pw(uint64_t b,uint64_t e,uint64_t m){uint64_t r=1%m;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
int main(int argc,char**argv){
  uint64_t N=atoll(argv[1]); long hits=0;
  for(uint64_t n=1;n<=N;n++){ uint64_t m=2*n+1; uint64_t t=pw(2,m-1,m); // 2^(m-1)
    // a = inverse of t mod m ; check a in {2, m-1, m-3} via t*2==1, t==m-1, 3t==-1
    if((u128)t*2%m==1 || t==m-1 || ((u128)3*t+1)%m==0){ hits++; printf("n=%llu m=%llu t=%llu\n",(unsigned long long)n,(unsigned long long)m,(unsigned long long)t); }
  }
  printf("done N=%llu hits=%ld\n",(unsigned long long)N,hits);
}
