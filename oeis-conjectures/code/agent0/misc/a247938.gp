best=0; forprime(p=2,67, my(r=sigma(2^p-1)/2^p); if(r>best, best=r; print("p=",p," ratio=",r," = ",r*1.)));
print("max over p<=67 attained at p=11: 135/128 = ",135/128.);
\\ analytic bound check for 19<=p<=200: s<p/log2(2p+1), bound exp(H_s/(2p)) < 135/128
bad=0; forprime(p=19,2000, my(s=floor(p/log(2*p+1)*log(2)), H=sum(i=1,s,1./i)); if(exp(H/(2*p))>=135/128., bad++; print("bound fails p=",p))); print("bound failures 19..2000: ",bad);
quit
