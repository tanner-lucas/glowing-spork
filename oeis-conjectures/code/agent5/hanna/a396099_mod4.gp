default(nbthreads,1);
B = x/(1-x) + 2*(x^4+x^5)/(1-x^4);
BB = subst(B,x,B); BBB = subst(B,x,BB);
R = x + BB*BBB - B;
N = numerator(R); D = denominator(R);
c = content([N,D]); \\ normalize
N=N/c; D=D/c;
print("D(0) = ", polcoeff(D,0), "   content(N) = ", content(N), "  content(D) = ", content(D));
print("deg N = ", poldegree(N), " deg D = ", poldegree(D));
\\ check series of A mod 4 against B for 60 terms by recursion
N0=60; A=x+O(x^2); for(i=1,N0, A2=subst(A,x,A); A3=subst(A,x,A2); A=x+A2*A3+O(x^(N0+1)));
Bs = B + O(x^(N0+1));
print("A == B mod 4 for 60 terms: ", Vec(A-Bs)%4 == vector(N0,k,0));
print(vector(12,k,polcoeff(A,k)%4));
