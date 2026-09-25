/* Generate a fixed point of a binary morphism (or of its square) and report
   extremes of n*r - pos0(n) and n*s - pos1(n) (pos = 1-indexed position of n-th 0 / 1).
   usage: morph img0 img1 startletter power L r s [nprint]  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static char *img[2]; static int len[2];
int main(int argc,char**argv){
  img[0]=argv[1]; img[1]=argv[2]; len[0]=strlen(img[0]); len[1]=strlen(img[1]);
  int start=atoi(argv[3]); int power=atoi(argv[4]); long L=atol(argv[5]);
  long double r=strtold(argv[6],NULL), s=strtold(argv[7],NULL); int np=argc>8?atoi(argv[8]):0;
  char *w=malloc(L+64), *t=malloc(L+64); long wl=1; w[0]=start;
  for(int it=0;it<200 && wl<L;it++){
    for(int p=0;p<power;p++){ long tl=0; for(long i=0;i<wl && tl<L;i++){int c=w[i]; for(int j=0;j<len[c]&&tl<L;j++) t[tl++]=img[c][j]-'0';} char*x=w;w=t;t=x; wl=tl; }
  }
  /* sanity: w must be a fixed point prefix: check that applying power again reproduces prefix */
  if(np){ printf("word: "); for(int i=0;i<np&&i<wl;i++) printf("%d",w[i]); printf("\npos0: "); long c=0; for(long i=0;i<wl&&c<np;i++) if(w[i]==0){printf("%ld,",i+1);c++;} printf("\npos1: "); c=0; for(long i=0;i<wl&&c<np;i++) if(w[i]==1){printf("%ld,",i+1);c++;} printf("\n"); }
  long n0=0,n1=0; long double mn0=1e30,mx0=-1e30,mn1=1e30,mx1=-1e30; long amn0=0,amx0=0,amn1=0,amx1=0;
  for(long i=0;i<wl;i++){ long pos=i+1;
    if(w[i]==0){ n0++; long double d=n0*r-pos; if(d<mn0){mn0=d;amn0=n0;} if(d>mx0){mx0=d;amx0=n0;} }
    else { n1++; long double d=n1*s-pos; if(d<mn1){mn1=d;amn1=n1;} if(d>mx1){mx1=d;amx1=n1;} } }
  printf("L=%ld  #0=%ld #1=%ld\n",wl,n0,n1);
  printf("n*r-pos0(n): min %.12Lf at n=%ld ; max %.12Lf at n=%ld\n",mn0,amn0,mx0,amx0);
  printf("n*s-pos1(n): min %.12Lf at n=%ld ; max %.12Lf at n=%ld\n",mn1,amn1,mx1,amx1);
  return 0;
}
