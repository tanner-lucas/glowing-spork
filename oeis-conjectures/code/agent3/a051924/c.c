// A051924: a(n)=C(2n,n)-C(2n-2,n-1). Conjecture: a(n) mod n^2 == n+2 iff n odd prime.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static uint64_t pw(uint64_t b,uint64_t e,uint64_t m){uint64_t r=1%m;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
static int *primes; static int np;
// v_q(m!) 
static uint64_t vfact(uint64_t m,uint64_t q){uint64_t v=0;while(m){m/=q;v+=m;}return v;}
static uint64_t binom_mod(uint64_t a,uint64_t b,uint64_t M){ // C(a,b) mod M via prime factorization
  uint64_t r=1%M;
  for(int i=0;i<np && (uint64_t)primes[i]<=a;i++){ uint64_t q=primes[i]; uint64_t v=vfact(a,q)-vfact(b,q)-vfact(a-b,q); if(v) r=(u128)r*pw(q,v,M)%M; }
  return r;
}
int main(int argc,char**argv){
  uint64_t N=atoll(argv[1]); uint64_t L=2*N+2;
  char*c=calloc(L+1,1); primes=malloc(sizeof(int)*L); np=0;
  for(uint64_t i=2;i<=L;i++){ if(!c[i]){primes[np++]=i; for(uint64_t j=i*i;j<=L;j+=i)c[j]=1;} }
  long mism=0;
  for(uint64_t n=2;n<=N;n++){
    uint64_t M=n*n; uint64_t A=(binom_mod(2*n,n,M)+M-binom_mod(2*n-2,n-1,M))%M;
    int isp=!c[n]; int odd_prime= isp && n>2;
    int cond=(A==(n+2)%M);
    if(cond!=odd_prime){ mism++; printf("MISMATCH n=%llu a(n) mod n^2=%llu oddprime=%d\n",(unsigned long long)n,(unsigned long long)A,odd_prime); fflush(stdout);}
  }
  printf("done N=%llu mismatches=%ld\n",(unsigned long long)N,mism);
}
