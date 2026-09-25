// Independent combinatorial count (Lucy_Hedgehog / Legendre-type DP, no range sieve):
// computes pi(x) and D(x)=sum_{p<=x} chi3(p) = pi(x;3,1)-pi(x;3,2), chi3 = nontrivial char mod 3.
// Then A(x)=#{p<=x, p==1 mod 6} = pi(x;3,1), B(x)=#{p<=x, p==5 mod 6} = pi(x;3,2)-1.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int64_t chisum(int64_t v){ // sum_{2<=n<=v} chi(n)
  if(v<1) return 0; int64_t c1=(v+2)/3, c2=(v+1)/3; return c1-c2-1; }
int main(int argc,char**argv){
  for(int a=1;a<argc;a++){
  int64_t x=strtoll(argv[a],0,10);
  int64_t r=(int64_t)sqrtl((long double)x); while(r*r>x) r--; while((r+1)*(r+1)<=x) r++;
  // values v = x/i for i=1..r (large), and v=1..r (small)
  int64_t *L1=malloc(8*(r+2)), *Lc=malloc(8*(r+2)), *S1=malloc(8*(r+2)), *Sc=malloc(8*(r+2));
  for(int64_t i=1;i<=r;i++){ int64_t v=x/i; L1[i]=v-1; Lc[i]=chisum(v); }
  for(int64_t v=0;v<=r;v++){ S1[v]= v>=1? v-1:0; Sc[v]=chisum(v); }
  for(int64_t p=2;p<=r;p++){
    if(S1[p]==S1[p-1]) continue; // p not prime
    int64_t sp1=S1[p-1], spc=Sc[p-1]; int64_t fp = (p%3==1)?1:((p%3==2)?-1:0);
    int64_t p2=p*p;
    int64_t lim = x/p2; if(lim>r) lim=r;
    for(int64_t i=1;i<=lim;i++){
      int64_t ip=i*p; int64_t a1,ac;
      if(ip<=r){ a1=L1[ip]; ac=Lc[ip]; } else { int64_t w=x/ip; a1=S1[w]; ac=Sc[w]; }
      L1[i]-= a1-sp1;
      Lc[i]-= fp*(ac-spc);
    }
    for(int64_t v=r; v>=p2; v--){ int64_t w=v/p; S1[v]-= S1[w]-sp1; Sc[v]-= fp*(Sc[w]-spc); }
  }
  int64_t pi=L1[1], D=Lc[1];
  int64_t p31=(pi-1+D)/2, p32=(pi-1-D)/2;
  printf("x=%lld pi=%lld pi(x;3,1)=%lld pi(x;3,2)=%lld  A=%lld B=%lld\n",(long long)x,(long long)pi,(long long)p31,(long long)p32,(long long)p31,(long long)(p32-1));
  free(L1);free(Lc);free(S1);free(Sc);
  }
}
