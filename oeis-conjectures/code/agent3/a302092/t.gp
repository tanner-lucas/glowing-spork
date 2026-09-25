rev(x)=fromdigits(Vecrev(digits(x)));
bell(n)=sum(k=0,n,stirling(n,k,2));
{
foreach([2,3,7,13,42,55,2841,3984,4539,4700,6048,7477], n, b=bell(n); r=rev(b); print(n," isPRP(B)=",ispseudoprime(b)," last digit ",b%10," rev PRP? ",ispseudoprime(r)));
}
