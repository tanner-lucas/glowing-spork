#include <stdio.h>
#include <stdlib.h>
// Huffman with weights 1..n via two-queue method. Track, for each node, min leaf depth below it (as height to shallowest leaf).
// minlen(root) = min over leaves of depth = computed as mind(node) = 0 for leaf, 1+min(mind(children)) for internal.
// tie mode 0: prefer leaf when weights equal; mode 1: prefer internal node.
typedef long long ll;
int main(int argc,char**argv){
  int N=atoi(argv[1]);
  ll *iw=malloc(sizeof(ll)*(N+1)); int *im=malloc(sizeof(int)*(N+1));
  for(int n=2;n<=N;n++){
    int res[2];
    for(int mode=0;mode<2;mode++){
      int li=1, ih=0, it=0; // leaves 1..n weights = index
      for(int step=0;step<n-1;step++){
        ll w[2]; int m[2];
        for(int t=0;t<2;t++){
          int useleaf;
          if(li>n) useleaf=0; else if(ih==it) useleaf=1;
          else { ll lw=li, nw=iw[ih]; useleaf = (lw<nw) || (lw==nw && mode==0); }
          if(useleaf){ w[t]=li; m[t]=0; li++; } else { w[t]=iw[ih]; m[t]=im[ih]; ih++; }
        }
        iw[it]=w[0]+w[1]; im[it]=1+(m[0]<m[1]?m[0]:m[1]); it++;
      }
      res[mode]=im[it-1];
    }
    // conjecture floor(log2(2(n+1)/3))
    int c=0; while((1LL<<(c+1))*3 <= 2LL*(n+1)) c++;
    if(res[0]!=c || res[1]!=c) { printf("n=%d leafpref=%d nodepref=%d conj=%d\n",n,res[0],res[1],c); }
    if(n<=40) fprintf(stderr,"%d,",res[0]);
  }
  fprintf(stderr,"\ndone\n");
}
