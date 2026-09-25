// Independent brute-force: generate tau(sigma^K(start)) sequentially (recursive expansion),
// compute D(n) = n*r - a(n) in __float128 and report the first n with D(n) outside (lo,hi).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <quadmath.h>
static char *sig[2], *tau[2]; static int slen[2], tlen[2];
static long long pos=0, cnt=0, maxpos; static int c; static __float128 r, lo, hi;
static int done=0; static long long firstn=0;
static void emit_tau(int a){
  for(int i=0;i<tlen[a];i++){
    pos++;
    if(tau[a][i]-'0'==c){ cnt++; __float128 D=(__float128)cnt*r-(__float128)pos;
      if(!(D>lo && D<hi)){ char b1[64]; quadmath_snprintf(b1,64,"%.30Qf",D); printf("FIRST VIOLATION n=%lld a(n)=%lld D=%s\n",cnt,pos,b1); done=1; return; } }
    if(pos>=maxpos){ done=1; return; }
  }
}
static void gen(int a,int k){ if(done) return; if(k==0){ emit_tau(a); return; } for(int i=0;i<slen[a]&&!done;i++) gen(sig[a][i]-'0',k-1); }
int main(int argc,char**argv){
  sig[0]=argv[1]; sig[1]=argv[2]; tau[0]=argv[3]; tau[1]=argv[4];
  for(int a=0;a<2;a++){ slen[a]=strlen(sig[a]); tlen[a]=strlen(tau[a]); }
  int start=atoi(argv[5]); int K=atoi(argv[6]); c=atoi(argv[7]);
  r=strtoflt128(argv[8],NULL); lo=strtoflt128(argv[9],NULL); hi=strtoflt128(argv[10],NULL); maxpos=atoll(argv[11]);
  gen(start,K);
  if(!firstn && !(done && pos<maxpos)) printf("no violation up to position %lld (n=%lld)\n",pos,cnt);
  return 0;
}
