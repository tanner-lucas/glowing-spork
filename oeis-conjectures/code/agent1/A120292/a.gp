\\ a(n) = numerator of (sum_{k<=n}(p_k+1) - 1)/prod_{k<=n}(p_k+1)
N = 200000;
PN = prime(N);
isp = vectorsmall(PN+2); forprime(p=2, PN, isp[p]=1);
\\ v_q(P_n) truncated at 'need', P_n = prod_{k<=n}(p_k+1), p_n = pn
vq(q, pn, need) = {my(v=0, m=q); while(m <= pn+1, forstep(x=m-1, pn, m, if(isp[x], v++; if(v>=need, return(v)))); m*=q); v};
anum(n, S, pn) = {my(f=factor(S), a=1); for(i=1,#f~, my(q=f[i,1], e=f[i,2], v=vq(q, pn, e)); if(v<e, a*=q^(e-v))); a};
\\ reproduce data via direct formula for first 70 and via definition for first 30
{
S=0; res=List(); comp=List();
forprime(p=2, PN, n=primepi(p); S += p+1;
  my(num = anum(n, S-1, p));
  if(n<=70, listput(res, num));
  if(num>1 && !isprime(num), listput(comp, [n, num, factor(num)]); if(bigomega(num)>2, print("NON-SEMIPRIME: n=",n," a(n)=",num," = ",factor(num))));
);
print("first 70: ", Vec(res));
print("#composite terms n<=",N,": ", #comp);
print("first composite n: ", vector(min(15,#comp),i,comp[i][1]));
print("first composite values: ", vector(min(8,#comp),i,comp[i][2]));
}
\\ cross-check first 30 with matdet definition
print(vector(30,n,abs(numerator(matdet(matrix(n,n,i,j,if(i==j,prime(i)/(1+prime(i)),1)))))));
quit;
