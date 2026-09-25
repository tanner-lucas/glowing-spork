\\ greedy representation in base of squares: returns digit vector (most significant first), last digit = coefficient of 1^2
rep(n)={my(d=List(),s=sqrtint(n)); forstep(k=s,1,-1, my(q=n\(k^2)); listput(d,q); n-=q*k^2); Vec(d)};
last(n)=my(v=rep(n)); v[#v];
\\ reproduce A007961 data prefix
print(vector(19,n,fromdigits(rep(n))));
\\ reproduce A376360 data and find gap-12
L=List(); for(n=1,400000, if(last(n)==3, listput(L,n)));
print(Vec(L)[1..22]);
for(i=1,#L-1, if(L[i+1]-L[i]==12, print("gap 12: a(",i,")=",L[i],"  a(",i+1,")=",L[i+1]," reps: ",rep(L[i])," ",rep(L[i+1])); break));
print("between: ", vector(11,j,last(336391+j)));
quit
