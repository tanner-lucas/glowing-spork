// Independent method: C(N,K) mod p^e via p-adic factorial decomposition
// N! = p^{v_p(N!)} * U(N),  U(N) = F(N) * U(floor(N/p)),  F(N) = prod_{k<=N, p !| k} k  (mod p^e)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
typedef uint64_t u64;
static u64 M;
static u64 mulm(u64 a, u64 b){ return (u64)((u128)a*b % M); }
static u64 powm(u64 a, u64 e){ u64 r=1%M; while(e){ if(e&1) r=mulm(r,a); a=mulm(a,a); e>>=1;} return r; }
static u64 p;
static u64 F(u64 N){ // product of k<=N coprime to p, mod M
  u64 r=1%M;
  for(u64 k=1;k<=N;k++){ if(k%p) r=mulm(r,k%M); }
  return r;
}
static u64 U(u64 N){ if(N==0) return 1%M; return mulm(F(N), U(N/p)); }
static u64 vp(u64 N){ u64 v=0; while(N){ N/=p; v+=N;} return v; }
// inverse mod M of unit via extended Euclid
static u64 invm(u64 a){ __int128 t=0,nt=1; __int128 r=M,nr=a; while(nr){ __int128 q=r/nr, tmp; tmp=t-q*nt; t=nt; nt=tmp; tmp=r-q*nr; r=nr; nr=tmp;} if(r!=1){fprintf(stderr,"not unit\n"); exit(1);} if(t<0) t+=M; return (u64)t; }
static u64 binom(u64 N, u64 K){
  u64 v = vp(N)-vp(K)-vp(N-K);
  u64 u = mulm(U(N), invm(mulm(U(K),U(N-K))));
  u64 pv = 1%M; for(u64 i=0;i<v;i++){ pv=mulm(pv,p); if(pv==0) break; }
  return mulm(pv,u);
}
int main(int argc, char **argv){
  p = strtoull(argv[1],0,10); int e = atoi(argv[2]);
  M=1; for(int i=0;i<e;i++) M*=p;
  u64 N = strtoull(argv[3],0,10), K = strtoull(argv[4],0,10);
  printf("C(%llu,%llu) mod %llu^%d = %llu\n",(unsigned long long)N,(unsigned long long)K,(unsigned long long)p,e,(unsigned long long)binom(N,K));
  return 0;
}
