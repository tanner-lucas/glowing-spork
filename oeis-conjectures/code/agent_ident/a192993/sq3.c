#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef unsigned long long u64;
static int issq(u64 x){ if(x==0) return 0; u64 r=(u64)sqrtl((long double)x); while(r*r>x) r--; while((r+1)*(r+1)<=x) r++; return r*r==x; }
static u64 p10[20];
static int ndig(u64 x){int d=0; while(x){d++;x/=10;} return d;}
// count ways N = P|S with P,S nonzero squares, S has no leading zero
static int ways(u64 N){ int L=ndig(N), c=0; for(int j=1;j<L;j++){ u64 S=N%p10[j], P=N/p10[j]; if(S<p10[j-1]) continue; if(issq(P)&&issq(S)) c++; } return c; }
int main(int argc,char**argv){
  int LMAX=atoi(argv[1]); p10[0]=1; for(int i=1;i<20;i++) p10[i]=p10[i-1]*10;
  long long hits=0, two=0;
  for(int L=2; L<=LMAX; L++){
    for(int j=1;j<L;j++){ // suffix length j, prefix length L-j
      // suffix squares with exactly j digits; prefix squares with exactly L-j digits
      u64 slo=(u64)ceill(sqrtl((long double)p10[j-1])), shi=(u64)floorl(sqrtl((long double)(p10[j]-1)));
      u64 plo=(u64)ceill(sqrtl((long double)p10[L-j-1])), phi=(u64)floorl(sqrtl((long double)(p10[L-j]-1)));
      while(slo*slo<p10[j-1]) slo++; while((shi+1)*(shi+1)<=p10[j]-1) shi++;
      while(plo*plo<p10[L-j-1]) plo++; while((phi+1)*(phi+1)<=p10[L-j]-1) phi++;
      for(u64 a=plo;a<=phi;a++){ u64 P=a*a*p10[j];
        for(u64 b=slo;b<=shi;b++){ u64 N=P+b*b; int w=ways(N);
          if(w>=3){ printf("N=%llu ways=%d (found via %llu|%llu)\n",N,w,a*a,b*b); hits++; }
        }
      }
    }
    fprintf(stderr,"L=%d done hits=%lld\n",L,hits);
  }
  return 0;
}
