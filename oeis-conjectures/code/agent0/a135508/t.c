#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
  long N=atol(argv[1]); // compute a(1..N)
  long M=N+10;
  int *spf=calloc(M+1,sizeof(int));
  for(long i=2;i<=M;i++) if(!spf[i]) for(long j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  int *e=calloc(M+1,sizeof(int)); // exponent of prime q in x(n)
  char *appeared=calloc(M+1,1);
  long *firstpos=calloc(M+1,sizeof(long));
  // x(1)=1. a(n)= m/gcd(x(n),m), m=n+1 ; x(n+1)=x(n)*(a(n)+2)
  long nonprime_nonone=0; long bad1=0, bad2=0;
  int data[]={2,3,1,1,1,7,2,1,1,11,1,1,7,1,1,17,1,1,1,7,11,23,1,1,1,1,7,29,1,1,2,11,17,7,1,37,1,1,1,41,7,1,11,1,23,47};
  for(long n=1;n<=N;n++){
    long m=n+1, t=m, a=1;
    while(t>1){ int q=spf[t]; int v=0; while(t%q==0){t/=q;v++;} int k=v-e[q]; if(k>0) for(int i=0;i<k;i++) a*=q; }
    if(n<=46 && a!=data[n-1]){printf("DATA MISMATCH n=%ld a=%ld\n",n,a);}
    if(a>1 && spf[a]!=a){ nonprime_nonone++; if(nonprime_nonone<10) printf("composite term a(%ld)=%ld\n",n,a);} 
    if(a>1 && !appeared[a]){appeared[a]=1; firstpos[a]=n;}
    long f=a+2; while(f>1){int q=spf[f]; f/=q; e[q]++;}
  }
  // check conjecture: for prime p <= N+1 with p-2 not prime, a(p-1)=p  (equiv: p appeared first at p-1)
  long cnt=0;
  for(long p=3;p<=N+1;p++){ if(spf[p]!=p) continue; int pm2prime = (p-2>=2 && spf[p-2]==p-2);
     if(!pm2prime){ if(!(appeared[p] && firstpos[p]==p-1)){ bad1++; if(bad1<10) printf("conj1 fails p=%ld\n",p);} }
     int inA025584 = !pm2prime; // p-2 not prime
     if(appeared[p] != (inA025584 || p==7)){ bad2++; if(bad2<10) printf("set mismatch p=%ld appeared=%d\n",p,appeared[p]); }
  }
  printf("N=%ld composite terms=%ld conj1 failures=%ld set-mismatches=%ld\n",N,nonprime_nonone,bad1,bad2);
}
