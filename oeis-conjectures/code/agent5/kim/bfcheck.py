import json, mpmath as mp
mp.mp.dps=40
rows={x['A']:x for x in json.load(open('rows.json'))}
res=[json.loads(l) for l in open('analyze_all.out') if l.startswith('{')]
bf={}
for fn in ('crossbf_part1.out','crossbf_part2.out'):
    for l in open(fn):
        if l.startswith('{'): z=json.loads(l); bf[(z['id'],z['sub'])]=z
bad=0; n=0
for r in res:
    b=bf.get((r['id'],r['sub']))
    if not b: print('missing',r['id'],r['sub']); continue
    if not r['pisot']: continue
    n+=1
    inf=mp.mpf(r['inf']); sup=mp.mpf(r['sup']); mn=mp.mpf(b['bf_min']); mx=mp.mpf(b['bf_max'])
    tol=mp.mpf('1e-15')
    ok = mn>=inf-tol and mx<=sup+tol
    if not ok: bad+=1; print('INCONSISTENT',r['id'],r['sub'],inf,mn,sup,mx)
    gap=max(mn-inf, sup-mx)
print('checked',n,'inconsistent',bad)
for k,b in bf.items():
    if 'bf_first_violation' in b: print(k,b['bf_first_violation'])
