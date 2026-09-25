// Discrepancy tester for positions of letters in sigma^k(start), sigma on {0,1}.
// usage: disc img0 img1 start k maxlen r0 lo0 hi0 r1 lo1 hi1 [printN]
// Tracks D_c(n) = n*r_c - pos_c(n) where pos_c(n) = position (1-based) of n-th letter c.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static char *img[2]; static int ilen[2];
static long long pos=0, cnt[2]={0,0}, maxlen;
static long double r[2], lo[2], hi[2], mn[2], mx[2]; static long long argmn[2], argmx[2], firstviol[2]={0,0};
static int printN=0; static int stop=0;
static void emit(int c){
  pos++; cnt[c]++;
  long long n=cnt[c];
  long double D = (long double)n*r[c] - (long double)pos;
  if(n==1||D<mn[c]){mn[c]=D;argmn[c]=n;}
  if(n==1||D>mx[c]){mx[c]=D;argmx[c]=n;}
  if(!firstviol[c] && !(D>lo[c] && D<hi[c])) { firstviol[c]=n; printf("letter %d: first violation n=%lld pos=%lld D=%.12Lf\n",c,n,pos,D); }
  if(printN && pos<=printN) printf("%d%s", c, pos==printN?"\n":",");
  if(pos>=maxlen) stop=1;
}
static void gen(int c, int k){
  if(stop) return;
  if(k==0){ emit(c); return; }
  for(int i=0;i<ilen[c] && !stop;i++) gen(img[c][i]-'0', k-1);
}
int main(int argc,char**argv){
  img[0]=argv[1]; img[1]=argv[2]; ilen[0]=strlen(img[0]); ilen[1]=strlen(img[1]);
  int start=atoi(argv[3]); int k=atoi(argv[4]); maxlen=atoll(argv[5]);
  r[0]=strtold(argv[6],0); lo[0]=strtold(argv[7],0); hi[0]=strtold(argv[8],0);
  r[1]=strtold(argv[9],0); lo[1]=strtold(argv[10],0); hi[1]=strtold(argv[11],0);
  if(argc>12) printN=atoi(argv[12]);
  gen(start,k);
  printf("length generated %lld  (#0=%lld #1=%lld)\n", pos, cnt[0], cnt[1]);
  for(int c=0;c<2;c++) printf("letter %d: min D=%.9Lf at n=%lld ; max D=%.9Lf at n=%lld ; bounds (%Lg,%Lg) %s\n", c, mn[c], argmn[c], mx[c], argmx[c], lo[c], hi[c], firstviol[c]?"VIOLATED":"ok");
  return 0;
}
