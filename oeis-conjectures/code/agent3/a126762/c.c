// A126762: least k>n with n^k == n (mod k). Conjecture (Ordowski): least k>n with n^(k-1)==1 (mod k), i.e. min is coprime to n.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint64_t pw(uint64_t b,uint64_t e,uint64_t m){uint64_t r=1%m;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
static uint64_t gcd(uint64_t a,uint64_t b){while(b){uint64_t t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  uint64_t N=atoll(argv[1]); long viol=0;
  for(uint64_t n=1;n<=N;n++){
    uint64_t k=n+1;
    for(;;k++){ if(pw(n,k,k)==n%k) break; }
    // k is a(n); conjecture requires gcd(n,k)==1 and n^(k-1)==1 mod k
    if(gcd(n,k)!=1 || pw(n,k-1,k)!=1%k){ viol++; if(viol<=20) printf("VIOLATION n=%llu a(n)=%llu gcd=%llu\n",(unsigned long long)n,(unsigned long long)k,(unsigned long long)gcd(n,k)); }
    if(argc>2 && n<=74) printf("%llu ",(unsigned long long)k);
  }
  printf("\nN=%llu violations=%ld\n",(unsigned long long)N,viol);
}
