/* Stream fixed point of 0->1, 1->101010 (starting 1); a(n) = position of n-th 0.
   Exact test of  -2 < n*r - a(n) < 2  with r=(9+sqrt(21))/6, i.e. compare 6a(n)+12-9n vs n*sqrt(21) etc. */
#include <stdio.h>
#include <stdlib.h>
typedef __int128 i128;
static const char *img[2]={"1","101010"}; static int len[2]={1,6};
static long pos=0,n0=0, L; static int done=0; static long nviol=0;
/* returns 1 if n*sqrt(21) >= R (exact) */
static int ge_sqrt(long n, i128 R){ if(R<=0) return 1; return (i128)21*n*n >= R*R; }
static int le_sqrt(long n, i128 R){ if(R<0) return 0; return (i128)21*n*n <= R*R; }
static inline void emit(int c){ pos++; if(pos>=L) done=1; if(c) return; n0++; long a=pos;
  /* upper violation: n*r - a >= 2  <=> n*sqrt21 >= 6a+12-9n */
  i128 Ru=(i128)6*a+12-(i128)9*n0;
  if(ge_sqrt(n0,Ru)){ nviol++; if(nviol<=10) printf("UPPER violation: n=%ld a(n)=%ld\n",n0,a); }
  /* lower violation: n*r - a <= -2 <=> n*sqrt21 <= 6a-12-9n */
  i128 Rl=(i128)6*a-12-(i128)9*n0;
  if(le_sqrt(n0,Rl)){ nviol++; if(nviol<=10) printf("LOWER violation: n=%ld a(n)=%ld\n",n0,a); }
}
static void expand(int c,int depth){ if(done) return; if(depth==0){emit(c);return;} for(int j=0;j<len[c]&&!done;j++) expand(img[c][j]-'0',depth-1); }
int main(int argc,char**argv){ L=atol(argv[1]); int D=atoi(argv[2]); expand(1,D); printf("scanned L=%ld positions, n0=%ld zeros, violations=%ld\n",pos,n0,nviol); }
