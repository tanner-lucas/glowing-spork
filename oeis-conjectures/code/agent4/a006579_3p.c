// squarefree n = p*q*r (p<q<r odd primes) with Pillai(n) = prod(2p_i-1) == -1 mod n
// necessary: r | 2pq-p-q. Enumerate p<q<=Q, factor N=2pq-p-q with spf sieve, test r>q prime factors.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long ull; typedef unsigned __int128 u128;
int main(int argc,char**argv){
  ull Q=strtoull(argv[1],0,10); ull L=2*Q*Q;
  uint32_t *spf=calloc(L+1,4); for(ull i=2;i<=L;i++) if(!spf[i]) for(ull j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i;
  long found=0, checked=0;
  for(ull p=3;p<=Q;p+=2){ if(spf[p]!=p) continue;
    for(ull q=p+2;q<=Q;q+=2){ if(spf[q]!=q) continue;
      ull N=2*p*q-p-q; ull m=N;
      while(m>1){ ull r=spf[m]; while(m%r==0) m/=r;
        if(r>q){ checked++; ull n=p*q*r; u128 P=(u128)(2*p-1)*(2*q-1)%n; P=P*(2*r-1)%n;
          if((ull)P==n-1){ found++; printf("FOUND n=%llu = %llu*%llu*%llu\n",n,p,q,r);} } } } }
  printf("Q=%llu candidates checked=%ld found=%ld\n",Q,checked,found);
}
