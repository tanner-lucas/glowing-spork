import json, re
pat = re.compile(r'n\s*\*\s*[a-zA-Z(]|[0-9]n\s*[-+]|\bn[rs]\b|u\(n\)|v\(n\)')
ctx = re.compile(r'morphism|limiting word|Positions? of|fixed point|-> ?\{?[01]|transform of', re.I)
old=set(l.split('\t')[0] for l in open('hits.tsv'))
out=[]
with open('/home/user/work/idx/oeis.jsonl') as f:
    for line in f:
        d=json.loads(line)
        cs=d.get('C',[])+d.get('F',[])
        found=[c for c in cs if 'onjectur' in c and '<' in c and pat.search(c)]
        if not found: continue
        allt=d.get('N','')+' '+' '.join(cs)+' '+' '.join(d.get('prog',[]) if isinstance(d.get('prog'),list) else [])
        if not ctx.search(allt): continue
        if d['id'] in old: continue
        out.append((d['id'], d.get('N','')[:70], found[0][:150]))
for o in out: print(' | '.join(o))
print(len(out))
