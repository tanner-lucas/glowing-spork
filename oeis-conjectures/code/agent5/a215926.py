from sympy import divisor_sigma as sg
def brute(n):
    k=1
    while True:
        if sg(k)<2*k and sg(k*n)>=2*k*n: return k
        k+=1
def pred(n):
    if sg(n)>=2*n: return 1
    if n%2==0: return 2 if sg(2*n)>=4*n else 3
    j=0
    while sg(2**j*n) < 2*2**j*n: j+=1
    return 2**j
bad=[n for n in range(2,6001) if brute(n)!=pred(n)]
print("mismatches up to 6000:",bad[:10])
# data check
txt=open('/home/user/work/oeisdata/seq/A215/A215926.seq').read()
dat=[int(x) for x in ''.join(l.split(' ',2)[2].strip() for l in txt.splitlines() if l[:2] in ('%S','%T','%U')).split(',') if x]
print("data match:", [pred(n) for n in range(2,2+len(dat))]==dat)
