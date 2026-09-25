import sys
N=1<<22
a=[0]*(N+2)
a[0]=1
# A(x) = (1-x)^3 A(x^2): a(2k)=a(k)+3a(k-1); a(2k+1)=-3a(k)-a(k-1)
for n in range(1,N+1):
    k=n>>1
    ak=a[k]; akm=a[k-1] if k>=1 else 0
    a[n] = ak+3*akm if n%2==0 else -3*ak-akm
# check against OEIS data
S=open('/home/user/work/oeisdata/seq/A373/A373308.seq').read()
data=[int(x) for x in "".join(l[11:] for l in S.splitlines() if l[:2] in('%S','%T','%U')).replace('\n','').split(',') if x.strip()]
print("data match:", a[:len(data)]==data, len(data))
# direct product check for small n
M=300
p=[1]+[0]*M
e=1
while e<=M:
    for _ in range(3):
        q=p[:]
        for i in range(e,M+1): q[i]-=p[i-e]
        p=q
    e*=2
print("product check:", p==a[:M+1])
tm=lambda n: 1 if bin(n).count('1')%2==0 else 2
c1=all(a[3*n]%3==tm(n) for n in range(N//3))
c2=all(a[3*n+1]%3==0 and a[3*n+2]%3==0 for n in range((N-2)//3))
# A000695: sums of distinct powers of 4 = numbers with only bits in even positions
def in695(k): return k & 0xAAAAAAAAAAAAAAAA == 0
zeros=[n for n in range(N+1) if a[n]==0]
pred=[n for n in range(N+1) if (n+1)%3==0 and (n+1)//3>=1 and in695((n+1)//3)]
print("conj1:",c1," conj2:",c2," conj3 (zeros == 3*A000695(k)-1, k>=1) up to",N,":",zeros==pred)
print(zeros[:20]); print(pred[:20])
print("max |a|:",max(abs(x) for x in a[:N+1]))
