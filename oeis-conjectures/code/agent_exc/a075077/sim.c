#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); long M=3*N+100;
  char *comp=calloc(2*M+10,1); for(long i=2;i*i<=2*M+9;i++) if(!comp[i]) for(long j=i*i;j<=2*M+9;j+=i) comp[j]=1;
  char *used=calloc(M+10,1), *usum=calloc(2*M+10,1);
  long a=1; used[1]=1; long low=2; long viol=0; long maxd=-99,mind=99; 
  int check[80]={1,3,5,4,2,8,6,9,7,11,10,12,13,14,16,17,15,19,20,18,22,23,21,25,24,26,28,27,29,31,32,30,34,35,33,37,38,36,40,41,39,43,42,44,46,45,47,48,50,49,51,53,52,54,56,55,57,58,59,60,61,62,63,65,64,66,67,68,70,71,69,73};
  int ok=1;
  for(long n=2;n<=N;n++){
    while(used[low]) low++;
    long m=low;
    for(;;m++){ if(m>M){printf("overflow\n");return 1;} if(used[m]) continue; long s=a+m; if(comp[s] && !usum[s]) break; }
    used[m]=1; usum[a+m]=1; a=m;
    if(n<=72 && a!=check[n-1]) ok=0;
    long d=a-n; if(n>6){ if(d<-2||d>1){ viol++; if(viol<20) printf("VIOL n=%ld a(n)=%ld\n",n,a);} }
    if(n>6){ if(d>maxd)maxd=d; if(d<mind)mind=d; }
  }
  printf("data match=%d N=%ld viol=%ld min(a(n)-n)=%ld max=%ld\n",ok,N,viol,mind,maxd);
}
