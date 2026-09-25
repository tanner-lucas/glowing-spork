default(parisizemax, 1000000000);
ispow(n,b) = if(n<1,0, n==b^valuation(n,b));
N=60;
A=x+O(x^(N+1)); for(i=1,3*N, A = subst(A,x,x^4+4*x*A^4)/subst(A,x,x^3+3*x*A^3));
v=Vec(A); print("A384270: ", v[1..12], " #", #v);
print("fails: ", select(n->(v[n]%2==1)!=ispow(n,2), [1..#v]));
\\ check equation residual
print("residual valuation: ", valuation(A*subst(A,x,x^3+3*x*A^3) - subst(A,x,x^4+4*x*A^4), x));
quit;
