import json,re
def entry(a):
    d=a[1:]; return open(f"/home/user/work/oeisdata/seq/A{d[:3]}/{a}.seq").read()
def lines(e,tag): return [l[11:] for l in e.splitlines() if l.startswith(tag)]
def data(a):
    e=entry(a); s=''.join(x.strip() for x in lines(e,'%S')+lines(e,'%T')+lines(e,'%U'))
    return [int(x) for x in s.split(',') if x]
def offset(a):
    return int(lines(entry(a),'%O')[0].split(',')[0])
def parse_morph(text):
    # "0 -> 1, 1 -> 1010" or "0->10, 1-> 001" or "{0->1, 1->000}"
    m=re.search(r'0\s*->\s*([01]+)\s*,\s*1\s*->\s*([01]+)',text)
    return (m.group(1),m.group(2)) if m else None
def parse_nest(e):
    for l in lines(e,'%t'):
        m=re.search(r'Nest\[Flatten\[# /\. \{0 -> \{([0-9, ]+)\}, 1 -> \{([0-9, ]+)\}\}\] &, \{([01])\}, (\d+)\]',l)
        if m:
            return (m.group(1).replace(', ','').replace(',',''), m.group(2).replace(', ','').replace(',',''), int(m.group(3)), int(m.group(4)))
    return None
T=json.load(open('targets.json'))
specs={}
for a in T:
    e=entry(a); N=lines(e,'%N')[0]; C=lines(e,'%C')
    conj=[c for c in C if 'onjectur' in c and '<' in c]
    sp={'id':a,'N':N,'conj':conj}
    m=re.search(r'Positions of ([01])\'?s? in (A\d{6})',N)
    if m:
        sp['letter']=int(m.group(1)); W=m.group(2); sp['word']=W
        eW=entry(W); NW=lines(eW,'%N')[0]; sp['wordN']=NW
        sp['morph']=parse_morph(NW)
        if 'transform' in NW:
            sp['kind']='transform'
        elif '0-limiting' in NW: sp['kind']='lim0'
        elif '1-limiting' in NW: sp['kind']='lim1'
        elif 'Fixed point' in NW: sp['kind']='fixed'
        sp['nest']=parse_nest(eW) or parse_nest(e)
    else:
        sp['kind']='other'; sp['nest']=parse_nest(e); sp['morph']=parse_morph(N+' '+' '.join(C))
    specs[a]=sp
json.dump(specs,open('specs_raw.json','w'),indent=1)
for a,sp in specs.items():
    print(a, sp.get('kind'), sp.get('letter'), sp.get('word'), sp.get('morph'), sp.get('nest'), '|', (sp['conj'][0][:120] if sp['conj'] else 'NOCONJ'))
