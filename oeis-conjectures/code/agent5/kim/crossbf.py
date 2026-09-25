import json,subprocess,sys
import mpmath as mp
from qs import QS
from fractions import Fraction as Fr
mp.mp.dps=50
res=[json.loads(l) for l in open(sys.argv[1]) if l.startswith('{')]
inst={ (x['id'],x['sub']):x for x in json.load(open('instances.json'))}
def parse_qs(s):
    # "(a)+(b)*sqrt(d)" or "a"
    import re
    m=re.fullmatch(r'\((.*)\)\+\((.*)\)\*sqrt\((\d+)\)',s)
    if m: return QS(Fr(m.group(1)),Fr(m.group(2)),int(m.group(3)))
    return QS(Fr(s),0,1)
def Kprime(x,maxpos):
    s0,s1=x['sig']; t0,t1=x['tau']
    L=[len(t0),len(t1)]; K=x['K']
    # length of tau(sigma^k(start)) via counts
    cnt=[1 if x['start']==0 else 0, 1 if x['start']==1 else 0]
    k=0
    while True:
        if k>=K and (k-K)%2==0 and cnt[0]*L[0]+cnt[1]*L[1]>=maxpos: return k
        cnt=[cnt[0]*s0.count('0')+cnt[1]*s1.count('0'), cnt[0]*s0.count('1')+cnt[1]*s1.count('1')]; k+=1
out=[]
done=set()
import os
if os.path.exists('crossbf_part1.out'):
    for l in open('crossbf_part1.out'):
        if l.startswith('{'):
            z=json.loads(l); done.add((z['id'],z['sub']))
MAXMM=int(float(sys.argv[2])) if len(sys.argv)>2 else 10**8
for r in res:
    if (r['id'],r['sub']) in done: continue
    x=inst[(r['id'],r['sub'])]
    rq=parse_qs(r['r_exact']); rs=mp.nstr(rq.mpf(),40)
    kp=Kprime(x,MAXMM)
    o=subprocess.run(['./bfmm',x['sig'][0],x['sig'][1],x['tau'][0],x['tau'][1],str(x['start']),str(kp),str(x['c']),rs,str(MAXMM)],capture_output=True,text=True).stdout.split()
    rec=dict(id=r['id'],sub=r['sub'],bf_positions=int(o[0]),bf_nmax=int(o[1]),bf_min=o[2],bf_min_n=int(o[3]),bf_max=o[4],bf_max_n=int(o[5]))
    fv=r.get('first_violation')
    if fv:
        lo=parse_qs(r['Dlo']).mpf(); hi=parse_qs(r['Dhi']).mpf()
        need=fv['a_n']+10
        if need<=6*10**9:
            kp2=Kprime(x,need)
            o2=subprocess.run(['./bf',x['sig'][0],x['sig'][1],x['tau'][0],x['tau'][1],str(x['start']),str(kp2),str(x['c']),rs,mp.nstr(lo,40),mp.nstr(hi,40),str(need)],capture_output=True,text=True).stdout.strip()
            rec['bf_first_violation']=o2
        else: rec['bf_first_violation']='beyond brute-force range'
    out.append(rec); print(json.dumps(rec)); sys.stdout.flush()
json.dump(out,open('crossbf_part2.json','w'),indent=1)
