#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// Grundy values of octal game .404: from n, remove 1 or 3 tokens and split remainder into two nonempty heaps
int main(int argc,char**argv){
  int N=atoi(argv[1]); unsigned short *G=calloc(N+1,2); int maxg=0; long long zeros=0;
  for(int n=0;n<=N;n++){
    uint64_t seen[16]={0};
    for(int r=1;r<=3;r+=2){ int m=n-r; if(m<2) continue;
      for(int a=1;a<=m/2;a++){ int v=G[a]^G[m-a]; seen[v>>6]|=1ULL<<(v&63);} }
    int g=0; while(seen[g>>6]>>(g&63)&1) g++;
    G[n]=g; if(g>maxg) maxg=g; if(g==0){ zeros++; if(n>286) printf("ZERO at %d\n",n);} 
  }
  printf("N=%d maxg=%d zeros=%lld\n",N,maxg,zeros);
  FILE*f=fopen("G.bin","wb"); fwrite(G,2,N+1,f); fclose(f);
  return 0;
}
