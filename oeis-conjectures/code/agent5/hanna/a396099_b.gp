B = x/(1-x) + 2*(x^4+x^5)/(1-x^4);
N0=60; A=x+O(x^2); for(i=1,N0, A2=subst(A,x,A); A3=subst(A,x,A2); A=x+A2*A3+O(x^(N0+1)));
Bs = B + O(x^(N0+1));
print(vector(N0,k,(polcoeff(A,k)-polcoeff(Bs,k))%4)==vector(N0,k,0));
\\ other claims: [x^n] A(A(x)) == 0 mod 4 for n>2 ; [x^n](A - x*A(A(A))) == 2 mod 4 for n>2
AA=subst(A,x,A); T=A-x*subst(A,x,AA);
print(vector(N0-2,k,polcoeff(AA,k+2)%4)); print(vector(N0-2,k,polcoeff(T,k+2)%4));
