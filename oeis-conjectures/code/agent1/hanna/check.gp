default(parisizemax, 2000000000);
ispow(n,b) = if(n<1,0, n==b^valuation(n,b));
fib(f) = bitand(f, f>>1)==0;
\\ A368628
N=400; A=1+O(x^N); for(i=1,N, B=subst(A,x,-x); A = 1 + x*(A^2-B^2)/2 + x*(A^4+B^4)/2);
v=Vec(A); print("A368628 first: ", v[1..8]); print("A368628 parity claim ok up to ", N-1, ": ", prod(n=0,N-1, (v[n+1]%2==1) == (n==0 || ispow(3*n+1,4))));
\\ A368635
A=1+O(x^N); for(i=1,N, A = 1 + 3*x*A^2 - 2*x*subst(A,x,-x)^2);
v=Vec(A); print("A368635 first: ", v[1..8]); print("A368635 parity ok: ", prod(n=0,N-1, (v[n+1]%2==1) == ispow(n+1,2)));
\\ A397588  (offset 1)
A=x+O(x^N); for(i=1,N, A = x + deriv(x*A^2));
v=Vec(A); print("A397588 first: ", v[1..8]); print("A397588 parity ok: ", prod(n=1,#v, (v[n]%2==1) == ispow(n,2)));
\\ A393856 (offset 1): A(x - x*A(4x)/4) = x
N2=300; A=x+O(x^N2); for(i=1,N2, A = serreverse(x - x*subst(A,x,4*x)/4));
v=Vec(A); print("A393856 first: ", v[1..8]);
print("A393856 parity ok: ", prod(n=1,#v, (v[n]%2==1) == ispow(n,2)), "  mod4 == Catalan(n-1): ", prod(n=1,#v, (v[n]-binomial(2*n-2,n-1)/n)%4==0), "  all == 1 mod 5: ", prod(n=1,#v, v[n]%5==1));
\\ A380708: A = 1 + x*abs(1/A)^2 coefficientwise abs
A=1+O(x^N); for(i=1,N, C=Vec(1/A); C=vector(#C,j,abs(C[j])); A = 1 + x*(Ser(C)+O(x^N))^2);
v=Vec(A); print("A380708 first: ", v[1..10]); print("A380708 parity ok: ", prod(n=1,N-1, (v[n+1]%2==1) == (n%2==1 && fib((n-1)/2))));
\\ A382319 / A382318
N3=300; A=x+O(x^N3); for(i=1,N3, A = x/(1-x) + sum(k=1,N3-1, subst(A^3,x,x^k)));
a=Vec(A); B = x + A^3; b=Vec(B);
print("A382319 first: ", a[1..8], "  A382318 first: ", b[1..8]);
print("A382318(3n)==A382319(n) mod 3: ", prod(n=1,(#b)\3, (b[3*n]-a[n])%3==0), "  other residues 0 mod 3 (n>=1): ", prod(m=4,#b, m%3==0 || b[m]%3==0));
