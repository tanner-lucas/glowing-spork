\p 120
{
Q=1-2*x+x^2-2*x^3+2*x^4-x^5+2*x^6-2*x^7;
N=(1-x)*(1+x)*(1-x^8);   \\ g.f. of differences d(n)=a(n)-a(n-1) (d(0)=a(0))
dv=Vec(N/Q+O(x^400));
\\ polynomial division: N = q*Q + R
qr=divrem(N,Q); R=qr[2]; print("poly part deg ",poldegree(qr[1]));
rts=polroots(Q); 
\\ R/Q = sum_i c_i/(x - r_i) with c_i=R(r_i)/Q'(r_i);  [x^n] c/(x-r) = -c/r^(n+1)
B=vector(7,i, -subst(R,x,rts[i])/subst(Q',x,rts[i])/rts[i]); beta=vector(7,i,1/rts[i]);
print("beta moduli: ",vector(7,i,abs(beta[i])));
i1=0; for(i=1,7, if(abs(imag(beta[i]))<1e-50 && real(beta[i])>1.5, i1=i));
print("dominant beta=",real(beta[i1]),"  B=",real(B[i1]));
\\ check closed form vs exact
for(n=5,60, s=sum(i=1,7,B[i]*beta[i]^n); if(abs(s-dv[n+1])>1e-30, print("closed form mismatch n=",n)));
C=sum(i=1,7, if(i==i1,0,abs(B[i]))); m=vecmax(vector(7,i,if(i==i1,0,abs(beta[i]))));
N0=0; for(n=5,2000, if(real(B[i1])*real(beta[i1])^n > C*m^n, N0=n; break));
print("dominant term exceeds tail bound for all n >= ",N0," (ratio increasing since beta1>m)");
print("exact d(n)>0 for 1<=n<=",399,": ", vecmin(dv[2..400])>0);
}
