from sympy import primerange
def ds(m): return sum(map(int,str(m)))
P=list(primerange(2,2*10**6))
a=[None]+[sum(ds(m) for m in range(P[i]+1,P[i+1])) for i in range(len(P)-1)]  # a[n], n 1-based: between prime(n)=P[n-1] and prime(n+1)=P[n]
S=[0,4,6,18,3,18,9,9,40,3,35,27,6,27,43,55,6,50,36,9,65,27,70,84,36,3,18,9,9,93,27,40,12,81,6,50,53,36,58,70,9,126,12,45,18,68,83,27,12,18,55,6,99,55,58,70,9,65,45,12,135,147,27,6,27,126,50,99,15,27,70,84,68,80,36]
print("data ok:", a[1:len(S)+1]==S)
lit=[];intd=[]
for n in range(10,len(a)-2):
    if a[n]>a[n+1]<a[n+2]:
        if P[n]-P[n-1]!=2: lit.append(n)
        if P[n+1]-P[n]!=2: intd.append((n,P[n],P[n+1],a[n],a[n+1],a[n+2]))
print("literal violations (first 5):", lit[:5], len(lit))
print("intended violations:", len(intd)); print(intd[:10])
