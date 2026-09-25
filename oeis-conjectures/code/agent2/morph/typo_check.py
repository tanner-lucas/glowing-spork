from firstviol import gen
from decimal import Decimal, getcontext
getcontext().prec=40
w=gen("1","1101",1,1,5000)
u=[i+1 for i,c in enumerate(w) if c==0]
r_typo=(5+Decimal(3).sqrt())/2; r_fix=(5+Decimal(13).sqrt())/2
first=[n for n in range(1,len(u)+1) if not (0 < n*r_typo-u[n-1] < 2)][:3]
print("A284386 first 12 u(n):",u[:12]); print("with r=(5+sqrt3)/2 first failures n:",first,[float(n*r_typo-u[n-1]) for n in first])
print("with r=(5+sqrt13)/2: min,max over n<=%d:"%len(u), min(float(n*r_fix-u[n-1]) for n in range(1,len(u)+1)), max(float(n*r_fix-u[n-1]) for n in range(1,len(u)+1)))
