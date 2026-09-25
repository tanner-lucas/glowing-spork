#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
int main(int argc,char**argv){
  int N=atoi(argv[1]);
  mpz_t *a=malloc((N+1)*sizeof(mpz_t)); for(int i=0;i<=N;i++) mpz_init_set_ui(a[i], i==0);
  mpz_t C,t; mpz_init(C); mpz_init(t);
  for(int k=1;k<=N;k++){
    mpz_bin_uiui(C, N, k);
    for(int n=N;n>=k;n--){
      mpz_mul(t, C, a[n-k]); mpz_sub(a[n], a[n], t);
      // C(n-1,k) = C(n,k)*(n-k)/n
      if(n>k){ mpz_mul_ui(C, C, n-k); mpz_divexact_ui(C, C, n); }
    }
  }
  for(int i=0;i<=15;i++) gmp_printf("%Zd,", a[i]); printf("\n");
  long bad=0;
  for(int n=1;n<=N;n++){
    int s1=mpz_sgn(a[n]), s0=mpz_sgn(a[n-1]);
    if(s1==0||s0==0){ printf("zero at n=%d\n",n); continue; }
    int differs = (s1!=s0);
    long m=8L*n+1; long r=0; while((r+1)*(r+1)<=m) r++; int tri = (r*r==m);
    if(differs!=tri){ if(bad<20) printf("MISMATCH n=%d differs=%d triangular=%d\n",n,differs,tri); bad++; }
  }
  printf("N=%d mismatches=%ld\n",N,bad);
}
