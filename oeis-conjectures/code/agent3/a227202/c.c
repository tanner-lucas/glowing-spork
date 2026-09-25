// A227202: a(1)=2; a(n)= least prime q > a(n-1) such that a(n-1) is a primitive root mod q (per the Mathematica program).
// Compare with prime(floor(n*e)) and prime(ceil(n*e)).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned __int128 u128;
static uint64_t pw(uint64_t b,uint64_t e,uint64_t m){uint64_t r=1%m;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
int main(int argc,char**argv){
  long NT=atol(argv[1]); long L=atol(argv[2]);
  uint32_t *spf=calloc(L+1,4); 
  for(long i=2;i<=L;i++) if(!spf[i]){ for(long j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i; }
  // prime list
  long np=0; for(long i=2;i<=L;i++) if(spf[i]==i) np++;
  uint32_t *pr=malloc(4*np); long c=0; for(long i=2;i<=L;i++) if(spf[i]==i) pr[c++]=i;
  long idx=0; // index in pr of current term
  uint64_t p=2; long viol=0;
  for(long n=1;n<=NT;n++){
    if(n>1){
      long j=idx+1;
      for(;;j++){ if(j>=np){fprintf(stderr,"sieve too small at n=%ld\n",n);return 1;}
        uint64_t q=pr[j]; if(p%q==0) continue; uint64_t m=q-1; int ok=1;
        while(m>1){ uint64_t r=spf[m]; if(pw(p,(q-1)/r,q)==1){ok=0;break;} while(m%r==0) m/=r; }
        if(ok) break; }
      idx=j; p=pr[j];
    }
    if(n<=60) printf("%llu%s",(unsigned long long)p, n==60?"\n":",");
    long f=(long)floor(n*M_E), cc=(long)ceil(n*M_E);
    if(cc-1<np){ uint64_t pf=pr[f-1], pc=pr[cc-1];
      if(!(p<pf)) { viol++; if(viol<=30) printf("n=%ld a(n)=%llu prime(floor(n e))=%llu prime(ceil(n e))=%llu %s\n",n,(unsigned long long)p,(unsigned long long)pf,(unsigned long long)pc, p<pc?"(only floor-version violated)":"(both violated)"); }
    }
  }
  printf("done NT=%ld violations(floor)=%ld\n",NT,viol);
}
