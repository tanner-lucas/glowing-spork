\\ third check in PARI/GP: build fixed point of 0->1, 1->101010 by iterating on Vecsmall
sig(w) = {my(L=sum(i=1,#w, if(w[i],6,1)), v=vectorsmall(L), j=0); for(i=1,#w, if(w[i], v[j+1]=1;v[j+2]=0;v[j+3]=1;v[j+4]=0;v[j+5]=1;v[j+6]=0; j+=6, v[j+1]=1; j+=1)); v};
w = Vecsmall([0]); while(#w < 21000000, w = sig(w));
print("length ", #w, " prefix ", vector(20,i,w[i]));
\\ n-th one and n-th zero
c1=0; c0=0; P1=0; P0=0;
for(p=1, 21000000, if(w[p], c1++; if(c1==2977771, P1=p), c0++; if(c0==8933313, P0=p)));
print("position of 2977771-th 1: ", P1, "   position of 8933313-th 0: ", P0);
s = (-1+sqrt(21))/2; r = (9+sqrt(21))/6;
print("2977771*s - P1 = ", 2977771*s - P1, "   exact test 21*n^2 > (2a+4+n)^2 : ", 21*2977771^2 > (2*P1+4+2977771)^2);
print("8933313*r - P0 = ", 8933313*r - P0, "   exact test 21*n^2 > (6a+12-9n)^2 : ", 21*8933313^2 > (6*P0+12-9*8933313)^2, " (rhs>0: ", 6*P0+12-9*8933313 > 0, ")");
quit;
