#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(){ int L=28; uint32_t N=1u<<L; uint32_t *a=malloc(sizeof(uint32_t)*(N+1)); a[1]=1;a[2]=1;
 for(uint32_t n=3;n<=N;n++){ uint32_t p=a[n-1]; a[n]=a[p]+a[n-p]; }
 // A072100 via array: m(i,1)=m(1,j)=1, m(i,j)=m(i-1,j-1)+m(i-1,j+1); a(n)=m(n,2)
 static long long m[64][80]; for(int i=1;i<64;i++) for(int j=1;j<80;j++){ if(i==1||j==1) m[i][j]=1; else m[i][j]=m[i-1][j-1]+m[i-1][j+1]; }
 for(int e=0;e<L;e++){ long long mx=-1; for(uint32_t k=1u<<e;k<=(1u<<(e+1));k++){ long long v=2LL*a[k]-k; if(v>mx) mx=v; } printf("n=%d max=%lld A072100(n)=%lld\n",e,mx,m[e>0?e:1][2]); }
}
