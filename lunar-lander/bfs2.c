// BFS for Integer Lunar Lander on a big box: state (v,h). Move: v'=v+a (a in -1,0,1), h'=h+v'.
// Reverse BFS from (0,0): predecessor of (v',h') is (v'-a, h'-v').
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define VM 260
#define HM 60000
#define NV (2*VM+1)
#define NH (2*HM+1)
static short d[NV][NH];
static int q[NV*(long)NH/4];
int main(){
  memset(d,-1,sizeof d);
  long head=0,tail=0; int *Q=malloc(sizeof(int)*2*(long)NV*NH);
  d[VM][HM]=0; Q[tail++]=VM; Q[tail++]=HM;
  while(head<tail){int v=Q[head++]-VM,h=Q[head++]-HM; int dd=d[v+VM][h+HM];
    for(int a=-1;a<=1;a++){int pv=v-a, ph=h-v; if(pv<-VM||pv>VM||ph<-HM||ph>HM)continue;
      if(d[pv+VM][ph+HM]<0){d[pv+VM][ph+HM]=dd+1;Q[tail++]=pv+VM;Q[tail++]=ph+HM;}}}
  // output T(i,j) for |i|<=60, |j|<=1500
  FILE*f=fopen("bfs2.txt","w");
  for(int i=-60;i<=60;i++)for(int j=-1500;j<=1500;j++)fprintf(f,"%d %d %d\n",i,j,d[i+VM][j+HM]);
  fclose(f); return 0;}
