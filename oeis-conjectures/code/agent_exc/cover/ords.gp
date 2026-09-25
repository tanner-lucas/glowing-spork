default(parisize, 10^9);
for(L=1,72, f=factor(polcyclo(L,10))[,1]; for(i=1,#f, q=f[i]; if(q!=3 && q!=2 && q!=5 && znorder(Mod(10,q))==L, print(L," ",q))));
