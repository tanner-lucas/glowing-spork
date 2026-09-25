# Verifies (1) the envelope characterization of T(i,j) on all of Z^2 in a box and
# (2) Sloane's closed form (Conjecture 2 of A360923) for i,j >= 0, against the BFS in bfs2.c.
# Usage: gcc -O2 -o bfs2 bfs2.c && ./bfs2 && python3 check2.py
import math
def Smin(i,n): return sum(max(i-k,k-n) for k in range(1,n+1))
def Smax(i,n): return sum(min(i+k,n-k) for k in range(1,n+1))
def T_char(i,j):
    n=abs(i)
    while True:
        if Smin(i,n) <= -j <= Smax(i,n): return n
        n+=1
def g(J): return 0 if J==0 else 1+math.isqrt(4*J-3)
def T_sloane(i,j):  # conjecture 2, i,j>=0
    if i==0: return g(j)
    return g(j+(i-1)*i//2)+i
bad=0; cnt=0
bfs={}
for line in open('bfs2.txt'):
    i,j,d=map(int,line.split()); bfs[(i,j)]=d
for (i,j),d in bfs.items():
    if abs(i)<=40 and abs(j)<=600:
        cnt+=1
        if T_char(i,j)!=d: bad+=1; print('char mismatch',i,j,d,T_char(i,j)) if bad<5 else None
        if i>=0 and j>=0 and T_sloane(i,j)!=d: bad+=1; print('sloane mismatch',i,j,d)
print('checked',cnt,'bad',bad)
