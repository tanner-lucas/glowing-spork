#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64;
// minimal base: t = c^y with c not a perfect power
static u64 ipow(u64 b,int e){u64 r=1; while(e--) r*=b; return r;}
static u64 minbase(u64 t){ for(int y=62;y>=2;y--){ u64 c=(u64)llround(pow((double)t,1.0/y)); for(u64 cc=(c>2?c-1:1); cc<=c+1; cc++){ if(cc<2) continue; u64 v=1; int ok=1; for(int i=0;i<y;i++){ if(v> t/cc){ok=0;break;} v*=cc;} if(ok && v==t) return minbase(cc);} } return t; }
int main(int argc,char**argv){
  long N=atol(argv[1]);
  uint32_t *spf=calloc(N+1,sizeof(uint32_t));
  for(long i=2;i<=N;i++) if(!spf[i]){ spf[i]=i; if((u64)i*i<=(u64)N) for(long j=(long)i*i;j<=N;j+=i) if(!spf[j]) spf[j]=i; }
  static uint32_t mb[1<<16]; for(u64 t=2;t<(1<<16);t++) mb[t]=(uint32_t)minbase(t);
  long found=0;
  for(long n=2;n<=N;n++){
    long m=n; u64 tau=1, sig=1;
    while(m>1){ u64 p=spf[m]; int e=0; u64 pk=1, s=1; while(m%p==0){m/=p;e++; pk*=p; s+=pk;} tau*=(e+1); sig*=s; }
    u64 c= tau<(1<<16)? mb[tau] : minbase(tau);
    // is sig a power of c?
    u64 v=sig; while(v%c==0) v/=c;
    if(v==1){ // candidate
      int mersenne_prod = ((sig & (sig-1))==0); // sigma power of 2 <=> product of distinct Mersenne primes
      if(!mersenne_prod){ printf("COUNTEREXAMPLE n=%ld tau=%llu sigma=%llu base=%llu\n",n,(unsigned long long)tau,(unsigned long long)sig,(unsigned long long)c); found++; }
    }
  }
  printf("N=%ld counterexamples=%ld\n",N,found);
}
