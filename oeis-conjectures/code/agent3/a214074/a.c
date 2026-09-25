#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); mpz_t a,b,x,y,g; mpz_inits(a,b,x,y,g,NULL);
  mpz_set_ui(a,1); mpz_set_ui(b,1);
  for(long n=1;n<=N;n++){
    mpz_mul_ui(a,a,2); mpz_mul_ui(b,b,3);
    long m=1;
    for(;;m++){ mpz_sub_ui(x,a,m); mpz_sub_ui(y,b,m); mpz_gcd(g,x,y); if(mpz_cmp_ui(g,1)==0) break; }
    printf("%ld %ld\n",n,m);
    if(n%5000==0){fflush(stdout);}
  }
}
