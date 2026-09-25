from fractions import Fraction as F
M=[0, 0, 0, 2, 3, 6, 8, 16, 20, 30, 36, 54, 63, 84, 96, 128, 144, 180, 200, 250, 275, 330, 360, 432, 468, 546, 588, 686, 735, 840, 896, 1024, 1088, 1224, 1296, 1458]
def formula(N):
    k,r=divmod(N,4)
    return [2*k**3, k*k*(2*k+1), k*(k+1)*(2*k+1), 2*k*(k+1)**2][r]
def B(N,c):
    f=sorted(((x-c)**2 for x in range(1,N+1)))
    tot=0
    for i in range(N//2):
        g=f[N-1-i]-f[i]
        if g>0: tot+=g
    return tot
for N in range(1,37):
    best=min(B(N,F(t,4)) for t in range(0,4*N+5))
    print(N, M[N-1], formula(N), best/2, 'tight' if best/2==M[N-1] else 'GAP')
