import json, re
pat = re.compile(r'[<>]=?\s*n\s*\*\s*[a-z]\s*-\s*[a-z]\(n\)|n\s*\*\s*[a-z]\s*-\s*[a-z]\(n\)\s*<|[a-z]\s*-\s*[a-z]\(n\)/n\s*<|n\*sqrt|n\s*\*\s*\(?\s*sqrt|n\*Pi\s*-|n\s*\*\s*r\s*-')
hits=[]
with open('/home/user/work/idx/oeis.jsonl') as f:
    for line in f:
        d=json.loads(line)
        cs=d.get('C',[])+d.get('F',[])
        txt=' '.join(cs)
        found=[c for c in cs if ('onjectur' in c) and pat.search(c)]
        if not found: continue
        name=d.get('N','')
        prog=' '.join(d.get('prog',[]) if isinstance(d.get('prog'),list) else [str(d.get('prog',''))])
        morph = bool(re.search(r'morphism|limiting word|->|Positions of|fixed point|transform', name+' '+txt+' '+prog))
        hits.append((d['id'], morph, name[:120], found[0][:260]))
print(len(hits))
with open('hits.tsv','w') as g:
    for h in hits: g.write('\t'.join(map(str,h))+'\n')
print(sum(1 for h in hits if h[1]))
