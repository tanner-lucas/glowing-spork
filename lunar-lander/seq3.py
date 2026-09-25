import subprocess
T={}
for N in range(0,41):
    if N==0: s={0}
    else:
        out=subprocess.run(['./dp3',str(N)],capture_output=True,text=True).stdout.split()
        s=set(map(int,out))
    for n in s:
        if n not in T: T[n]=N
    mx=max(s)
    print(N, mx, flush=True) if N%5==0 else None
lim=max(n for n in range(100000) if all(m in T for m in range(n+1)))
print('complete up to',lim)
print([T[n] for n in range(0,min(lim,120)+1)])
open("t3_00n.txt","w").write('\n'.join(f"{n} {T[n]}" for n in range(lim+1)))
