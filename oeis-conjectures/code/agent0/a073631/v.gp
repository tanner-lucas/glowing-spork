p=3842760169;
print("isprime(p)=",isprime(p));
print("(3/2)^(p-1) mod p^2 == 1: ", Mod(3,p^2)^(p-1)==Mod(2,p^2)^(p-1));
k=p^2; print("k=",k);
print("k | 3^(k-1)-2^(k-1): ", Mod(3,k)^(k-1)==Mod(2,k)^(k-1));
print("issquarefree(k)=",issquarefree(k), "  k%529=",k%529);
q=41975417117; print("q prime ",isprime(q)," ", Mod(3,q^2)^(q^2-1)==Mod(2,q^2)^(q^2-1));
quit
