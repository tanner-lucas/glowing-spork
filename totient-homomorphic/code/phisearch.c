// Search for k in [K0,K1) with phi(j+k) == phi(j) + phi(k) for j in a given list (A066426 / A110172).
// Segmented totient sieve using only multiplications; cofactor via exact double division (n < 2^53).
// usage: phisearch K0 K1 jfile outfile
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define S (1<<17)
#define JM 2048
typedef uint64_t u64;
static u64 phi[S+JM], prod[S+JM];
int main(int argc,char**argv){
  u64 K0=strtoull(argv[1],0,10), K1=strtoull(argv[2],0,10);
  FILE*jf=fopen(argv[3],"r"); int J[4096],nj=0; while(fscanf(jf,"%d",&J[nj])==1)nj++; fclose(jf);
  FILE*out=fopen(argv[4],"a");
  u64 hi=K1+JM; u64 r=(u64)sqrt((double)hi)+2;
  // primes up to r
  char*isc=calloc(r+1,1); u64*P=malloc(sizeof(u64)*(r/2+10)); int np=0;
  for(u64 i=2;i<=r;i++){ if(!isc[i]){P[np++]=i; for(u64 m=i*i;m<=r;m+=i)isc[m]=1;} }
  // phi(j) for j list (small, direct)
  u64 cj[4096]; for(int t=0;t<nj;t++){u64 n=J[t],res=n; for(u64 p=2;p*p<=n;p++) if(n%p==0){while(n%p==0)n/=p; res-=res/p;} if(n>1)res-=res/n; cj[t]=res;}
  u64 hits=0;
  for(u64 L=K0; L<K1; L+=S){
    u64 len=S+JM; // cover [L, L+len)
    for(u64 i=0;i<len;i++){phi[i]=1;prod[i]=1;}
    u64 top=L+len;
    for(int t=0;t<np;t++){ u64 p=P[t]; if(p*p>top)break;
      u64 st=((L+p-1)/p)*p;
      for(u64 m=st;m<top;m+=p){phi[m-L]*=(p-1);prod[m-L]*=p;}
      u64 pe=p*p;
      while(pe<top){ u64 st2=((L+pe-1)/pe)*pe; for(u64 m=st2;m<top;m+=pe){phi[m-L]*=p;prod[m-L]*=p;} if(pe>top/p)break; pe*=p; }
    }
    for(u64 i=0;i<len;i++){ u64 n=L+i; if(prod[i]!=n){ u64 q=(u64)((double)n/(double)prod[i]+0.5); phi[i]*=(q-1);} }
    if(L==0){phi[0]=0;} // k=0 not allowed
    u64 kmax = (K1-L<S)?(K1-L):S;
    for(int t=0;t<nj;t++){ u64 c=cj[t]; const u64*a=phi,*b=phi+J[t]; int any=0;
      for(u64 i=0;i<kmax;i++) any|=(b[i]==a[i]+c);
      if(any){ for(u64 i=0;i<kmax;i++) if(b[i]==a[i]+c && L+i>=1){ fprintf(out,"%d %llu\n",J[t],(unsigned long long)(L+i)); hits++; } }
    }
    if(((L/S)&1023)==0){fprintf(stderr,"L=%llu hits=%llu\n",(unsigned long long)L,(unsigned long long)hits); fflush(out);}
  }
  fclose(out); return 0;}
