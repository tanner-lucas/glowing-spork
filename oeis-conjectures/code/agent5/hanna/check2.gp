default(nbthreads,1);
N=40;
tr(p,m)=sum(k=0,m,polcoeff(p,k)*x^k);  \\ truncate polynomial to degree m
C=Pol((1-sqrt(1-4*x+O(x^(N+3))))/2);
\\ A374570: A^2 = A(A*C)
A=x;
for(n=2,N, B=A+t*x^n; E=tr(B^2,n+1)-tr(subst(B,x,tr(B*C,n+1)),n+1); c=polcoeff(E,n+1); s=polcoeff(c,1,t); c0=polcoeff(c,0,t); A=A+(-c0/s)*x^n);
v=Vec(A); v=Vecrev(A)[2..N+1]; print("A374570 ",v[1..12]); print(" odd positions: ", select(k->v[k]%2, vector(#v,k,k)));
\\ A389540: A^2 = A(2x-2A)/2 ; a(n) determined at x^n
A=x;
for(n=2,N, B=A+t*x^n; E=tr(B^2,n)-tr(subst(B,x,2*x-2*B),n)/2; c=polcoeff(E,n); s=polcoeff(c,1,t); c0=polcoeff(c,0,t); A=A+(-c0/s)*x^n);
v=Vecrev(A)[2..N+1]; print("A389540 ",v[1..12]); print(" odd positions: ", select(k->v[k]%2, vector(#v,k,k)));
\\ A177775: [x^n] A^{o n} = [x^n] A^{o (n-1)} for n>2, a(1)=a(2)=1
it(B,m,deg)=my(R=x); for(i=1,m,R=tr(subst(B,x,R),deg)); R;
A=x+x^2;
for(n=3,24, B=A+t*x^n; c=polcoeff(it(B,n,n),n)-polcoeff(it(B,n-1,n),n); s=polcoeff(c,1,t); c0=polcoeff(c,0,t); A=A+(-c0/s)*x^n);
v=Vecrev(A)[2..25]; print("A177775 ",v[1..10]); print(" odd positions: ", select(k->v[k]%2, vector(#v,k,k)));
