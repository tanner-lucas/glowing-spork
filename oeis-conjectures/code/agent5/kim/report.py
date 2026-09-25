import json,re,csv
import mpmath as mp
from fractions import Fraction as Fr
from qs import QS
mp.mp.dps=60
def parse_qs(s):
    m=re.fullmatch(r'\((.*)\)\+\((.*)\)\*sqrt\((\d+)\)',s)
    if m: return QS(Fr(m.group(1)),Fr(m.group(2)),int(m.group(3)))
    return QS(Fr(s),0,1)
def pretty(q):
    q=parse_qs(q) if isinstance(q,str) else q
    if q.b==0: return str(q.a)
    a,b,d=q.a,q.b,q.d
    s=''
    if a!=0: s+=str(a)
    sb=('+' if b>0 and a!=0 else ('-' if b<0 else ''))
    ab=abs(b)
    s+=(sb if a!=0 else ('-' if b<0 else ''))+('' if ab==1 else str(ab)+'*')+f'sqrt({d})'
    return s
res=[json.loads(l) for l in open('analyze_all.out') if l.startswith('{')]
strict=json.load(open('strict.json'))
bf={}
for fn in ('crossbf_part1.out','crossbf_part2.out'):
    try:
        for l in open(fn):
            if l.startswith('{'):
                z=json.loads(l); bf[(z['id'],z['sub'])]=z
    except FileNotFoundError: pass
prior={
 'A284753':'Entry already cites a proof (Fokkink-Joshi, Theorem 19).',
 'A284894':'Entry proves only boundedness (weak form).',
 'A284895':'Entry (Dekking 2018) already notes the first inequality is false at n=2 and suggests 0 < a(n)-n*sqrt(2) < 2.',
 'A285074':'Entry contains a proof (Dekking).','A285075':'Entry contains a "proof"; it overlooks n=1 (equality).',
 'A285077':'Entry: provable as A285074 (Dekking).','A285078':'Entry (Dekking): provable for n>=2.',
 'A285669':'Entry proves only boundedness (weak form).',
 'A287664':'Entry contains a proof (best bounds (-(2/3)phi, 1)).','A287665':'Entry contains a proof.',
 'A287770':'Entry contains a proof sketch (Sturmian).'}
rows=[]
for r in res:
    key=r['id']+r['sub']
    v=r['verdict']
    fv=r.get('first_violation'); st=strict.get(key)
    rq=parse_qs(r['r_exact'])
    lo=parse_qs(r['Dlo']); hi=parse_qs(r['Dhi'])
    cert=''; verdict=''
    if v.startswith('PROVED'): verdict='PROVED'
    elif v.startswith('BOUNDARY'):
        which=[]
        if r.get('inf_eq_lo'): which.append('inf = lower bound')
        if r.get('sup_eq_hi'): which.append('sup = upper bound')
        verdict='BOUNDARY (holds; '+', '.join(which)+', never attained)'
    else:
        n=fv['n']; an=fv['a_n']
        Dex=rq*n-an
        eqonly = (st is None) or (st and not st['strict_exact'])
        if eqonly:
            verdict=f'FALSE only at n={n} by equality (D({n}) = bound exactly); strict inequality holds for all n>=2 (inf/sup equal the bounds, attained only at n=1)'
        else:
            n2=st['n']; an2=st['a_n']; D2=rq*n2-an2
            pre='NON-PISOT (unbounded) -> ' if v.startswith('NON') else ''
            if n2!=n:
                verdict=f"{pre}FALSE: D({n}) equals a bound (non-strict); first strict violation n={n2}"
            else:
                verdict=f"{pre}FALSE: smallest violating n={n2}"
            cert=f"n={n2}, a(n)={an2}, n*r - a(n) = {pretty(D2)} = {mp.nstr(D2.mpf(),25)} (bounds {pretty(lo)} , {pretty(hi)})"
            if n!=n2: cert=f"n={n}: D = {pretty(Dex)} (equality); "+cert
    notes=[n for n in r['notes'] if not n.startswith('Stated multiplier') and not n.startswith('Literal statement "-2')]
    if r['id'] in prior: notes.append(prior[r['id']])
    lit=[]
    mism=[n for n in r['notes'] if n.startswith('Stated multiplier')]
    if mism:
        m=re.match(r'Stated multiplier (.*?) = ([0-9.]+) differs from the true density ratio r = (.*?) = ([0-9.]+);',mism[0])
        lit.append(f"stated multiplier {m.group(1)} ~ {m.group(2)} is not the density ratio r = {pretty(m.group(3))} ~ {m.group(4)[:10]}")
    if r.get('literal_first_violation'):
        lf=r['literal_first_violation']
        lit.append(f"literal statement first fails at n={lf[0]} (value {lf[2][:12]})")
    if r['id']=='A284371': lit=['literal "-2 < n*sqrt(3) < 3" omits "- a(n)"; literally false at n=2 (2*sqrt(3) > 3)']
    if r['id']=='A285423': lit=['literal "r = (1 + sqrt(3))2" is malformed (missing "/"); read as 2*(1+sqrt(3)) it fails at n=1 (D = 4.46)']
    if r['sub'] in ('u','v'): lit.append('literal "u(n) = # 0s <= n" (v: # 1s) makes the statement trivially false; intended u/v = positions')
    lit='; '.join(lit)
    b=bf.get((r['id'],r['sub']))
    bfs=''
    if b:
        bfs=f"first {b['bf_nmax']} terms: min {b['bf_min'][:14]} (n={b['bf_min_n']}), max {b['bf_max'][:14]} (n={b['bf_max_n']})"
        if 'bf_first_violation' in b: bfs+=f"; brute-force first violation: {b['bf_first_violation']}"
    rows.append(dict(A=r['id']+(('('+r['sub']+')') if r['sub'] else ''),
        word=f"{r['morph']}"+(f"; tau: {r['tau']}" if r['tau'] else '')+f"; start {r['start']}, K={r['K']} (limit word = fixed point of sigma^{r['period']} from letter {r['root']})",
        letter=r['letter'], reading=r['reading'], stated=r['stated'],
        r_exact=pretty(r['r_exact']), lambda2=r['lambda2'],
        inf_exact=(pretty(r['inf_exact']) if 'inf_exact' in r else '-inf'), inf=r['inf'],
        sup_exact=(pretty(r['sup_exact']) if 'sup_exact' in r else '+inf'), sup=r['sup'],
        verdict=verdict, literal_note=lit, certificate=cert, notes=' '.join(notes), bruteforce=bfs, data_ok=r['data_ok'], ndata=r['ndata']))
json.dump(rows,open('rows.json','w'),indent=1)
with open('/home/user/work/results/kimberling_all.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(x) for x in rows]
print(len(rows))
from collections import Counter
print(Counter(x['verdict'].split(' ')[0].split(':')[0] for x in rows))
