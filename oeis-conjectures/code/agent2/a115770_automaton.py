# Decide whether {k : 7k = 11 (x) k} == {k : 5k = 13 (x) k}, where (x) is carryless (GF(2)[x]) multiplication.
# General method: for odd a, b: condition a*k == b (x) k. Read bits of k LSB-first; state = (carry, last W bits of k).
# Bit i of a*k: (sum_{j in bits(a)} k_{i-j} + carry) mod 2, new carry = floor(.../2).
# Bit i of b (x) k: XOR_{j in bits(b)} k_{i-j}.
from collections import deque
def make(a,b):
    A=[j for j in range(a.bit_length()) if a>>j&1]; B=[j for j in range(b.bit_length()) if b>>j&1]
    W=max(max(A),max(B))
    def step(state,bit):
        c,hist=state   # hist: tuple of previous W bits, hist[0]=k_{i-1}
        bits=(bit,)+hist  # bits[j] = k_{i-j}
        s=sum(bits[j] for j in A)+c
        lhs=s&1; rhs=0
        for j in B: rhs^=bits[j]
        if lhs!=rhs: return None
        return (s>>1, bits[:W])
    init=(0,(0,)*W)
    return step,init
def accepting(step,state,memo):
    # accept iff feeding zeros forever never fails; zeros lead eventually to a cycle; carry bounded -> finite
    if state in memo: return memo[state]
    seen=set(); s=state
    while s is not None and s not in seen:
        seen.add(s); s=step(s,0)
    res = s is not None  # entered a cycle without failure
    memo[state]=res; return res
def compare(a1,b1,a2,b2,maxwitness=5):
    st1,i1=make(a1,b1); st2,i2=make(a2,b2); m1={}; m2={}
    # states may be None (dead)
    start=(i1,i2,0,0)  # pair + value of k so far + length (for witness)
    seen={(i1,i2)}; dq=deque([(i1,i2,0,0)]); diffs=[]
    while dq:
        s1,s2,val,ln=dq.popleft()
        acc1 = s1 is not None and accepting(st1,s1,m1)
        acc2 = s2 is not None and accepting(st2,s2,m2)
        if acc1!=acc2: diffs.append((val,acc1,acc2));
        if len(diffs)>=maxwitness: break
        for bit in (0,1):
            n1 = st1(s1,bit) if s1 is not None else None
            n2 = st2(s2,bit) if s2 is not None else None
            if n1 is None and n2 is None: continue
            if (n1,n2) not in seen:
                seen.add((n1,n2)); dq.append((n1,n2,val|(bit<<ln),ln+1))
    return seen,diffs
seen,diffs=compare(7,11,5,13)
print("reachable product states:",len(seen)," differing (k, acc1, acc2):",diffs)
# sanity: brute force comparison of the automaton language vs direct definition
def clmul(a,b):
    r=0
    while b:
        if b&1: r^=a
        a<<=1; b>>=1
    return r
def in_lang(a,b,k):
    st,s=make(a,b); m={}
    x=k
    while x:
        s=st(s,x&1); x>>=1
        if s is None: return False
    return accepting(st,s,m)
for (a,b) in [(7,11),(5,13)]:
    bad=[k for k in range(1<<16) if in_lang(a,b,k)!=(a*k==clmul(b,k))]
    print((a,b),"automaton vs direct mismatches for k<2^16:",bad[:5])
S=[k for k in range(1<<12) if 7*k==clmul(11,k)]; T=[k for k in range(1<<12) if 5*k==clmul(13,k)]
print(S[:20]); print(S==T)
def charset(k):
    if k==0: return True
    while k%2==0: k//=2
    return (k+1)&k==0 and k>=7
bad=[k for k in range(1<<22) if (7*k==clmul(11,k))!=charset(k)]
print("characterization {0} U {2^a(2^b-1): b>=3} mismatches below 2^22:",bad[:5])
