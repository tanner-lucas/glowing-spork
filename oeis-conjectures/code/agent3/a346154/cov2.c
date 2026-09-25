// A346154 covering search (fast early-exit): n%3!=1, every k in [2,K] has n^k+n+1 divisible by a prime < QMAX, or k==2 mod 3 (k>2) (algebraic factor n^2+n+1)
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
  long N0=atol(argv[1]), N1=atol(argv[2]); int K=atoi(argv[3]); int QMAX=atoi(argv[4]);
  int primes[5000],np=0; for(int p=2;p<QMAX;p++){int ok=1;for(int d=2;d*d<=p;d++)if(p%d==0){ok=0;break;} if(ok)primes[np++]=p;}
  long t[5000], c[5000], nm[5000];
  long cnt=0;
  for(long n=N0;n<=N1;n++){
    if(n%3==1) continue;
    for(int i=0;i<np;i++){ long q=primes[i]; nm[i]=n%q; c[i]=(nm[i]+1)%q; t[i]=nm[i]*nm[i]%q; }
    int k; 
    for(k=2;k<=K;k++){
      int covered = (k%3==2 && k>2);
      if(!covered) for(int i=0;i<np;i++) if((t[i]+c[i])%primes[i]==0){covered=1;break;}
      if(!covered) break;
      for(int i=0;i<np;i++) t[i]=t[i]*nm[i]%primes[i];
    }
    if(k>K){ printf("candidate n=%ld\n",n); fflush(stdout); cnt++; }
  }
  fprintf(stderr,"done %ld..%ld candidates %ld\n",N0,N1,cnt);
}
