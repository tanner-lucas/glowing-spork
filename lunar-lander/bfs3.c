// reverse BFS from (0,0,0) over box |a|<=A,|v|<=V,|h|<=H for the 3D lander. Moves: a'=a+d, v'=v+a', h'=h+v'.
// predecessor of (a',v',h'): (a'-d, v'-a', h'-v').
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int A,V,H;
#define ID(a,v,h) ((((long)(a)+A)*(2*V+1)+((v)+V))*(2L*H+1)+((h)+H))
int main(int c,char**argv){A=atoi(argv[1]);V=atoi(argv[2]);H=atoi(argv[3]);
 long n=(2L*A+1)*(2L*V+1)*(2L*H+1); unsigned char*d=malloc(n); memset(d,255,n);
 long*Q=malloc(sizeof(long)*n); long hd=0,tl=0; d[ID(0,0,0)]=0; Q[tl++]=ID(0,0,0);
 while(hd<tl){long id=Q[hd++]; long h=id%(2L*H+1)-H; long r=id/(2L*H+1); long v=r%(2L*V+1)-V; long a=r/(2L*V+1)-A;
   for(int dd=-1;dd<=1;dd++){long pa=a-dd,pv=v-a,ph=h-v; if(labs(pa)>A||labs(pv)>V||labs(ph)>H)continue; long p=ID(pa,pv,ph); if(d[p]==255){d[p]=d[id]+1;Q[tl++]=p;}}}
 printf("00n:"); for(int k=0;k<=200 && k<=H;k++)printf(" %d",d[ID(0,0,k)]); printf("\n");
 printf("n00:"); for(int k=0;k<=A && k<=40;k++)printf(" %d",d[ID(k,0,0)]); printf("\n");
 printf("0n0:"); for(int k=0;k<=V && k<=60;k++)printf(" %d",d[ID(0,k,0)]); printf("\n");
 return 0;}
