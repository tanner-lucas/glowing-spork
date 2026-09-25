from math import e
N=300000
divs=[[] for _ in range(N+1)]
for d in range(1,N+1):
    for m in range(d,N+1,d): divs[m].append(d)
def Delta(n):
    D=divs[n]; best=0; j=0
    for i in range(len(D)):
        while j<len(D) and D[j] <= e*D[i]: j+=1
        best=max(best,j-i)
    return best
S=[1,2,1,2,1,2,1,2,1,2,1,3,1,2,2,2,1,2,1,3,2,2,1,4,1,2,1,2,1,3,1,2,1,2]
print("data ok:", [Delta(n) for n in range(1,len(S)+1)]==S)
bad=[n for n in range(1,N+1) if 2*Delta(n) > len(divs[n])]
print("n<=%d with a(n) > d(n)/2:"%N, bad)
