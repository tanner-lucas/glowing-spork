def a(n):
    m=n+1
    while bin(n^m).count('1')!=4: m+=1
    return m
seq=open('/home/user/work/oeisdata/seq/A182/A182336.seq').read()
t=[]
for l in seq.splitlines():
    if l[:2] in('%S','%T','%U'): t+=[int(x) for x in l.split(' ',2)[2].strip().strip(',').split(',') if x]
print('data match', [a(n) for n in range(len(t))]==t)
bad=[n for n in range(97,300001) if not (n+1<=a(n)<=9*n/8+1)]
print('violations 97..3e5:',bad[:10])
print('n=96:',a(96),9*96/8+1)
# check constructive bound m-n from proof for all n>=112 up to 3e5
def proofm(n):
    t=3
    while (n>>t)&1: t+=1
    if t>=6: return n+(1<<(t-3))
    return None
ok=all((proofm(n) is None) or (bin(n^proofm(n)).count('1')==4 and proofm(n)-n<=n/8+1) for n in range(112,300001))
print('proof construction valid 112..3e5:',ok)
