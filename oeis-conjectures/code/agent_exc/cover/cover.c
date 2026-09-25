// Covering-congruence search for A232210 (append 3's) and A242775 (prepend 3's).
// mode 0 (A232210): 3*N_k = c*10^k - 1, c = 3p+1.  q | N_k  <=> c*10^k == 1 (mod q).
// mode 1 (A242775): 3*N_k = 10^(k+d) + e, e = 3p - 10^d. q | N_k <=> 10^(k+d) == -e (mod q).
// Period M (bitset). Algebraic factorizations optionally mark residues.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define MAXQ 400
typedef unsigned __int128 u128;
int nq; uint64_t Q[MAXQ]; int LQ[MAXQ]; uint64_t PW[MAXQ][80];
int M; int W;
uint64_t *pat; // pattern[qi][j] -> W words : residues k ≡ j (mod L) in [0,M)
static int issq(uint64_t x, uint64_t *r){ uint64_t s=(uint64_t)sqrtl((long double)x); while(s*s>x) s--; while((s+1)*(s+1)<=x) s++; *r=s; return s*s==x; }
static int iscube(uint64_t x){ uint64_t s=(uint64_t)cbrtl((long double)x); while(s*s*s>x) s--; while((s+1)*(s+1)*(s+1)<=x) s++; return s*s*s==x; }
int main(int argc,char**argv){
  int mode=atoi(argv[1]); uint64_t pmin=strtoull(argv[2],0,10), pmax=strtoull(argv[3],0,10); M=atoi(argv[4]);
  int useAlg = argc>5 ? atoi(argv[5]) : 1;
  W=(M+63)/64;
  FILE*f=fopen("ords.txt","r"); int L; uint64_t q; nq=0;
  while(fscanf(f,"%d %lu",&L,&q)==2){ if(M%L) continue; if(q> (1ULL<<62)) continue; Q[nq]=q; LQ[nq]=L; uint64_t v=1; for(int j=0;j<L;j++){PW[nq][j]=v; v=(uint64_t)((u128)v*10%q);} nq++; }
  fclose(f);
  pat=calloc((size_t)nq*80*W,8);
  for(int i=0;i<nq;i++) for(int j=0;j<LQ[i];j++){ uint64_t*P=pat+((size_t)i*80+j)*W; for(int k=j;k<M;k+=LQ[i]) P[k>>6]|=1ULL<<(k&63); }
  uint64_t full[W]; memset(full,0,sizeof full); for(int k=0;k<M;k++) full[k>>6]|=1ULL<<(k&63);
  // sieve primes up to pmax
  char*comp=calloc(pmax+1,1); for(uint64_t i=2;i*i<=pmax;i++) if(!comp[i]) for(uint64_t j=i*i;j<=pmax;j+=i) comp[j]=1;
  long found=0;
  for(uint64_t p=pmin;p<=pmax;p++){ if(comp[p]||p<2) continue;
    uint64_t cov[W]; memset(cov,0,sizeof cov);
    int d=0; uint64_t t=p, pd=1; while(t){d++; t/=10; pd*=10;}
    __int128 e = (__int128)3*p - (__int128)pd; // mode1
    uint64_t c = 3*p+1;
    for(int i=0;i<nq;i++){ uint64_t qq=Q[i]; uint64_t r;
      if(mode==0) r = c%qq; else { __int128 me=-e; __int128 rr= me%(__int128)qq; if(rr<0) rr+=qq; r=(uint64_t)rr; }
      if(mode==0){ // c == 10^{-k}: find j with PW[j]==r  => k == -j mod L
        for(int j=0;j<LQ[i];j++) if(PW[i][j]==r){ int k=(LQ[i]-j)%LQ[i]; uint64_t*P=pat+((size_t)i*80+k)*W; for(int w=0;w<W;w++) cov[w]|=P[w]; break; }
      } else { // 10^(k+d) == r: find j with PW[j]==r => k == j-d mod L
        for(int j=0;j<LQ[i];j++) if(PW[i][j]==r){ int k=((j-d)%LQ[i]+LQ[i])%LQ[i]; uint64_t*P=pat+((size_t)i*80+k)*W; for(int w=0;w<W;w++) cov[w]|=P[w]; break; }
      }
    }
    char alg[64]=""; 
    if(useAlg){
      uint64_t r;
      if(mode==0){
        if(issq(c,&r) && M%2==0){ for(int k=0;k<M;k+=2) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"c=sq ");}
        if(c%10==0 && issq(c/10,&r) && M%2==0){ for(int k=1;k<M;k+=2) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"c=10sq ");}
        if(M%3==0){ if(iscube(c)){for(int k=0;k<M;k+=3) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"c=cube ");}
          if(c%10==0&&iscube(c/10)){for(int k=2;k<M;k+=3) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"c=10cube ");}
          if(c%100==0&&iscube(c/100)){for(int k=1;k<M;k+=3) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"c=100cube ");} }
      } else {
        // 10^(k+d) + e.  e=-m^2: k+d even.  e=-10m^2: k+d odd. e=+-m^3 etc: k+d==0 mod3 ; e=+-10m^3: k+d==2 mod 3; e=+-100m^3: k+d==1 mod 3
        __int128 ae = e<0? -e: e;
        if(e<0 && M%2==0){ if(issq((uint64_t)ae,&r)){ for(int k=0;k<M;k++) if((k+d)%2==0) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"e=-sq ");}
                   if((uint64_t)ae%10==0 && issq((uint64_t)ae/10,&r)){ for(int k=0;k<M;k++) if((k+d)%2==1) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"e=-10sq ");} }
        if(M%3==0 && ae>0){ uint64_t a=(uint64_t)ae;
          if(iscube(a)){ for(int k=0;k<M;k++) if((k+d)%3==0) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"e=cube ");}
          if(a%10==0&&iscube(a/10)){ for(int k=0;k<M;k++) if((k+d)%3==2) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"e=10cube ");}
          if(a%100==0&&iscube(a/100)){ for(int k=0;k<M;k++) if((k+d)%3==1) cov[k>>6]|=1ULL<<(k&63); strcat(alg,"e=100cube ");} }
      }
    }
    int ok=1; for(int w=0;w<W;w++) if(cov[w]!=full[w]) {ok=0;break;}
    if(ok){ found++; printf("p=%lu M=%d %s\n",p,M,alg); fflush(stdout); if(found>=50) break; }
  }
  fprintf(stderr,"done found=%ld nq=%d\n",found,nq);
}
