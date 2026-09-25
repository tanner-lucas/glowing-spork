# Exact arithmetic in Q(sqrt(d)), d squarefree > 1 (or d=1 meaning rational field)
from fractions import Fraction as Fr
import mpmath as mp
class QS:
    __slots__=('a','b','d')
    def __init__(s,a,b=0,d=1):
        s.a=Fr(a); s.b=Fr(b); s.d=d
        if d==1: s.a+=s.b; s.b=Fr(0)
    def _c(s,o):
        if isinstance(o,QS):
            assert o.d==s.d or o.b==0 or s.b==0, (o.d,s.d)
            return o
        return QS(o,0,s.d)
    def __add__(s,o): o=s._c(o); return QS(s.a+o.a,s.b+o.b,max(s.d,o.d) if (s.b or o.b) else s.d)
    __radd__=__add__
    def __neg__(s): return QS(-s.a,-s.b,s.d)
    def __sub__(s,o): return s+(-s._c(o))
    def __rsub__(s,o): return s._c(o)-s
    def __mul__(s,o):
        o=s._c(o); d=s.d if s.b else o.d
        return QS(s.a*o.a+s.b*o.b*d, s.a*o.b+s.b*o.a, d)
    __rmul__=__mul__
    def conj(s): return QS(s.a,-s.b,s.d)
    def norm(s): return s.a*s.a-s.b*s.b*s.d
    def inv(s):
        n=s.norm(); assert n!=0
        return QS(s.a/n,-s.b/n,s.d)
    def __truediv__(s,o): o=s._c(o); return s*o.inv()
    def __rtruediv__(s,o): return s._c(o)*s.inv()
    def sign(s):
        a,b,d=s.a,s.b,s.d
        if b==0: return (a>0)-(a<0)
        if a>=0 and b>=0: return 1 if (a>0 or b>0) else 0
        if a<=0 and b<=0: return -1
        # opposite signs: compare a^2 vs b^2 d
        if a>0: return 1 if a*a>b*b*d else -1
        return -1 if a*a>b*b*d else 1
    def __lt__(s,o): return (s-o).sign()<0
    def __le__(s,o): return (s-o).sign()<=0
    def __gt__(s,o): return (s-o).sign()>0
    def __ge__(s,o): return (s-o).sign()>=0
    def __eq__(s,o):
        try: return (s-o).sign()==0
        except Exception: return False
    def __hash__(s): return hash((s.a,s.b,s.d))
    def mpf(s): return mp.mpf(s.a.numerator)/s.a.denominator + mp.mpf(s.b.numerator)/s.b.denominator*mp.sqrt(s.d)
    def __repr__(s):
        if s.b==0: return str(s.a)
        return f"({s.a})+({s.b})*sqrt({s.d})"
def sqfree(n):
    f=1; m=n; p=2
    while p*p<=m:
        while m%(p*p)==0: m//=p*p; f*=p
        p+=1
    return f,m   # n = f^2 * m
