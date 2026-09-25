// 2D 5-neighbor outer totalistic CA (Wolfram code), single ON cell, infinite plane with uniform background.
// usage: ca RULE T  -> prints for n=0..T: left x-axis string, right x-axis string, ON count within [-n,n]^2
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){
  int R=atoi(argv[1]); int T=atoi(argv[2]); int mode=argc>3?atoi(argv[3]):0;
  int W=2*T+5, C=T+2; unsigned char *a=calloc(W*W,1), *b=calloc(W*W,1); int bg=0;
  a[C*W+C]=1;
  for(int n=0;n<=T;n++){
    // output stage n
    if(mode==0){
      printf("%d L ",n); int started=0; for(int x=-n;x<=0;x++){ int v=a[C*W+C+x]; if(v) started=1; if(started) putchar('0'+v);} if(!started) putchar('0');
      printf(" R "); started=0; for(int x=0;x<=n;x++){ int v=a[C*W+C+x]; if(v) started=1; if(started) putchar('0'+v);} if(!started) putchar('0');
      long cnt=0; for(int y=-n;y<=n;y++) for(int x=-n;x<=n;x++) cnt+=a[(C+y)*W+C+x];
      printf(" ON %ld\n",cnt);
    } else {
      long cnt=0; for(int y=-n;y<=n;y++) for(int x=-n;x<=n;x++) cnt+=a[(C+y)*W+C+x];
      printf("%d %ld\n",n,cnt);
    }
    if(n==T) break;
    // step: cells within radius n+1 computed; others = new background
    int nbg=(R>>(2*4*bg+bg))&1;
    for(int y=0;y<W;y++) for(int x=0;x<W;x++){
      if(y<1||x<1||y>=W-1||x>=W-1){ b[y*W+x]=nbg; continue; }
      int s=a[(y-1)*W+x]+a[(y+1)*W+x]+a[y*W+x-1]+a[y*W+x+1]; int c=a[y*W+x];
      b[y*W+x]=(R>>(2*s+c))&1;
    }
    bg=nbg; unsigned char*t=a;a=b;b=t;
  }
}
