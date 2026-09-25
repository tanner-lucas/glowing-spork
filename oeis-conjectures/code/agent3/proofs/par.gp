{
\\ A222014 : A = sum_{n>=0} n! x^n A^(n^2) / prod_{k=1..n}(1+k x A^n)
N=40; A=1+O(x^(N+1));
for(i=1,N, A=sum(n=0,N, n!*x^n*A^(n^2)/prod(k=1,n,1+k*x*A^n)) + O(x^(N+1)));
v=Vec(A); print("A222014 first terms: ", v[1..12]);
print("A222014 parity check n<=",N,": ", vector(N+1,n, v[n]%2==((n)==2^valuation(n,2))));
\\ n-1 index: coefficient of x^m is v[m+1]; odd iff m+1 power of 2
print("A222014 odd indices: ", select(m->v[m+1]%2, vector(N+1,i,i-1)));
\\ A375439
M=250; B=x+x^2+O(x^(M+1)); for(i=1,M, B=x+x^2+(2*B^3+subst(B,x,x^3))/3+O(x^(M+1)));
w=Vec(B); print("A375439 first: ", w[1..12], "  integral: ", #select(c->denominator(c)!=1,w)==0);
print("A375439 odd indices <= ",M,": ", select(m->w[m]%2, vector(#w,i,i)));
}
