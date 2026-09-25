#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int isprime(long m){ if(m<2) return 0; for(long d=2;d*d<=m;d++) if(m%d==0) return 0; return 1; }
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc,char**argv){
  long N=atol(argv[1]); long bad=0;
  for(long n=3;n<=N;n++){
    long m=2*n-1; // compute p_2 and p_3 mod m
    int64_t a=1%m, b=(n+1)%m; // a=p_{k+2}, b=p_{k+1}; start k=n-1
    for(long k=n-1;k>=2;k--){ int64_t c = ((k%m)*b - ((k+1)%m)*a) % m; if(c<0) c+=m; a=b; b=c; }
    // now b = p_2 mod m (should be 0), a = p_3 mod m
    if(b!=0){ printf("p2 not 0 mod m at n=%ld\n",n); }
    long g = gcdl(a, m); if(a==0) g=m;
    long den = m/g;
    if(den!=1 && !isprime(den)){ printf("VIOLATION n=%ld denominator %ld\n",n,den); bad++; }
  }
  printf("checked n<=%ld, violations %ld\n",N,bad);
}
