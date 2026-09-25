// brute force a(n): least m>1 such that 1^2..n^2 pairwise incongruent mod 2^m-1
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static unsigned char *seen; 
int ok(long n, int m){
  unsigned long long M=(1ULL<<m)-1;
  // use hash set of residues via sorting
  unsigned long long *r=malloc(n*sizeof(*r));
  for(long k=1;k<=n;k++) r[k-1]=((unsigned __int128)k*k)%M;
  int cmp(const void*a,const void*b){unsigned long long x=*(unsigned long long*)a,y=*(unsigned long long*)b;return x<y?-1:x>y;}
  qsort(r,n,sizeof(*r),cmp);
  int good=1; for(long k=1;k<n;k++) if(r[k]==r[k-1]){good=0;break;}
  free(r); return good;
}
int main(int argc,char**argv){
  long N=atol(argv[1]); int m=2;
  for(long n=1;n<=N;n++){ while(!ok(n,m)) m++; printf("%ld %d\n",n,m);} }
