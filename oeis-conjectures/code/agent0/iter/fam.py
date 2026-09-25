import re
def seqdata(A):
    s=open(f"/home/user/work/oeisdata/seq/{A[:4]}/{A}.seq").read()
    t="".join(re.findall(r"^%[STU] "+A+r" (.*)$",s,re.M))
    return [int(x) for x in t.replace(" ","").split(",") if x]
def rec(init, coeffs, N):
    a=list(init)
    while len(a)<N:
        n=len(a); a.append(sum(c*a[n-k] for k,c in coeffs.items()))
    return a
d004=seqdata("A289004"); r004=rec(d004[:10],{1:2,2:-1,4:2,5:-1,7:1,8:-1,10:-1},60)
assert r004[:len(d004)]==d004
print("A289004 data length",len(d004))
d010=seqdata("A289010"); print("A289010:",d010[:30])
def iterate(rules, n_iter):
    pat=re.compile("|".join(re.escape(p) for p,_ in rules)); d=dict(rules)
    w="00"; L=[2]
    for i in range(n_iter):
        w=pat.sub(lambda m: d[m.group(0)], w); L.append(len(w))
    return L
for name,rules,target in [("A289001",[("00","0010"),("01","001"),("10","010")],r004),
                          ("A289035",[("00","0010"),("01","010"),("10","010")],r004),
                          ("A289239",[("00","0010"),("01","100"),("10","010")],r004),
                          ("A289242",[("00","0010"),("01","100"),("10","100")],r004),
                          ("A289071",[("00","0010"),("01","010"),("10","100")],d010)]:
    L=iterate(rules,30)
    mm=[(i,L[i],target[i]) for i in range(min(len(L),len(target))) if L[i]!=target[i]]
    print(name,"lengths n=20..26:",L[20:27],"first mismatch:",mm[:2])
