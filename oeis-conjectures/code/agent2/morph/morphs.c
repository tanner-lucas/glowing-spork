/* Streaming version: expands start letter under sigma (depth D) and tracks discrepancies.
   usage: morphs img0 img1 start power L "a,b,c,d" "a,b,c,d"   where r=(a+b*sqrt(c))/d
   Tracks D0(n)=n*r-pos0(n), D1(n)=n*s-pos1(n); prints min/max and the first n achieving them. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static char *img[2]; static int len[2];
static long L, pos=0, n0=0, n1=0; static long double r,s;
static long double mn0=1e30,mx0=-1e30,mn1=1e30,mx1=-1e30; static long amn0,amx0,amn1,amx1;
static int done=0; static long K=0; static long pp0[200],pp1[200];
static inline void emit(int c){ pos++; if(c==0){n0++; if(n0<=K) pp0[n0-1]=pos; long double d=n0*r-pos; if(d<mn0){mn0=d;amn0=n0;} if(d>mx0){mx0=d;amx0=n0;}}
  else {n1++; if(n1<=K) pp1[n1-1]=pos; long double d=n1*s-pos; if(d<mn1){mn1=d;amn1=n1;} if(d>mx1){mx1=d;amx1=n1;}} if(pos>=L) done=1; }
static void expand(int c,int depth){ if(done) return; if(depth==0){emit(c);return;} for(int j=0;j<len[c]&&!done;j++) expand(img[c][j]-'0',depth-1); }
static long double parse(char*s){ long double a,b,c,d; sscanf(s,"%Lf,%Lf,%Lf,%Lf",&a,&b,&c,&d); return (a+b*sqrtl(c))/d; }
int main(int argc,char**argv){
  img[0]=argv[1]; img[1]=argv[2]; len[0]=strlen(img[0]); len[1]=strlen(img[1]);
  int start=atoi(argv[3]); int power=atoi(argv[4]); L=atol(argv[5]); r=parse(argv[6]); s=parse(argv[7]); if(argc>8) K=atol(argv[8]);
  /* choose depth so that expansion length >= L: estimate by exact length recursion */
  long double l0=1,l1=1; int D=0; long double cur = 1;
  while(1){ /* length of sigma^D(start) */
    long double nl0=0,nl1=0; for(int j=0;j<len[0];j++) nl0+= img[0][j]=='0'?l0:l1; for(int j=0;j<len[1];j++) nl1+= img[1][j]=='0'?l0:l1;
    l0=nl0; l1=nl1; D++; cur = start==0?l0:l1; if(D%power==0 && cur>=L) break; if(D>2000) break; }
  expand(start,D);
  if(K){printf("pos0:");for(long i=0;i<K&&i<n0;i++)printf("%ld,",pp0[i]);printf("\npos1:");for(long i=0;i<K&&i<n1;i++)printf("%ld,",pp1[i]);printf("\n");}
  printf("depth=%d L=%ld #0=%ld #1=%ld r=%.15Lf s=%.15Lf\n",D,pos,n0,n1,r,s);
  printf("n*r-pos0(n): min %.10Lf at n=%ld ; max %.10Lf at n=%ld\n",mn0,amn0,mx0,amx0);
  printf("n*s-pos1(n): min %.10Lf at n=%ld ; max %.10Lf at n=%ld\n",mn1,amn1,mx1,amx1);
  return 0;
}
