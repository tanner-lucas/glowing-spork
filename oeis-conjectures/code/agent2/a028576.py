import gmpy2
from gmpy2 import mpz
from sympy import factorint, divisors
N=6000
C=[mpz(1)]*(N+1)
for d in range(1,N+1): C[d]=C[d-1]*(2*(2*d-1))//d
def mu(n):
    f=factorint(n)
    if any(e>1 for e in f.values()): return 0
    return -1 if len(f)%2 else 1
MU=[0]+[mu(n) for n in range(1,N+1)]
bad=[]
for n in range(1,N+1):
    S=sum(MU[n//d]*C[d]**2 for d in divisors(n))
    if S % (4*n) : bad.append((n,'notint')); continue
    a=S//(4*n)
    if a % n or (3*a) % (n*n): bad.append((n,int(a%n),int((3*a)%(n*n))))
print("checked n<=",N,"violations:",bad[:10])
# check listed data
S0=open('/home/user/work/oeisdata/seq/A028/A028576.seq').read()
print([l for l in S0.splitlines() if l.startswith(('%S','%O','%C'))][:6])
print([int(sum(MU[n//d]*C[d]**2 for d in divisors(n))//(4*n)) for n in range(1,12)])
