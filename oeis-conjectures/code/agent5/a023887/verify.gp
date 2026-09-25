q=3294173; print(isprime(q), " ", factor(q-1));
x=Mod(7,q)^(7^6); print("Phi_7(7^(7^6)) mod q = ", 1+x+x^2+x^3+x^4+x^5+x^6);
\\ sigma_n(n) for n=7^6 equals sum_{i=0..6} 7^(n*i) = Phi_7(7^n)
n=7^6; y=Mod(7,q)^n; print("sigma_n(n) mod q = ", sum(i=0,6,y^i));
\\ p=3 and p=5 cases
print(factor(sigma(9,9))); print(ispseudoprime(polcyclo(3125,5)));
