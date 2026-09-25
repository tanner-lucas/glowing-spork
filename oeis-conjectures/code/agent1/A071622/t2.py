import gmpy2, math
from gmpy2 import mpz
p4=mpz(1); p3=mpz(1); s=0; first_ln=None; first_l10=None; first_nonpos=None
for k in range(1,60001):
    p4*=4; p3*=3
    s += 1 if (p4//p3) & 1 else -1
    if k>2300:
        if first_ln is None and s <= math.log(k)**2: first_ln=(k,s,math.log(k)**2)
        if first_l10 is None and s <= math.log10(k)**2: first_l10=(k,s,math.log10(k)**2)
        if first_nonpos is None and s <= 0: first_nonpos=(k,s)
print("first n>2300 with a(n)<=ln(n)^2:", first_ln)
print("first n>2300 with a(n)<=log10(n)^2:", first_l10)
print("first n>2300 with a(n)<=0:", first_nonpos)
