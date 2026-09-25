// Independent generator: self-reading construction of the fixed point of 0->1, 1->101010
// then exact integer check of the conjectured bounds using sqrt(21) comparisons in __int128.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef __int128 i128;
int main(){
  const long N = 30000000;
  char *w = malloc(N+16);
  long len = 0, rd = 0;
  // seed: w starts with 1 (fixed point beginning with sigma(1)=101010)
  const char *img0 = "1", *img1 = "101010";
  w[len++] = 1; // w[0]=1; reading w[0] must reproduce w[0..5]
  // self-reading: output = concatenation of images of w[rd]; the first image overwrites w[0..5]
  long out = 0;
  while(out < N){
    const char *im = w[rd] ? img1 : img0; rd++;
    for(int j=0; im[j] && out < N; j++){ w[out++] = im[j]-'0'; }
    if(out > len) len = out;
  }
  // print prefix
  for(int i=0;i<40;i++) putchar('0'+w[i]); putchar('\n');
  // count positions and test bounds exactly
  long n0=0, n1=0, v0=0, v1=0;
  for(long p=1; p<=N; p++){
    if(w[p-1]==0){ n0++;
      // u: n*r - a > 2  with r=(9+sqrt21)/6  <=> n*sqrt21 > 6a+12-9n
      i128 rhs = (i128)6*p + 12 - (i128)9*n0;
      int gt2 = (rhs < 0) || ((i128)21*n0*n0 > rhs*rhs);
      // u: n*r - a < -2 <=> n*sqrt21 < 6a - 12 - 9n
      i128 rhs2 = (i128)6*p - 12 - (i128)9*n0;
      int ltm2 = (rhs2 > 0) && ((i128)21*n0*n0 < rhs2*rhs2);
      if((gt2||ltm2) && v0 < 5){ v0++; printf("zeros: n=%ld a(n)=%ld violates %s\n", n0, p, gt2?"<2":">-2"); }
    } else { n1++;
      // v: n*s - a > 2  with s=(-1+sqrt21)/2 <=> n*sqrt21 > 2a+4+n
      i128 rhs = (i128)2*p + 4 + n1;
      int gt2 = (i128)21*n1*n1 > rhs*rhs;
      // v: n*s - a < -1 <=> n*sqrt21 < 2a - 2 + n
      i128 rhs2 = (i128)2*p - 2 + n1;
      int ltm1 = (rhs2 > 0) && ((i128)21*n1*n1 < rhs2*rhs2);
      if((gt2||ltm1) && v1 < 5){ v1++; printf("ones: n=%ld a(n)=%ld violates %s\n", n1, p, gt2?"<2":">-1"); }
    }
  }
  printf("counted %ld zeros, %ld ones\n", n0, n1);
  return 0;
}
