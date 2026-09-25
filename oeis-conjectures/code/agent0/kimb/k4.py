from mpmath import mp, sqrt, nstr
import importlib.util, sys, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import exactdp
mp.dps=80
res=exactdp.analyze("10","0010",('lim',0),0,(3+sqrt(3))/3)
print("A285140 (letter0, r=(3+sqrt3)/3) inf",nstr(res[-1][2],12),"sup",nstr(res[-1][3],12))
