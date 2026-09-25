N=80; A=x+O(x^3);
for(i=1,N, F = x - A^2/(1-A^2); A = serreverse(F + O(x^(N+2))));
v=vector(N,n,polcoeff(A,n)); print(v[1..12]);
odd=select(n->v[n]%2, vector(N,n,n)); print("odd n: ", odd);
S=Set(concat(vector(7,m,3*2^(m-1)-2), vector(7,m,4*2^(m-1)-2))); print("A027383 up to N: ", select(t->t<=N, S));
