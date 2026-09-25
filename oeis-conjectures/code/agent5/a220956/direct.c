// Direct computation of A220956(n) = (C(2n,n) - C(2n-2,n-1)) mod n^2 - n - 2 using exact GMP binomials.
#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv){
  unsigned long n = strtoul(argv[1], 0, 10);
  mpz_t a, b, m, r;
  mpz_inits(a, b, m, r, NULL);
  mpz_bin_uiui(a, 2*n, n);
  mpz_bin_uiui(b, 2*n-2, n-1);
  fprintf(stderr, "bits of C(2n,n): %lu\n", (unsigned long)mpz_sizeinbase(a,2));
  mpz_set_ui(m, n); mpz_mul_ui(m, m, n);
  mpz_sub(r, a, b);
  mpz_mod(r, r, m);          // nonnegative residue in [0, n^2)
  gmp_printf("n=%lu  (C(2n,n)-C(2n-2,n-1)) mod n^2 = %Zd\n", n, r);
  mpz_sub_ui(r, r, n); mpz_sub_ui(r, r, 2);
  gmp_printf("a(n) = %Zd\n", r);
  // also C(2n-1,n-1) mod n^2
  mpz_bin_uiui(a, 2*n-1, n-1);
  mpz_mod(a, a, m);
  gmp_printf("C(2n-1,n-1) mod n^2 = %Zd\n", a);
  return 0;
}
