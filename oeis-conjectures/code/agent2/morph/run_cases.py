import subprocess, sys, re
from cases import cases
L = int(sys.argv[1]) if len(sys.argv)>1 else 10**6
def oeis_S(aid):
    a=aid[:7]; txt=open(f"/home/user/work/oeisdata/seq/{a[:4]}/{a}.seq").read()
    s="".join(l.split(" ",2)[2] for l in txt.splitlines() if l[:2] in("%S","%T","%U"))
    return [int(x) for x in s.replace("\n","").split(",") if x.strip()]
for (aid,i0,i1,st,pw,let,rr,lo,hi) in cases:
    out=subprocess.run(["./morphs",i0,i1,str(st),str(pw),str(L),rr,rr,"60"],capture_output=True,text=True).stdout
    lines=out.splitlines()
    pos=[int(x) for x in lines[let].split(":")[1].strip(",").split(",")]
    data=None
    try:
        if aid[-1] not in "uv": data=oeis_S(aid)
    except Exception as e: data=None
    ok = "n/a" if data is None else (pos[:len(data)]==data[:len(pos)])
    m=re.search(r"n\*r-pos0\(n\): min (\S+) at n=(\d+) ; max (\S+) at n=(\d+)",out) if let==0 else re.search(r"n\*s-pos1\(n\): min (\S+) at n=(\d+) ; max (\S+) at n=(\d+)",out)
    mn,amn,mx,amx=float(m.group(1)),int(m.group(2)),float(m.group(3)),int(m.group(4))
    viol = (mn<=lo) or (mx>=hi)
    print(f"{aid:10s} dataOK={ok} bounds=({lo},{hi}) min={mn:.6f}@{amn} max={mx:.6f}@{amx} {'VIOLATION' if viol else ''}",flush=True)
