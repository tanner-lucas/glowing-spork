import sys, json
sys.path.insert(0,'/home/user/work/agent5/morph')
from exact2 import analyze
import mpmath as mp
mp.mp.dps=60
inst={ (x['id'],x['sub']):x for x in json.load(open('/home/user/work/agent5/kim/instances.json'))}
bad=0; n=0
for l in open('/home/user/work/agent5/kim/analyze_all.out'):
    if not l.startswith('{'): continue
    r=json.loads(l)
    if not r['pisot']: continue
    x=inst[(r['id'],r['sub'])]
    # exact2.analyze(i0,i1,tau0,tau1,c,root,parity,T): root=start letter, parity=K mod 2
    rr,l2,inf,sup=analyze(x["sig"][0],x["sig"][1],x["tau"][0],x["tau"][1],x["c"],r["root"],(None if r["period"]==1 else 0),T=700)
    di=abs(inf-mp.mpf(r['inf'])); ds=abs(sup-mp.mpf(r['sup']))
    n+=1
    ok = di<mp.mpf('1e-25') and ds<mp.mpf('1e-25')
    if not ok: bad+=1; print('MISMATCH',r['id'],r['sub'],mp.nstr(inf,20),r['inf'][:22],mp.nstr(sup,20),r['sup'][:22])
print('compared',n,'mismatches',bad)
