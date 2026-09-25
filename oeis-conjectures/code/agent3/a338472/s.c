// odd composite n with (1 + sum_{k even, 2..n-1} 2*k^(n-1)) == 0 mod n  (direct O(n log n) check)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint64_t pw(uint64_t b,uint64_t e,uint64_t m){uint64_t r=1%m;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
int isprime(uint64_t n){if(n<2)return 0;for(uint64_t d=2;d*d<=n;d++)if(n%d==0)return 0;return 1;}
int main(int argc,char**argv){
  uint64_t N=atoll(argv[1]);
  for(uint64_t n=3;n<=N;n+=2){
    uint64_t s=1; for(uint64_t k=2;k<n;k+=2){ s=(s+2*pw(k,n-1,n))%n; }
    int pr=isprime(n);
    if((s==0)!=pr) printf("MISMATCH n=%llu prime=%d s=%llu\n",(unsigned long long)n,pr,(unsigned long long)s);
  }
  printf("done %llu\n",(unsigned long long)N);
}
