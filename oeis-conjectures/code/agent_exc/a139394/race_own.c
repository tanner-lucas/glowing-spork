// Independent segmented sieve (own code, no primesieve) for the race 1 mod 6 vs 5 mod 6.
// Sieves the two progressions 6k+1 and 6k+5 separately (byte arrays), k in [k0,k1).
// Tracks A=#{p==1 mod 6}, B=#{p==5 mod 6} and reports events a(n)<=0 of A139394 and counts at query points.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define S (1<<19)
static unsigned char s1[S], s5[S];
int main(int argc,char**argv){
  uint64_t k0=strtoull(argv[1],0,10), k1=strtoull(argv[2],0,10);
  int64_t A=strtoll(argv[3],0,10), B=strtoll(argv[4],0,10);
  uint64_t lastp=strtoull(argv[5],0,10);     // last prime (>=5) before 6*k0+1
  int nq=argc-6; uint64_t *qx=malloc(sizeof(uint64_t)*(nq+1)); for(int i=0;i<nq;i++) qx[i]=strtoull(argv[6+i],0,10);
  int qi=0;
  uint64_t xmax=6*k1+5; uint64_t r=(uint64_t)sqrtl((long double)xmax)+2;
  char*c=calloc(r+1,1); for(uint64_t i=2;i*i<=r;i++) if(!c[i]) for(uint64_t j=i*i;j<=r;j+=i) c[j]=1;
  uint64_t np=0; uint32_t *P=malloc(sizeof(uint32_t)*r); for(uint64_t i=17;i<=r;i++) if(!c[i]) P[np++]=i;
  uint64_t *o1=malloc(8*np), *o5=malloc(8*np);
  for(uint64_t i=0;i<np;i++){ uint64_t p=P[i];
    // smallest k>=k0 with 6k+r == 0 mod p and 6k+r >= p*p
    uint64_t inv6=0; for(uint64_t t=1;t<p;t++) if((6*t)%p==1){inv6=t;break;}
    for(int rr=0;rr<2;rr++){ uint64_t res = rr==0?1:5; uint64_t kc = ((p - res%p)%p)*inv6 % p; // k == -res/6 mod p
      uint64_t kmin = (p*p - res + 5)/6; if(kmin<k0) kmin=k0;
      uint64_t k = kmin + ((kc + p - kmin%p)%p);
      if(rr==0) o1[i]=k; else o5[i]=k; }
  }
  // presieve pattern for 5,7,11,13 : period 5005 in k
  const int PER=5005; unsigned char *pat1=malloc(S+PER), *pat5=malloc(S+PER);
  for(int k=0;k<S+PER;k++){ uint64_t a=6*(uint64_t)k+1, b=6*(uint64_t)k+5; pat1[k]=(a%5&&a%7&&a%11&&a%13); pat5[k]=(b%5&&b%7&&b%11&&b%13); }
  int64_t maxlead=-(1LL<<60); uint64_t maxx=0; long neg=0, zero=0; int printed=0;
  uint64_t nextck = 10000000000ULL*((6*k0)/10000000000ULL+1);
  for(uint64_t kb=k0; kb<k1; kb+=S){
    uint64_t len = (k1-kb<S)? k1-kb : S;
    memcpy(s1, pat1 + (kb%PER), len); memcpy(s5, pat5 + (kb%PER), len);
    if(kb==0){ s1[0]=0; s1[1]=1; s1[2]=1; /*7,13*/ s5[0]=1; s5[1]=1; /*5,11*/ }
    uint64_t kend=kb+len;
    for(uint64_t i=0;i<np;i++){ uint64_t p=P[i]; uint64_t k;
      for(k=o1[i]; k<kend; k+=p) s1[k-kb]=0; o1[i]=k;
      for(k=o5[i]; k<kend; k+=p) s5[k-kb]=0; o5[i]=k; }
    for(uint64_t j=0;j<len;j++){
      uint64_t k=kb+j;
      if(s1[j]){ uint64_t x=6*k+1;
        while(qi<nq && qx[qi]<x){ printf("Q x=%lu A=%ld B=%ld\n",qx[qi],A,B); qi++; }
        while(x>nextck){ printf("CK x=%lu A=%ld B=%ld\n",nextck,A,B); nextck+=10000000000ULL; }
        A++;
        if(A>B){ neg++; if(A-B>maxlead){maxlead=A-B;maxx=x;} if(printed<20){printf("NEG n=%ld q_n=%lu B=%ld\n",A,x,B);printed++;} }
        else if(A==B && lastp==x-2){ zero++; if(printed<20){printf("ZERO n=%ld q_n=%lu p_n=%lu\n",A,x,lastp);printed++;} }
        lastp=x; }
      if(s5[j]){ uint64_t x=6*k+5;
        while(qi<nq && qx[qi]<x){ printf("Q x=%lu A=%ld B=%ld\n",qx[qi],A,B); qi++; }
        while(x>nextck){ printf("CK x=%lu A=%ld B=%ld\n",nextck,A,B); nextck+=10000000000ULL; }
        B++; lastp=x; }
    }
    fflush(stdout);
  }
  printf("END k1=%lu (x<%lu) A=%ld B=%ld lastp=%lu neg=%ld zero=%ld maxlead=%ld at %lu\n",k1,6*k1+1,A,B,lastp,neg,zero,maxlead,maxx);
}
