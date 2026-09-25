default(nbthreads,1);
N=40;
\\ A091713: A = x + x*A(A(A(x)))
A=x+O(x^2); for(i=1,N, A = x + x*subst(A,x,subst(A,x,A)) + O(x^(N+1))); v=Vec(A); print("A091713 ",v[1..12]); print(" all odd: ", vector(N,k,v[k]%2)==vector(N,k,1));
\\ A396099: A = x + A(A(x))*A(A(A(x)))
A=x+O(x^2); for(i=1,N, A2=subst(A,x,A); A3=subst(A,x,A2); A = x + A2*A3 + O(x^(N+1))); v=Vec(A); print("A396099 ",v[1..10]," allodd ",vector(N,k,v[k]%2)==vector(N,k,1));
\\ A374570: A^2 = A(A*C), C = x + C^2
C=(1-sqrt(1-4*x+O(x^(N+2))))/2;
A=x+O(x^2);
for(n=2,N, B=A+t*x^n+O(x^(n+1)); E=B^2-subst(B,x,B*C); c=polcoeff(E,n+1); s=polcoeff(c,1,t); c0=polcoeff(c,0,t); A=A+(-c0/s)*x^n + O(x^(n+1)));
v=Vec(A); print("A374570 ",v[1..12]); print(" odd positions: ", select(k->v[k]%2, vector(#v,k,k)));
\\ A389540: A^2 = A(2x-2A)/2
A=x+O(x^2);
for(n=2,N, B=A+t*x^n+O(x^(n+1)); E=B^2-subst(B,x,2*x-2*B)/2; c=polcoeff(E,n); s=polcoeff(c,1,t); c0=polcoeff(c,0,t); A=A+(-c0/s)*x^n+O(x^(n+1)));
v=Vec(A); print("A389540 ",v[1..12]); print(" odd positions: ", select(k->v[k]%2, vector(#v,k,k)));
\\ A368633: A = 1 + 2xA^2 - xA(-x)^2
A=1+O(x); for(i=1,N+1, A=1+2*x*A^2-x*subst(A,x,-x)^2+O(x^(N+1))); v=Vec(A); print("A368633 ",v[1..12]); print(" odd positions (n=index-1): ", select(k->v[k+1]%2, vector(#v,k,k-1)));
