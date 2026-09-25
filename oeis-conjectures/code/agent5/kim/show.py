import json,re,sys
def entry(a):
    d=a[1:]
    return open(f"/home/user/work/oeisdata/seq/A{d[:3]}/{a}.seq").read()
T=json.load(open('targets.json'))
for a in T:
    e=entry(a)
    N=[l[11:] for l in e.splitlines() if l.startswith('%N')][0]
    m=re.search(r'(Positions of [01]\'?s? in|complement of) (A\d{6})',N)
    ref=None
    m2=re.search(r'in (A\d{6})',N)
    if m2: ref=m2.group(1)
    line=f"{a} | {N[:90]}"
    if ref:
        e2=entry(ref); N2=[l[11:] for l in e2.splitlines() if l.startswith('%N')][0]
        line+=f" || {ref}: {N2[:100]}"
    print(line)
