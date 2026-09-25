default(parisizemax, 1000000000);
ispow(n,b) = if(n<1,0, n==b^valuation(n,b));
N=70;
\\ A384270: A(x) = A(x^4 + 4*x*A^4) / A(x^3 + 3*x*A^3), offset 1
A=x; for(i=1,N, A=A+O(x^(i+2)); A = subst(A,x,x^4+4*x*A^4)/subst(A,x,x^3+3*x*A^3));
v=Vec(A); print("A384270: ", v[1..10], " #", #v, "  parity ok: ", prod(n=1,#v,(v[n]%2==1)==ispow(n,2)));
A=x; for(i=1,N, A=A+O(x^(i+2)); A = subst(A,x,x^3-3*x*A^3)/subst(A,x,x^2-2*x*A^2));
v=Vec(A); print("A384830: ", v[1..10], " #", #v, "  parity ok: ", prod(n=1,#v,(v[n]%2==1)==ispow(n,2)));
is2(n) = my(d=digits(n,3)); if(d[1]!=0 && 0, 0); my(m=2*n, e=digits(m,3)); vecsum(e)==2 && vecmax(e)==1;
print("  mod3: ==1 iff 3^k: ", prod(n=1,#v, (v[n]%3==1)==ispow(n,3)), "   ==2 iff 2n sum of two distinct powers of 3: ", prod(n=1,#v, (v[n]%3==2)==is2(n)));
quit;
