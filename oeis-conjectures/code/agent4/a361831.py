import sys, gmpy2
sys.setrecursionlimit(10000)
def ok(k):
    while k%3==0: k//=3
    return k==1 or gmpy2.is_prime(k)
def first(n):
    L=(n+8)//9
    while True:
        # lexicographic enumeration of L-digit strings with digit sum n, leading digit>=1
        res=None
        def rec(pos, rem, val):
            nonlocal res
            left=L-pos
            if left==0:
                if rem==0 and ok(val): res=val; return True
                return False
            lo=1 if pos==0 else 0
            for d in range(max(lo, rem-9*(left-1)), min(9,rem)+1):
                if rec(pos+1, rem-d, val*10+d): return True
            return False
        if rec(0,n,0): return res
        L+=1
N=int(sys.argv[1])
vals=[first(n) for n in range(2,N+1)]
print(vals[:23])
bad9=[(n,v%10) for n,v in zip(range(2,N+1),vals) if n>25 and v%10!=9]
badz=[n for n,v in zip(range(2,N+1),vals) if '0' in str(v)]
print('n>25 with a(n) not ending in 9:',bad9[:20])
print('terms containing 0:',badz[:20])
