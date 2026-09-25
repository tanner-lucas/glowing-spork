#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); long M=N+200000;
  char *comp=calloc(2*M+10,1); for(long i=2;i*i<=2*M+5;i++) if(!comp[i]) for(long j=i*i;j<=2*M+5;j+=i) comp[j]=1;
  char *used=calloc(M+2,1), *usum=calloc(2*M+10,1);
  // next-unused linked list via "skip" pointers

  long a=1; used[1]=1; long head=2; // smallest unused candidate >=2
  long bad=0, maxdev_lo=0, maxdev_hi=0;
  printf("1");
  for(long n=2;n<=N;n++){
    // iterate unused numbers from head
    long prev=-1, m=head, found=-1;
    while(m<=M){
      if(!used[m]){
        long s=a+m;
        if(comp[s] && !usum[s]){ found=m; break; }
      }
      m++;
      if(m-head>100000){printf("\nsearch too long at n=%ld\n",n);return 0;}
    }
    if(found<0){printf("\nnot found n=%ld\n",n);return 0;}
    used[found]=1; usum[a+found]=1; a=found;
    while(used[head]) head++;
    if(n<=30) printf(",%ld",a);
    if(n>6 && (a < n-2 || a > n+1)){ if(bad<10) printf("\nVIOLATION n=%ld a(n)=%ld",n,a); bad++; }
  }
  printf("\nN=%ld violations=%ld\n",N,bad);
  return 0;
}
