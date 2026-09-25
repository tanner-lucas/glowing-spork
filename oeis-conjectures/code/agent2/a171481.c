#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ long N=atol(argv[1]); int *a=malloc((N+1)*sizeof(int)); a[0]=0;a[1]=1;a[2]=1;
  long bad=0; double mx=0;
  for(long n=3;n<=N;n++){ long p=a[n-1]; long i=n-p-2; if(p<0||p>=n||i<0){printf("undefined at n=%ld\n",n);return 1;} a[n]=a[p]+a[i]; long d=a[n]-a[n-1]; if(d!=0&&d!=1){ if(bad<5) printf("diff %ld at n=%ld\n",d,n); bad++; } }
  printf("N=%ld bad=%ld a(N)=%d a(N)/N=%.8f e/10=%.8f\n",N,bad,a[N],(double)a[N]/N,2.718281828459045/10);
  for(int n=0;n<34;n++) printf("%d,",a[n]); printf("\n"); }
