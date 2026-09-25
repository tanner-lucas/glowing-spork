#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  int *a=malloc((N+1)*sizeof(int));
  a[1]=a[2]=a[3]=1;
  for(long n=4;n<=N;n++){ long x=a[n-1],y=a[n-2],z=a[n-3]; a[n]=n-a[x]-a[y]-a[z]; if(a[n]<1||a[n]>n){printf("out of range at %ld\n",n);return 0;} }
  // fixed point of 0->1, 1->1000 via self-reading, starting with 1
  char *w=malloc(N+8); long out=0, rd=0;
  w[0]=1;
  while(out<N){ if(w[rd]){ const char im[4]={1,0,0,0}; for(int j=0;j<4&&out<N;j++) w[out++]=im[j]; } else { w[out++]=1; } rd++; }
  long s=0, bad=0;
  for(long n=1;n<=N;n++){ s+=w[n-1]; if(s!=a[n]){ if(bad<5) printf("mismatch at n=%ld: a(n)=%d partial sum=%ld\n",n,a[n],s); bad++; } }
  printf("N=%ld mismatches=%ld\n",N,bad);
  for(int i=1;i<=31;i++) printf("%d,",a[i]); printf("\n");
  return 0;
}
