// Verifies Theorem 4: BFS restricted to altitude >= 0 (no crash) gives the same T(i,j)
// as the unrestricted game whenever a soft landing is possible (j>=0, and j>=t_{|i|-1} if i<0).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define VM 260
#define HM 60000
static short d0[2*VM+1][2*HM+1], d1[2*VM+1][2*HM+1];
static void bfs(short d[2*VM+1][2*HM+1], int nocrash){
  memset(d,-1,sizeof(short)*(2*VM+1)*(2*HM+1));
  int *Q=malloc(sizeof(int)*2*(long)(2*VM+1)*(2*HM+1)); long h=0,t=0;
  d[VM][HM]=0; Q[t++]=0; Q[t++]=0;
  while(h<t){int v=Q[h++],x=Q[h++]; int dd=d[v+VM][x+HM];
    for(int a=-1;a<=1;a++){int pv=v-a, px=x-v; if(pv<-VM||pv>VM||px<-HM||px>HM)continue; if(nocrash&&px<0)continue;
      if(d[pv+VM][px+HM]<0){d[pv+VM][px+HM]=dd+1;Q[t++]=pv;Q[t++]=px;}}}
  free(Q);}
int main(){ bfs(d0,0); bfs(d1,1); long checked=0,bad=0,imposs_ok=0;
  for(int i=-60;i<=60;i++)for(int j=0;j<=1500;j++){ int ai=i<0?-i:i; long t=(long)ai*(ai-1)/2;
    int soft = (i>=0) || (j>=t);
    if(soft){checked++; if(d1[i+VM][j+HM]!=d0[i+VM][j+HM]){bad++; if(bad<5)printf("diff %d %d: %d vs %d\n",i,j,d0[i+VM][j+HM],d1[i+VM][j+HM]);}}
    else { if(d1[i+VM][j+HM]<0) imposs_ok++; else printf("unexpected soft landing %d %d\n",i,j);} }
  printf("soft-landable starts checked=%ld mismatches=%ld; impossible starts confirmed=%ld\n",checked,bad,imposs_ok); return 0;}
