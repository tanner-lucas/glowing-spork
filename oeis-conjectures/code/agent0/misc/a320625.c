#include <stdio.h>
#include <stdint.h>
typedef int64_t i64; typedef uint64_t u64;
static i64 inv(i64 a,i64 m){ i64 g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; i64 b=a1; // ext euclid
  i64 r0=m,r1=b,s0=0,s1=1; while(r1){ i64 q=r0/r1,t; t=r0-q*r1;r0=r1;r1=t; t=s0-q*s1;s0=s1;s1=t;} if(s0<0)s0+=m; return s0; }
int main(){
  for(int n=1;n<=18;n++){
    u64 mod=1; for(int i=0;i<n+1;i++) mod*=3;
    u64 M=(mod/3-1)/2; // (3^n-1)/2
    // C(2k,k)=3^e*u
    int e=0; u64 u=1; u64 S=1; // k=0 term 1
    for(u64 k=1;k<=M;k++){
      u64 f[3]={2*k,2*k-1,k}; int ev[3]; u64 uv[3];
      for(int j=0;j<3;j++){ u64 t=f[j]; int v=0; while(t%3==0){t/=3;v++;} ev[j]=v; uv[j]=t%mod; }
      e += ev[0]+ev[1]-2*ev[2];
      u = (u*uv[0])%mod; u=(u*uv[1])%mod;
      u64 ik=(u64)inv((i64)uv[2],(i64)mod); u=(u*ik)%mod; u=(u*ik)%mod;
      if(e<=n){ u64 p3=1; for(int i=0;i<e;i++) p3*=3; S=(S+(u*p3)%mod)%mod; }
    }
    if(S% (mod/3) !=0){ printf("n=%d: S not divisible by 3^n!? S=%llu\n",n,(unsigned long long)S); continue; }
    int r=(int)(S/(mod/3))%3;
    printf("n=%d a(n) mod 3 = %d  (conj: %d)\n",n,r,(n%2)?1:2); fflush(stdout);
  }
}
