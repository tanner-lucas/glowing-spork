// scan k: candidate exceptions to floor(C(N,4)^(1/4)) == floor((N-3/2)/24^(1/4))
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned __int128 u128;
int main(int argc, char**argv){
  uint64_t K = strtoull(argv[1],0,10);
  u128 F = ((u128)0x369f03385ff02ffeULL<<64) | 0xf6d8539ece1140a3ULL; // frac(24^(1/4))*2^128
  u128 half = (u128)1<<127;
  u128 phase = 0;
  uint64_t thr = (uint64_t)1<<63;
  for(uint64_t k=1;k<=K;k++){
    phase += F;
    if((k & ((1u<<16)-1))==0){
      double t = 0.7/(2.2134*(double)k)*18446744073709551616.0*1.5;
      thr = t > 9.2e18 ? ((uint64_t)1<<63) : (uint64_t)t;
    }
    u128 t = phase + half;
    uint64_t hi = (uint64_t)(t>>64);
    if((~hi) < thr){
      double delta = (double)(~hi)/18446744073709551616.0;
      double N = 2.2133638394006434*(double)k + 1.5;
      if(delta*N < 1.0) printf("%llu %.6g\n",(unsigned long long)k, delta*N);
    }
  }
  return 0;
}
