// segmented phi; check phi(2n)+phi(2n+2) <= phi(2n-1)+phi(2n+1) and < phi(2n+1)+phi(2n+3)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long ull;
int main(int argc,char**argv){
  ull X=strtoull(argv[1],0,10); ull S=1ULL<<22; ull R=(ull)sqrtl((long double)X)+10;
  char*c=calloc(R+1,1); ull *pr=malloc(sizeof(ull)*R); int np=0;
  for(ull i=2;i<=R;i++) if(!c[i]){ pr[np++]=i; for(ull j=i*i;j<=R;j+=i) c[j]=1; }
  ull *ph=malloc(8*(S+8)), *rem=malloc(8*(S+8));
  double bestr1=1e9, bestr2=1e9; ull arg1=0,arg2=0; long v1=0,v2=0;
  // keep previous tail values to handle windows across segments: we process values in [L, L+S) and need phi at 2n-1..2n+3
  // simpler: use overlapping segments of size S+4 starting at L with step S.
  for(ull L=1; L<=X; L+=S){
    ull len=S+4;
    for(ull i=0;i<len;i++){ ph[i]=L+i; rem[i]=L+i; }
    for(int t=0;t<np;t++){ ull p=pr[t]; if(p*p>L+len) break; ull st=((L+p-1)/p)*p; for(ull x=st;x<L+len;x+=p){ ull i=x-L; ph[i]-=ph[i]/p; do rem[i]/=p; while(rem[i]%p==0); } }
    for(ull i=0;i<len;i++){ if(rem[i]>1) ph[i]-=ph[i]/rem[i]; }
    if(L==1) ph[0]=1;
    // for each even m=2n in [L+1, L+S] with indices m-1..m+3 inside window
    for(ull m=L+1+((L+1)&1); m+3<L+len && m<L+1+S; m+=2){
      ull i=m-L; // ph index of m
      long long lhs=(long long)ph[i]+(long long)ph[i+2];
      long long r1=(long long)ph[i-1]+(long long)ph[i+1];
      long long r2=(long long)ph[i+1]+(long long)ph[i+3];
      if(lhs>r1){ v1++; if(v1<10) printf("VIOL1 2n=%llu lhs=%lld rhs=%lld\n",m,lhs,r1);} 
      if(lhs>=r2){ v2++; if(v2<10) printf("VIOL2 2n=%llu lhs=%lld rhs=%lld\n",m,lhs,r2);} 
      double q1=(double)r1/lhs, q2=(double)r2/lhs;
      if(m>100 && q1<bestr1){bestr1=q1;arg1=m;} if(m>100 && q2<bestr2){bestr2=q2;arg2=m;}
    }
  }
  printf("X=%llu viol1=%ld viol2=%ld min ratio rhs1/lhs=%.6f at 2n=%llu, rhs2/lhs=%.6f at 2n=%llu\n",X,v1,v2,bestr1,arg1,bestr2,arg2);
}
