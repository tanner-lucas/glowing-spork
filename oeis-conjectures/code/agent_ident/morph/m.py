import sys
def iterate(rules, start, n, parity=None):
    # returns prefix of length >= n of lim sigma^(k)(start), k of given parity class, using fixed point of sigma^2 if needed
    w=start
    it=0
    while True:
        w2=''.join(rules[c] for c in w)
        it+=1
        if len(w2)>=n and it%2==0 and w2.startswith(start) : return w2[:n]
        w=w2
        if len(w)>50*n: return None
def lim(rules,start,n):
    # limit of sigma^{2k}(start)
    s2={c:''.join(rules[d] for d in rules[c]) for c in rules}
    w=start
    while len(w)<n:
        w=''.join(s2[c] for c in w)
    return w[:n]
def fixed(rules,start,n):
    w=start
    while len(w)<n: w=''.join(rules[c] for c in w)
    return w[:n]
N=2000000
def seqstr(s): return [int(c) for c in s]
# A284674 / A284677 : 0->1, 1->0111
R={'0':'1','1':'0111'}
W0=seqstr(lim(R,'0',N)); W1=seqstr(lim(R,'1',N))
print("A284674",W0[:20]); print("A284677",W1[:20])
# conjecture A284677(n) = A284674(n-1) (1-indexed)
fail=[n for n in range(2,N) if W1[n-1]!=W0[n-2]][:5]; print("A284677(n)=A284674(n-1) first fails:",fail)
fail2=[n for n in range(3,N+1) if W1[n-1]!=W0[n-1]][:5]; print("A284677(n)=A284674(n), n>=3 fails:",fail2)
# A284948: 1-limiting of 0->10,1->00 ; A096268 period doubling fixed pt 0->01,1->00 offset 0
R={'0':'10','1':'00'}
V1=seqstr(lim(R,'1',N)); PD=seqstr(fixed({'0':'01','1':'00'},'0',N))
print("A284948",V1[:20]); print("A096268",PD[:20])
fail=[n for n in range(2,N) if V1[n-1]!=PD[n-2]][:5]; print("A284948(n)=A096268(n-2) fails:",fail)
# A285076: 1-limiting of 0->10,1->010 ; A285073 0-limiting
R={'0':'10','1':'010'}
U1=seqstr(lim(R,'1',N)); U0=seqstr(lim(R,'0',N))
print("A285076",U1[:20]); print("A285073",U0[:20])
fail=[n for n in range(3,N+1) if U1[n-1]!=U0[n-1]][:5]; print("A285076(n)=A285073(n) n>=3 fails:",fail)
# A285358 fixed pt 0->10,1->1101 starting with 1; A284929 fixed pt 0->01, 1->1011 starting 0
X=seqstr(fixed({'0':'10','1':'1101'},'1',N)); Y=seqstr(fixed({'0':'01','1':'1011'},'0',N))
print("A285358",X[:20]); print("A284929",Y[:20])
fail=[n for n in range(1,N-1) if X[n-1]!=Y[n]][:5]; print("A285358(n)=A284929(n+1) fails:",fail)
# A285383 limiting 0-word of 0->11,1->01 ; A035263 fixed pt of 0->11? trajectory of 1 under 0->11,1->10
R={'0':'11','1':'01'}
Z0=seqstr(lim(R,'0',N)); T=seqstr(fixed({'0':'11','1':'10'},'1',N))
print("A285383",Z0[:20]); print("A035263",T[:20])
fail=[n for n in range(2,N) if Z0[n-1]!=T[n-2]][:5]; print("A285383(n)=A035263(n-1) fails:",fail)
