a(n)=my(s=sigma(n)); sumdiv(n,d,moebius(d)*(s\d))
{
bad=0; for(n=2,200000, v=a(n); pp=isprimepower(n); if(v>n || (pp && v!=n) || (!pp && v>=n), bad++; print("counter n=",n)));
print("A074882: checked n<=200000, violations: ",bad);
bad2=0; for(n=2,200000, if(isprimepower(n),next); f=factor(n); k=#f~; gap=n-sigma(n)*eulerphi(n)/n; if(gap<2^(k-1), bad2++; print("gap fail n=",n," gap=",gap)));
print("gap >= 2^(omega-1) failures: ",bad2);
}
