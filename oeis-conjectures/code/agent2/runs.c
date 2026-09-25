#include <stdio.h>
static int s2(long n){return __builtin_popcountl(n);}
static int s3(long n){int t=0;while(n){t+=n%3;n/=3;}return t;}
static int sbt(long n){int t=0;while(n){int d=n%3; if(d==2){t-=1;n=n/3+1;} else {t+=d;n/=3;}}return t;}
int main(){ long N=200000000; 
  for(int which=0;which<2;which++){
    long run=0,maxrun=0,count4=0; long bad4=0; long start=0;
    for(long n=1;n<=N;n++){ int in = which==0 ? (s2(n)==s3(n)) : (s2(n)==sbt(n));
      if(in){ if(run==0) start=n; run++; if(run>maxrun) maxrun=run; if(run==4){count4++; long need = which==0?4:0; if(start%6!=need) bad4++;} }
      else run=0; }
    printf("%s: N=%ld maxrun=%ld runs>=4: %ld, 4-runs with start not == %d mod 6: %ld\n", which==0?"A037301":"A330904", N, maxrun, count4, which==0?4:0, bad4);
  }
  /* sanity: first terms */
  printf("A037301 first: "); for(long n=0,c=0;c<15;n++) if(s2(n)==s3(n)){printf("%ld,",n);c++;} printf("\n");
  printf("A330904 first: "); for(long n=0,c=0;c<15;n++) if(s2(n)==sbt(n)){printf("%ld,",n);c++;} printf("\n");
}
