B = x/(1-x) + 2*(x^4+x^5)/(1-x^4);
BB = subst(B,x,B); BBB = subst(B,x,BB);
chk(R)=my(N=numerator(R),D=denominator(R),c=content([N,D])); N/=c; D/=c; [polcoeff(D,0), content(N)];
print("identity x+BB*BBB-B: ", chk(x+BB*BBB-B));
S=BB+O(x^4); print("BB low terms: ", S);
print("BB - x - 2x^2: ", chk(BB - x - 2*x^2));
T=B-x*BBB; print("T low terms: ", T+O(x^4));
print("T - x - 2x^3/(1-x) : ", chk(T - x - 2*x^3/(1-x)));
