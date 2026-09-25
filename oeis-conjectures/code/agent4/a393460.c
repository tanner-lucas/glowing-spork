#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  char *comp=calloc(N+1,1); comp[0]=comp[1]=1; for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  char *R=calloc(N+1,1);
  for(long q=2;q<=N;q++) if(!comp[q] && q%10!=0){ long r=0,t=q; while(t){ r=r*10+t%10; t/=10;} if(r<=N) R[r]=1; }
  long *pr=malloc(sizeof(long)*(N/5+1000)); long np=0; for(long i=2;i<=N;i++) if(!comp[i]) pr[np++]=i;
  long missing=0; long maxsteps=0, argmax=0;
  for(long n=4;n<=N;n++){ long i; int ok=0;
    for(i=0;i<np && pr[i]<n;i++){ if(R[n-pr[i]]){ok=1;break;} }
    if(!ok){ missing++; if(missing<20) printf("no representation: n=%ld\n",n); }
    if(i>maxsteps){maxsteps=i;argmax=n;}
  }
  printf("N=%ld missing=%ld max prime index needed=%ld at n=%ld\n",N,missing,maxsteps,argmax);
}
