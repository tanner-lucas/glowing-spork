// A346154: search n (n%3 != 1) such that n^k+n+1 has a small prime factor (or algebraic factor n^2+n+1 when k==2 mod 3, k>2) for all 2<=k<=K
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){
  long N0=atol(argv[1]), N1=atol(argv[2]); int K=atoi(argv[3]); int QMAX=atoi(argv[4]);
  int primes[5000],np=0; for(int p=2;p<QMAX;p++){int ok=1;for(int d=2;d*d<=p;d++)if(p%d==0){ok=0;break;} if(ok)primes[np++]=p;}
  char *cov=malloc(K+1);
  for(long n=N0;n<=N1;n++){
    if(n%3==1) continue;
    memset(cov,0,K+1);
    int need=0;
    for(int k=2;k<=K;k++){ if(k%3==2 && k>2) cov[k]=1; else need++; }
    for(int i=0;i<np && need>0;i++){
      long q=primes[i]; long nm=n%q; long c=(nm+1)%q; long t=(nm*nm)%q; // t = n^k mod q, start k=2
      for(int k=2;k<=K;k++){
        if(!cov[k] && (t+c)%q==0){ // q | n^k+n+1 ; ensure n^k+n+1 > q (true unless tiny n)
          cov[k]=1; need--; }
        t=(t*nm)%q;
      }
    }
    if(need==0) printf("candidate n=%ld\n",n);
  }
  return 0;
}
