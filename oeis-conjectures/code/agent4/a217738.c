#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long ull; typedef unsigned __int128 u128;
// fast doubling F(n) mod m
static void fib(ull n, ull m, ull *F, ull *G){ // returns F(n), F(n+1)
  if(n==0){*F=0;*G=1%m;return;}
  ull a,b; fib(n>>1,m,&a,&b);
  ull c=(ull)((u128)a*(( (2*(u128)b) + m - a)%m)%m); // F(2k)=F(k)*(2F(k+1)-F(k))
  ull d=(ull)(((u128)a*a + (u128)b*b)%m);
  if(n&1){*F=d;*G=(c+d)%m;} else {*F=c;*G=d;}
}
int main(int argc,char**argv){
  ull N=strtoull(argv[1],0,10); long cnt=0,bad=0;
  for(ull k=1;k<=N;k++){
    ull m=k*(k+1); ull F,G; fib(k,m,&F,&G);
    if(F==0){ cnt++; if(cnt<=15) printf("%llu,",k); if(k%12){ bad++; printf("\nNOT DIV BY 12: %llu\n",k);} }
  }
  printf("\nN=%llu terms=%ld non-multiples-of-12=%ld\n",N,cnt,bad);
}
