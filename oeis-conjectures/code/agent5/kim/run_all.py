import json,re,sys
import sympy as sp
import mpmath as mp
from fractions import Fraction as Fr
from qs import QS
from engine import Problem, apply
mp.mp.dps=80
specs=json.load(open('specs_raw.json')); conj=json.load(open('conj_parsed.json'))
def entry(a):
    d=a[1:]; return open(f"/home/user/work/oeisdata/seq/A{d[:3]}/{a}.seq").read()
def lines(e,tag): return [l[11:] for l in e.splitlines() if l.startswith(tag)]
def data(a):
    e=entry(a); s=''.join(x.strip() for x in lines(e,'%S')+lines(e,'%T')+lines(e,'%U'))
    return [int(x) for x in s.split(',') if x]
def offset(a): return int(lines(entry(a),'%O')[0].split(',')[0])
def to_qs(expr_str, d):
    """parse string -> QS in Q(sqrt d) or None if not representable"""
    e=sp.nsimplify(sp.sympify(expr_str.replace('^','**')),rational=True) if re.search(r'\d\.\d',expr_str) else sp.sympify(expr_str.replace('^','**'))
    e=sp.radsimp(sp.expand(e))
    sq=sp.sqrt(d)
    b=sp.expand(e).coeff(sq); a=sp.simplify(sp.expand(e)-b*sq)
    if not (a.is_Rational and b.is_Rational): return None
    return QS(Fr(int(a.p),int(a.q)),Fr(int(b.p),int(b.q)),d)
def mpval(expr_str):
    return mp.mpf(sp.N(sp.sympify(expr_str.replace('^','**')),90))
# ---- build instances ----
inst=[]
for a,s in specs.items():
    c=conj[a]; nest=s.get('nest'); kind=s['kind']
    base=dict(id=a,kind=kind,notes=[])
    if kind in ('fixed','lim0','lim1'):
        sig=s['morph']; tau=('0','1'); start=nest[2]; K=nest[3]
        if (nest[0],nest[1])!=tuple(sig): base['notes'].append(f"Mathematica %t uses morphism {nest[0]},{nest[1]} but %N says {sig[0]},{sig[1]}; %N used (matches data)")
    elif kind=='transform':
        sig=(nest[0],nest[1]); tau=tuple(s['morph']); start=nest[2]; K=nest[3]
    else:
        sig=s['morph'] if s['morph'] else (nest[0],nest[1]); tau=('0','1'); start=nest[2]; K=nest[3]
    for (lo,mid,hi) in c['ineqs'][:2]:
        if 'A026363' in mid: continue
        I=dict(base); I['notes']=list(base['notes'])
        I.update(sig=sig,tau=tau,start=start,K=K,lo=lo,hi=hi,mid=mid,nmin=c['nmin'] if c['nmin'] is not None else 1)
        # letter
        if 'u(n)' in mid: I['c']=0; I['reading']='u(n) = position of n-th 0 in the word (literal "# 0\'s <= n" makes the statement trivially false)'; I['sub']='u'
        elif 'v(n)' in mid: I['c']=1; I['reading']='v(n) = position of n-th 1 in the word (literal "# 1\'s <= n" makes the statement trivially false)'; I['sub']='v'
        elif kind in ('fixed','lim0','lim1','transform'): I['c']=s['letter']; I['reading']=f"a(n) = position of n-th {s['letter']} in {s['word']} (1-based)"; I['sub']=''
        else:
            I['sub']=''
            if a in ('A026363','A026367','A045671','A086398'): I['c']=1
            else: I['c']=0
            I['reading']=f"a(n) = position of n-th {I['c']} in the fixed point of {sig[0]},{sig[1]} (identification from the entry's comments; checked against data)"
        # multiplier R and sign
        sign=1; R=None
        m=re.match(r'n\s*\*\s*([rs])\s*-\s*[auv]\(n\)',mid)
        if m: R=c['defs'].get(m.group(1))
        m=re.match(r'n\s*\*\s*(sqrt\(\d+\))\s*-\s*a\(n\)',mid)
        if m: R=m.group(1)
        m=re.match(r'n\s*\*\s*(\(.*\))\s*-\s*a\(n\)',mid)
        if m: R=m.group(1)
        m=re.match(r'a\(n\)\s*-\s*n\s*\*\s*(sqrt\(\d+\))',mid)
        if m: R=m.group(1); sign=-1
        if mid.strip()=='n*sqrt(3)': R='sqrt(3)'; I['notes'].append('Literal statement "-2 < n*sqrt(3) < 3" omits "- a(n)" (typo; literally false at n=2); read as n*sqrt(3) - a(n)')
        I['R']=R; I['sign']=sign
        if a=='A284895' and hi=='2': I['notes'].append("Second inequality is Dekking's suggested corrected conjecture")
        inst.append(I)
print(len(inst),"instances")
json.dump(inst,open('instances.json','w'),indent=1)
