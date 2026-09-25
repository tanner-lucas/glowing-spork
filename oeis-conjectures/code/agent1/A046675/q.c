// q(n) = number of partitions of n into distinct odd primes (long double); check q(n) >= q(n-2)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  int N = atoi(argv[1]);
  char *comp = calloc(N+1,1);
  for(int i=2;(long)i*i<=N;i++) if(!comp[i]) for(int j=i*i;j<=N;j+=i) comp[j]=1;
  long double *q = calloc(N+1,sizeof(long double));
  q[0]=1;
  for(int p=3;p<=N;p+=2) if(!comp[p]) for(int n=N;n>=p;n--) q[n]+=q[n-p];
  int cnt=0;
  for(int n=2;n<=N;n++){
    long double d = q[n]-q[n-2];
    if(d < 0 || fabsl(d) <= 1e-12L*q[n]) { if(cnt<40) printf("n=%d q(n)-q(n-2)=%Lg q(n)=%Lg%s\n", n, d, q[n], d<0?"  NEGATIVE":"  ~0"); cnt++; }
  }
  printf("N=%d, flagged=%d, q(N)=%Lg\n", N, cnt, q[N]);
  // print (-1)^n a(n) for n=0..40 to compare with data
  for(int n=0;n<=40;n++){ long double v = q[n] - (n>=2?q[n-2]:0); long double a = (n%2?-v:v); printf("%.0Lf,", a);} printf("\n");
  return 0;
}
