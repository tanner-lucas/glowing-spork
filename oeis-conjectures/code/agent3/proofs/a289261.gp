{
Q=1-2*x+x^2-2*x^3+2*x^4-x^5+2*x^6-2*x^7;
R=polroots(Q); print(R); print(vector(#R,i,abs(R[i])));
\\ reciprocal polynomial roots = growth rates
P=polrecip(Q); r=polroots(P); print("growth rates |.|: ", vector(#r,i,abs(r[i])));
G=(1+x)*(1-x^8)/Q; v=Vec(G+O(x^60)); print(v[1..20]);
}
