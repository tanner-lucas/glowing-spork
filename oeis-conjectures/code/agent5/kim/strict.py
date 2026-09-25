import json
from engine import Problem
from qs import QS
from fractions import Fraction as Fr
import re, mpmath as mp
def parse_qs(s):
    m=re.fullmatch(r'\((.*)\)\+\((.*)\)\*sqrt\((\d+)\)',s)
    if m: return QS(Fr(m.group(1)),Fr(m.group(2)),int(m.group(3)))
    return QS(Fr(s),0,1)
inst={ (x['id'],x['sub']):x for x in json.load(open('instances.json'))}
out={}
for l in open('analyze_all.out'):
    if not l.startswith('{'): continue
    r=json.loads(l)
    if 'first_violation' not in r: continue
    x=inst[(r['id'],r['sub'])]
    P=Problem(x['sig'][0],x['sig'][1],x['tau'][0],x['tau'][1],start=x['start'],K=x['K'],c=x['c'])
    lo=parse_qs(r['Dlo']); hi=parse_qs(r['Dhi'])
    if lo.b!=0 and P.d!=lo.d: pass
    fv=P.first_violation_dfs(lo,hi,maxT=600,strict=True)
    if fv:
        n,an,D=fv; Dex=P.r*n-an
        out[r['id']+r['sub']]=dict(n=n,a_n=an,D=mp.nstr(D,30),strict_exact=(Dex<lo or Dex>hi))
    else: out[r['id']+r['sub']]=None
    print(r['id'],r['sub'],'first(any)=',r['first_violation']['n'],'first strict=',out[r['id']+r['sub']])
json.dump(out,open('strict.json','w'),indent=1)
