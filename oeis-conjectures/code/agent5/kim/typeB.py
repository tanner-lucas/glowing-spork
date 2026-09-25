import json,re
import mpmath as mp
from run_all import data, offset
hits=[l.rstrip('\n').split('\t') for l in open('hits.tsv')]
rows=[]
for i,m,n,c in hits:
    if 'a(n)/n' not in c: continue
    e=open(f"/home/user/work/oeisdata/seq/A{i[1:4]}/{i}.seq").read()
    C=[l[11:] for l in e.splitlines() if l.startswith('%C') and 'a(n)/n' in l and 'onjectur' in l]
    t=C[0] if C else c
    mm=re.search(r'->\s*([-+0-9.sqrt() ]+?)(?:\.\.\.|,|\s+as|\s+and)',t)
    b=re.search(r'([-0-9/]+)\s*<\s*m\s*-\s*a\(n\)/n\s*(<=?)\s*([-0-9/ m+]+?)\s*(?:<|for|$)',t)
    nm=re.search(r'n\s*>=\s*(\d+)',t)
    rows.append((i,t[:200],mm.group(1) if mm else None,b.groups() if b else None,int(nm.group(1)) if nm else 1))
out=[]
for i,t,mstr,b,nmin in rows:
    if not mstr or not b: out.append((i,'UNPARSED',t)); continue
    try: m=mp.mpf(eval(mstr.replace('sqrt','mp.sqrt')))
    except Exception: out.append((i,'UNPARSED-m',t)); continue
    lo=eval(b[0]); hiexpr=b[2].strip()
    hi=eval(hiexpr.replace('m','('+str(m)+')'))
    dat=data(i); off=offset(i)
    unc=mp.mpf(10)**(-(len(mstr.split('.')[1]) if '.' in mstr else 30))  # truncation uncertainty of stated m
    bad=[]
    for k,an in enumerate(dat):
        n=k+off
        if n<nmin or n<=0: continue
        v=m-mp.mpf(an)/n
        if v<=lo-unc or (v>=hi+unc if b[1]=='<' else v>hi+unc): bad.append((n,an,mp.nstr(v,6)))
    status = 'EMPTY-INTERVAL' if lo>=hi else ('VIOLATED-IN-DATA' if bad else 'ok-in-data')
    out.append((i,status,f"m~{mstr} bounds {b[0]} {b[1]} {hiexpr}; first bad {bad[:2]}"))
for o in out: print(' | '.join(map(str,o)))
json.dump(out,open('typeB.json','w'),indent=1)
