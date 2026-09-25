#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// usage: ./t LIMIT pat1 rep1 pat2 rep2 ...
int main(int argc,char**argv){
  long LIM=atol(argv[1]); int nr=(argc-2)/2; char **pat=argv+2; 
  char *w=malloc(LIM+10), *w2=malloc(LIM+10); strcpy(w,"00"); long len=2;
  printf("0 %ld\n",len);
  for(int it=1;it<200;it++){
    long o=0,i=0; int over=0;
    while(i<len){ int done=0;
      for(int r=0;r<nr;r++){ char *p=pat[2*r], *q=pat[2*r+1]; long pl=strlen(p);
        if(i+pl<=len && strncmp(w+i,p,pl)==0){ long ql=strlen(q); if(o+ql>LIM){over=1;break;} memcpy(w2+o,q,ql); o+=ql; i+=pl; done=1; break; } }
      if(over) break;
      if(!done){ if(o+1>LIM){over=1;break;} w2[o++]=w[i++]; }
    }
    if(over) break;
    char *t=w; w=w2; w2=t; len=o; w[len]=0;
    if(it<=6) printf("%d %ld %s\n",it,len,w); else printf("%d %ld\n",it,len);
    fflush(stdout);
  }
}
