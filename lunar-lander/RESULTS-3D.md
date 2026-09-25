# 3-D Integer Lunar Lander: new sequences

A position is (a, v, h): acceleration, velocity, altitude. A move picks d in {-1,0,1} and sets
a += d, then v += a, then h += v. Each sequence below gives the least number of moves to reach (0,0,0).

## T3(0,0,n): landing from rest at altitude n
Exact for n = 0..1912 by the bitset DP (`dp3.c`, `seq3.py`), and independently confirmed by BFS
(`bfs3.c`) for n <= 200. Full list: `T3_rest_to_rest_n0-1912.txt`.

0, 8, 4, 5, 6, 7, 6, 7, 7, 8, 8, 9, 8, 9, 9, 9, 8, 10, 9, 10, 9, 10, 10, 11, 10, 10, 10, 11, 11, 11, 10, 11, 11, 11, 11, 12, 11, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 12, 13, 13, 13, 13, 13, 12, 14, 13, 13, 13, 13, 13, 14, 14, 13, 14, 14, 14, 14, 14, 14, 14, 15, 14, 15, 14, 15, 14, 14, 14, 15, 15, 15, 15, 15, 14, 15, 15, 15, 15, 15, 15, 16, 15, 15, 16, 16, 15, 16, 16, 16, 16, ...

## T3(n,0,0): starting at the origin with acceleration n
From BFS over two different state boxes, (|a|,|v|,|h|) <= (30,400,3000) and (40,700,6000). Both boxes
give identical values. The exact DP (`dp3g.c`, mode 1) confirms n <= 12.

0, 1, 7, 13, 17, 22, 26, 30, 34, 39, 43, 48, 52, 57, 60, 65, 69, 74, 78, 83, 87, 91

## T3(0,n,0): starting at the origin with velocity n
From BFS over the same two boxes, which again agree.

0, 2, 7, 6, 9, 9, 11, 12, 12, 12, 14, 13, 14, 15, 16, 16, 16, 17, 17, 18, 18, 19, 20, 20, 20, 21, 22, 21, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 26, 26, 26, 26, 27, 27, 28, 27, 28, 28, 29, 29, 30, 29, 30, 30, 30, 31, 31, 31, 31, 32, 32

## Max altitude M_N landable from rest to rest in exactly N moves (N = 1..36)
0, 0, 0, 2, 3, 6, 8, 16, 20, 30, 36, 54, 63, 84, 96, 128, 144, 180, 200, 250, 275, 330, 360, 432, 468,
546, 588, 686, 735, 840, 896, 1024, 1088, 1224, 1296, 1458

Proved for even N (Theorem 5 in README.md). Conjectured for odd N: M_(4k+1) = k^2(2k+1) and
M_(4k+3) = 2k(k+1)^2.
