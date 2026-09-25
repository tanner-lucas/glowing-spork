import subprocess
def rec(init, coeffs, N):
    a=list(init)
    while len(a)<N:
        n=len(a); a.append(sum(c*a[n-k] for k,c in coeffs.items()))
    return a
cases=[
 ("A288524/A288523",["00","0101","10","010"], rec([2,4,5,8,11],{1:1,2:1,3:1,4:-2},400)),
 ("A288633/A288465",["00","0110","1","10"], rec([2,4,6,10],{1:2,4:-1},400)),
 ("A288668",["00","0110","10","000"], None),
 ("A288732",["00","1000","10","01"], rec([2,4,6,8,10],{1:1,4:2,5:-2},400)),
 ("A288926/A288925",["00","1000","10","0001"], rec([2,4,8,13,26],{1:1,2:1,4:3,5:-2},400)),
 ("A288932/A123720",["00","1000","10","10101"], [2**n+2**(n-1)-n if n>0 else 2 for n in range(400)]),
 ("A289035/A289004",["00","0010","01","010","10","010"], None),
 ("A289107",["00","0010","01","011","10","000"], rec([2,4,7,12,22],{1:2,3:-1},400)),
 ("A289239/A289004",["00","0010","01","100","10","010"], None),
]
# A288668: a(n)=a(n-2)+2a(n-3), a(0)=2, a(2)=4, a(3)=5 -- a(1)? read data
import re
def seqdata(A):
    s=open(f"/home/user/work/oeisdata/seq/{A[:4]}/{A}.seq").read()
    t="".join(re.findall(r"^%[STU] "+A+r" (.*)$",s,re.M))
    return [int(x) for x in t.replace(" ","").split(",") if x]
d668=seqdata("A288668"); d004=seqdata("A289004")
r668=rec(d668[:3],{2:1,3:2},400)
r004=rec(d004[:10],{1:2,2:-1,4:2,5:-1,7:1,8:-1,10:-1},400)
assert r004[:len(d004)]==d004 and r668[:len(d668)]==d668
cases=[(n,r,(t if t is not None else (r668 if '668' in n else r004))) for n,r,t in cases]
for name,rules,target in cases[3:]:
    out=subprocess.run(["./t","400000000"]+rules,capture_output=True,text=True).stdout.split("\n")
    lens=[int(l.split()[1]) for l in out if l.strip()]
    mism=[(i,lens[i],target[i]) for i in range(len(lens)) if lens[i]!=target[i]]
    print(name,"iterates computed:",len(lens)-1," first mismatch:",mism[:3])
