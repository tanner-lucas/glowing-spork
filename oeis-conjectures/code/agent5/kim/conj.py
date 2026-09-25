import json,re
specs=json.load(open('specs_raw.json'))
def parse(text):
    t=text.replace(' ',' ')
    # variable definitions
    defs={}
    for m in re.finditer(r'\b([rs])\s*=\s*([-+0-9sqrt()./ *]+?)(?=\s*(?:,|and|so that|\.\s|\.$|$|;|\s+the|\s+\(|\.\.| \[))',t):
        defs.setdefault(m.group(1),m.group(2).strip())
    ineqs=[]
    for m in re.finditer(r'(-?\s*[0-9][0-9/.]*(?:\s*[-+]\s*sqrt\(\d+\))?|-?\s*sqrt\(\d+\)|-?\s*1\s*\+\s*sqrt\(\d+\))\s*<\s*([^<]{3,40}?)\s*<\s*(-?[0-9][0-9/.]*|-?\s*sqrt\(\d+\)|r|s|-?[0-9]+\s*\+\s*sqrt\(\d+\))(?=[\s,.;]|$)',t):
        ineqs.append((m.group(1).strip(),m.group(2).strip(),m.group(3).strip()))
    nmin=re.search(r'n\s*>=\s*(\d+)',t)
    return defs,ineqs,(int(nmin.group(1)) if nmin else None)
out={}
for a,sp in specs.items():
    txt=' '.join(sp['conj'])
    i=txt.find('onjectur'); txt2=txt[i-2:] if i>=0 else txt
    defs,ineqs,nmin=parse(txt)
    out[a]=dict(defs=defs,ineqs=ineqs,nmin=nmin)
    print(a, defs, ineqs, nmin)
json.dump(out,open('conj_parsed.json','w'),indent=1)
