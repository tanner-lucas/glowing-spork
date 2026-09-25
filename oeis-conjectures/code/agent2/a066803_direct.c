/* Independent check: compute a(2^k) = gcd(2^N+1, 3^N+1), N=2^k, via GMP:
   r = 3^N mod F (F = 2^N+1) by k squarings, then gcd(F, r+1). */
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <time.h>
int main(int argc,char**argv){
  int k0=atoi(argv[1]), k1=atoi(argv[2]);
  for(int k=k0;k<=k1;k++){
    unsigned long N=1UL<<k; mpz_t F,r,g; mpz_inits(F,r,g,NULL);
    mpz_set_ui(F,0); mpz_setbit(F,N); mpz_add_ui(F,F,1);
    mpz_set_ui(r,3);
    for(int i=0;i<k;i++){ mpz_mul(r,r,r); mpz_mod(r,r,F); }
    mpz_add_ui(r,r,1);
    mpz_gcd(g,F,r);
    printf("k=%d a(2^k)=",k); mpz_out_str(stdout,10,g); printf("  [%.1fs]\n",(double)clock()/CLOCKS_PER_SEC); fflush(stdout);
    mpz_clears(F,r,g,NULL);
  }
  return 0;
}
