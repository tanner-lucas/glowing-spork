#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  int *a=malloc((N+2)*sizeof(int));
  for(int p=3;p<=12;p++){
    long double r=(sqrtl((long double)p*(p+4))-p)/2;
    a[1]=1; long bad=0, first=0;
    for(long n=2;n<=N;n++) a[n]=n - a[a[n-1]]/p;
    for(long n=1;n<=N;n++){ long f=(long)floorl(r*(n+1)); if(f!=a[n]){ if(!bad) first=n; bad++; } }
    printf("p=%d r=%.12Lf mismatches=%ld first=%ld\n",p,r,bad,first);
  }
}
