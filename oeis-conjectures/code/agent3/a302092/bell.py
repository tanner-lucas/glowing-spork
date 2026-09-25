import gmpy2, sys
from gmpy2 import mpz
need={2,3,7,13,42,55,2841,3984,4539,4700,6048,7477}
N=max(need)
row=[mpz(1)]  # Bell triangle row 0 -> B(0)=1
res={}
for n in range(1,N+1):
    new=[row[-1]]
    for x in row: new.append(new[-1]+x)
    row=new
    # row[0] = B(n)
    if n in need:
        b=row[0]; s=str(b); r=mpz(s[::-1])
        res[n]=(gmpy2.is_prime(b,5), s[-1], gmpy2.is_prime(r,25), len(s))
        print(n, 'B prp', res[n][0], 'last', res[n][1], 'rev prp', res[n][2], 'digits', res[n][3], flush=True)
