// brute-force running min/max of D(n)=n*r-a(n) over positions <= maxpos (quad precision)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <quadmath.h>
static char *sig[2], *tau[2]; static int slen[2], tlen[2];
static long long pos=0, cnt=0, maxpos; static int c; static __float128 r, mn, mx; static long long nmn, nmx; static int done=0;
static void emit_tau(int a){
  for(int i=0;i<tlen[a];i++){
    pos++;
    if(tau[a][i]-'0'==c){ cnt++; __float128 D=(__float128)cnt*r-(__float128)pos;
      if(cnt==1||D<mn){mn=D;nmn=cnt;} if(cnt==1||D>mx){mx=D;nmx=cnt;} }
    if(pos>=maxpos){ done=1; return; }
  }
}
static void gen(int a,int k){ if(done) return; if(k==0){ emit_tau(a); return; } for(int i=0;i<slen[a]&&!done;i++) gen(sig[a][i]-'0',k-1); }
int main(int argc,char**argv){
  sig[0]=argv[1]; sig[1]=argv[2]; tau[0]=argv[3]; tau[1]=argv[4];
  for(int a=0;a<2;a++){ slen[a]=strlen(sig[a]); tlen[a]=strlen(tau[a]); }
  int start=atoi(argv[5]); int K=atoi(argv[6]); c=atoi(argv[7]);
  r=strtoflt128(argv[8],NULL); maxpos=atoll(argv[9]);
  gen(start,K);
  char b1[64],b2[64]; quadmath_snprintf(b1,64,"%.25Qf",mn); quadmath_snprintf(b2,64,"%.25Qf",mx);
  printf("%lld %lld %s %lld %s %lld\n",pos,cnt,b1,nmn,b2,nmx);
  return 0;
}
