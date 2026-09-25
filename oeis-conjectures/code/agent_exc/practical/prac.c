// Enumerate practical numbers up to X via segmented sieve (Stewart-Sierpinski criterion),
// check Sun's conjecture p(n)^(1/n) strictly decreasing: R(n)= n*log(p(n+1)/p(n))/log(p(n)) < 1.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define S (1<<18)   // even numbers per segment
int main(int argc,char**argv){
  uint64_t X=strtoull(argv[1],0,10);
  uint64_t r=(uint64_t)sqrt((double)X)+2;
  char*c=calloc(r+1,1); uint32_t*P=malloc(4*r); int np=0;
  for(uint64_t i=2;i<=r;i++){ if(!c[i]){P[np++]=i; for(uint64_t j=i*i;j<=r;j+=i) c[j]=1;} }
  static uint64_t cof[S], sig[S]; static unsigned char ok[S];
  // small practical numbers: 1,2 handled: start n-count with 1 (the number 1)
  uint64_t cnt=1, prev=1; double maxR=-1; uint64_t maxRn=0, maxRp=0; uint64_t maxgap=0, maxgapp=0;
  int nfail=0;
  // process even numbers m=2*(base+j)
  for(uint64_t base=1; 2*base<=X; base+=S){
    uint64_t len=S; if(2*(base+len-1)>X) len=(X/2)-base+1;
    for(uint64_t j=0;j<len;j++){ uint64_t m=2*(base+j); uint64_t v=m; uint64_t s=1,pw=1; while(!(v&1)){v>>=1; pw<<=1; s+=pw;} cof[j]=v; sig[j]=s; ok[j]=1; }
    for(int i=1;i<np;i++){ uint64_t p=P[i]; if((uint64_t)p*p>2*(base+len-1)) {
          // remaining primes > sqrt(max m) : handled after loop as cofactor
          break; }
      // first j with 2*(base+j) % p ==0  -> (base+j)%p==0
      uint64_t j0=(p - base%p)%p;
      for(uint64_t j=j0;j<len;j+=p){ if(!ok[j]) continue;
        if(p>sig[j]+1){ ok[j]=0; continue; }
        uint64_t v=cof[j]/p, pw=p, s=1+p; while(v%p==0){v/=p; pw*=p; s+=pw;} cof[j]=v; sig[j]*=s; }
    }
    for(uint64_t j=0;j<len;j++){
      if(!ok[j]) continue; uint64_t v=cof[j];
      if(v>1){ // v is 1 or a product of primes > sqrt(m) -> at most one such prime (m<=X, primes > sqrt(m)) ... but primes > P[] loop bound: v could be prime or composite with primes > sqrt(maxm)? v<=m, all prime factors >= loop limit > sqrt(m) => v prime
        if(v>sig[j]+1) continue; }
      uint64_t m=2*(base+j);
      // m practical
      cnt++; // m is cnt-th practical number (counting 1 as first)
      if(prev>=2){ double R = (double)(cnt-1)*log((double)m/(double)prev)/log((double)prev);
        if(cnt-1>=3 && R>maxR){maxR=R;maxRn=cnt-1;maxRp=prev;}
        if(cnt-1>=3 && R>=0.999){ nfail++; if(nfail<50) printf("NEAR/FAIL n=%lu p(n)=%lu p(n+1)=%lu R=%.9f\n",cnt-1,prev,m,R);} }
      if(m-prev>maxgap){maxgap=m-prev;maxgapp=prev; printf("gap %lu after %lu (n=%lu) log^2/c=%.1f\n",maxgap,prev,cnt-1,log((double)prev)*log((double)prev)/1.336);} 
      prev=m;
    }
  }
  printf("END X=%lu count=%lu maxR=%.9f at n=%lu p=%lu\n",X,cnt,maxR,maxRn,maxRp);
}
