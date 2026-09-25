#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
int main(int argc,char**argv){
  uint64_t N=strtoull(argv[1],0,10);
  uint8_t *b=calloc(N/8+1,1);
  for(uint64_t x=0;3*x*x+x*x*x<=N;x++)
    for(uint64_t y=x; x*x+2*y*y+x*y*y<=N; y++){
      uint64_t base=x*x+y*y; uint64_t z=y; uint64_t v=base+z*z+x*y*z;
      while(v<=N){ b[v>>3]|=1<<(v&7); z++; v=base+z*z+x*y*z; }
    }
  // report a(n)/n at checkpoints; check a(n) < 2n and a(n) <= a(n-1)+a(n-2)
  uint64_t cnt=0; uint64_t p1=0,p2=0; uint64_t next=10; long viol1=0, viol2=0; double maxratio=0; uint64_t maxr_n=0;
  for(uint64_t v=0;v<=N;v++) if(b[v>>3]>>(v&7)&1){ cnt++; // a(cnt)=v
      if(cnt>1 && v>=2*cnt){viol1++; if(viol1<10) printf("a(%lu)=%lu >= 2n\n",cnt,v);} 
      if(cnt>4 && v>p1+p2){viol2++; if(viol2<10) printf("a(%lu)=%lu > a(n-1)+a(n-2)\n",cnt,v);} 
      if(cnt>1000){ double r=(double)v/cnt; if(r>maxratio){maxratio=r;maxr_n=cnt;} }
      p2=p1; p1=v;
      if(v>=next){ printf("v~%lu n=%lu a(n)/n=%.6f\n",v,cnt,(double)v/cnt); next*=10; }
  }
  printf("N=%lu count=%lu ratio=%.6f max ratio(n>1000)=%.6f at n=%lu viol=%ld %ld\n",N,cnt,(double)N/cnt,maxratio,maxr_n,viol1,viol2);
}
