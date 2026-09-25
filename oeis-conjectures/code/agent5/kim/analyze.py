import json,re,sys
import sympy as sp
import mpmath as mp
from fractions import Fraction as Fr
from qs import QS
from engine import Problem, apply
from run_all import data, offset, to_qs, mpval, entry, lines
mp.mp.dps=80
inst=json.load(open('instances.json'))
# dedupe identical (id, lo, hi, R)
seen=set(); I2=[]
for x in inst:
    key=(x['id'],x['sub'],x['lo'],x['hi'],re.sub(r'[ ()]','',x['R'] or ''))
    if key in seen: continue
    seen.add(key); I2.append(x)
inst=I2
for x in inst:
    if x['id'] in ('A045671','A045672'): x['nmin']=0
def fmt(v,dig=35):
    return mp.nstr(v,dig) if isinstance(v,mp.mpf) else mp.nstr(v.mpf(),dig)
def gen_word(x, minlen=6000):
    s0,s1=x['sig']; w=str(x['start']); K=x['K']
    for _ in range(K): w=apply([s0,s1],w)
    k=K
    while len(w)<minlen:
        for _ in range(2): w=apply([s0,s1],w)
        k+=2
    return w
results=[]
only=sys.argv[1:] 
for x in inst:
    if only and x['id'] not in only: continue
    res=dict(id=x['id'],sub=x['sub'],morph=f"0->{x['sig'][0]}, 1->{x['sig'][1]}",tau=(f"0->{x['tau'][0]}, 1->{x['tau'][1]}" if tuple(x['tau'])!=('0','1') else ''),
             start=x['start'],K=x['K'],letter=x['c'],reading=x['reading'],stated=f"{x['lo']} < {x['mid']} < {x['hi']}"+(f", R = {x['R']}" if x['R'] else ''),notes=list(x['notes']),nmin=x['nmin'])
    # ---- validate against data
    w=gen_word(x)
    coded=''.join(x['tau'][int(ch)] for ch in w)
    pos=[i+1 for i,ch in enumerate(coded) if ch==str(x['c'])]
    dat=data(x['id']); off=offset(x['id'])
    if x['sub']:  # fixed point entry: data is the word
        ok = [int(ch) for ch in coded[:len(dat)]]==dat
    else:
        dd = dat[1:] if (off==0) else dat
        ok = pos[:len(dd)]==dd
    res['data_ok']=ok; res['ndata']=len(dat)
    if not ok: res['notes'].append('DATA MISMATCH'); 
    P=Problem(x['sig'][0],x['sig'][1],x['tau'][0],x['tau'][1],start=x['start'],K=x['K'],c=x['c'])
    d=P.d; r=P.r
    res['r_exact']=str(r); res['r_num']=fmt(r); res['lambda2']=fmt(P.l2,12); res['pisot']=bool(P.pisot)
    res['root']=P.b; res['period']=P.p
    # stated R
    Rq=None; Rnum=None
    if x['R']:
        Rs=x['R']
        if Rs=='(1 + sqrt(3))2':
            res['notes'].append('Stated r = "(1 + sqrt(3))2" is a typo; read as (1 + sqrt(3))/2')
            Rs='(1 + sqrt(3))/2'
        if re.fullmatch(r'\d+\.\d+',Rs):
            Rnum=mp.mpf(Rs); res['notes'].append(f'r stated only as decimal {Rs}...; exact r used')
            Rq=r if abs(r.mpf()-Rnum)<mp.mpf('1e-4') else None
        else:
            Rq=to_qs(Rs,d); Rnum=mpval(Rs)
    r_match = (Rq is not None and Rq==r)
    res['r_stated_matches']=r_match
    if not r_match:
        res['notes'].append(f"Stated multiplier {x['R']} = {mp.nstr(Rnum,12)} differs from the true density ratio r = {r} = {mp.nstr(r.mpf(),12)}; literal statement fails by linear drift; intended reading uses exact r")
        # literal first violation
        lo_l=mpval(x['lo'].replace('r','('+x['R']+')') if 'sqrt' not in x['lo'] else x['lo']); hi_l=mpval(x['hi'] if x['hi']!='r' else x['R'])
        for n,an in enumerate(pos,1):
            Dl=(n*Rnum-an)*x['sign']
            if not (lo_l<Dl<hi_l): res['literal_first_violation']=(n,an,mp.nstr(Dl,15)); break
    # bounds in terms of D = n r - a(n)
    def bnd(sv):
        sv=sv.strip()
        if sv=='r': sv='('+(x['R'] if x['R']!='(1 + sqrt(3))2' else '(1 + sqrt(3))/2')+')'
        q=to_qs(sv,d)
        if q is None:
            q=to_qs(sv,1) 
        return q
    lo=bnd(x['lo']); hi=bnd(x['hi'])
    if x['sign']==-1: lo,hi=-hi,-lo
    res['Dlo']=str(lo); res['Dhi']=str(hi)
    # literal typo A284371: "-2 < n*sqrt(3) < 3"
    if x['mid'].strip()=='n*sqrt(3)': res['literal_first_violation']=(2,None,'2*sqrt(3)=3.464 > 3')
    # special initial terms (n=0 for A045671/2)
    if x['nmin']==0:
        a0=dat[0]; D0=-a0
        res['notes'].append(f"n=0 term: a(0)={a0}, D(0)={D0}, inside bounds: {lo < QS(D0,0,d) < hi}")
    # ---- extremes
    if P.pisot:
        ex=P.exact_extremes()
        inf=ex['min'][0]; sup=ex['max'][0]
        res['inf_exact']=str(inf); res['sup_exact']=str(sup); res['inf']=fmt(inf); res['sup']=fmt(sup)
        viol_lo = inf<lo; viol_hi = sup>hi
        eq_lo = inf==lo; eq_hi = sup==hi
        res['inf_eq_lo']=eq_lo; res['sup_eq_hi']=eq_hi
    else:
        res['inf']='-infinity (non-Pisot)'; res['sup']='+infinity (non-Pisot)'
        viol_lo=viol_hi=True; eq_lo=eq_hi=False
    # attainment check for equalities: D(n) = bound possible only if bound - n r in Z
    attained=[]
    for (eq,B) in ((eq_lo,lo),(eq_hi,hi)):
        if eq:
            # n r - a = B  => n*r.b == B.b ; a = n r.a - B.a integer
            if r.b!=0:
                nn=B.b/r.b
                if nn.denominator==1 and nn>=1:
                    nn=int(nn); aa=nn*r.a-B.a
                    if aa.denominator==1 and nn<=len(pos) and pos[nn-1]==int(aa): attained.append((nn,int(aa)))
    # ---- verdict
    first=None
    if viol_lo or viol_hi or attained:
        fv=P.first_violation_dfs(lo,hi,maxT=600)
        if fv:
            n,an,Dv=fv
            # exact check
            Dex=r*n-an
            ok_ex = not (lo<Dex<hi)
            first=(n,an,fmt(Dv,25),ok_ex)
            res['first_violation']=dict(n=n,a_n=an,D=fmt(Dv,30),exact_check=ok_ex,
                in_data=(n-1 < len(pos) and (n <= len(dat))))
        if not P.pisot: verdict='NON-PISOT (unbounded) -> FALSE'
        else: verdict='FALSE'
    elif eq_lo or eq_hi:
        verdict='BOUNDARY (inf/sup equals bound, not attained) -> holds'
    else:
        verdict='PROVED'
    res['verdict']=verdict
    results.append(res)
    print(json.dumps(res)); sys.stdout.flush()
json.dump(results,open('results_%s.json'%('all' if not only else '_'.join(only)),'w'),indent=1)
