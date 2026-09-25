import numpy as np, sys, math
def apply(w, imgs):
    lens = np.array([len(im) for im in imgs])
    L = lens[w]
    off = np.zeros(len(w)+1, dtype=np.int64); np.cumsum(L, out=off[1:])
    out = np.empty(off[-1], dtype=np.uint8)
    for j in range(max(lens)):
        mask = L > j
        vals = np.array([im[j] if len(im)>j else 0 for im in imgs], dtype=np.uint8)
        idx = off[:-1][mask] + j
        out[idx] = vals[w[mask]]
    return out
def gen(imgs, start, parity, N):
    # iterate from [start]; keep iteration count parity == parity (0 or 1) at the end
    w = np.array([start], dtype=np.uint8); it = 0
    while len(w) < N or it % 2 != parity:
        w = apply(w, imgs); it += 1
    return w[:N]
def fib_word(N):
    return gen([[0,1],[0]], 0, None if False else 0, N) if False else None
