// a(n) = #{m<=n : gpf(m) == 1 mod 4}; test conjecture a(n) - n/2 < -sqrt(n) for n > 1000
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
int main(int argc,char**argv){
  uint64_t N = strtoull(argv[1],0,10);
  uint64_t S = (uint64_t)sqrt((double)N)+2;
  char *c = calloc(S+1,1); int *pr = malloc(sizeof(int)*S); int np=0;
  for(uint64_t i=2;i<=S;i++){ if(!c[i]){ pr[np++]=i; for(uint64_t j=i*i;j<=S;j+=i) c[j]=1; } }
  const uint64_t B = 1<<22;
  uint64_t *rem = malloc(B*8); uint32_t *last = malloc(B*4);
  int64_t a=0; double worst = -1e18; uint64_t worstn=0; uint64_t viol=0, firstviol=0;
  for(uint64_t L=1; L<=N; L+=B){
    uint64_t R = L+B-1; if(R>N) R=N; uint64_t len=R-L+1;
    for(uint64_t i=0;i<len;i++){ rem[i]=L+i; last[i]=1; }
    for(int k=0;k<np;k++){ uint64_t p=pr[k]; if(p*p>R) { /* still need to divide p out of numbers with p factor */ }
      uint64_t start = ((L+p-1)/p)*p;
      for(uint64_t m=start;m<=R;m+=p){ uint64_t i=m-L; while(rem[i]%p==0) rem[i]/=p; last[i]=p; }
    }
    for(uint64_t i=0;i<len;i++){
      uint64_t n=L+i; uint64_t g = rem[i]>1 ? rem[i] : last[i];
      if(n>1 && g%4==1) a++;
      if(n>1000){ double d = (double)a - n/2.0 + sqrt((double)n); // conjecture: d < 0
        if(d>worst){worst=d;worstn=n;}
        if(d>=0){ viol++; if(!firstviol) firstviol=n; }
      }
      if(n<=32) printf("%lld,",(long long)a);
    }
  }
  printf("\nN=%llu a(N)=%lld  a(N)-N/2=%.1f  sqrt(N)=%.1f  max over n>1000 of a(n)-n/2+sqrt(n) = %.3f at n=%llu ; violations=%llu first=%llu\n",
    (unsigned long long)N,(long long)a,(double)a-N/2.0,sqrt((double)N),worst,(unsigned long long)worstn,(unsigned long long)viol,(unsigned long long)firstviol);
  return 0;
}
