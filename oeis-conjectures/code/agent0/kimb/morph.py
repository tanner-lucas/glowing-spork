import numpy as np, sys
def iterate(img0, img1, start, steps):
    w = np.array([start], dtype=np.uint8)
    i0 = np.array([int(c) for c in img0], dtype=np.uint8)
    i1 = np.array([int(c) for c in img1], dtype=np.uint8)
    for _ in range(steps):
        lens = np.where(w==0, len(i0), len(i1))
        out = np.empty(lens.sum(), dtype=np.uint8)
        pos = np.concatenate(([0], np.cumsum(lens)[:-1]))
        for letter, img in ((0,i0),(1,i1)):
            idx = pos[w==letter]
            for j,c in enumerate(img):
                out[idx+j] = c
        w = out
    return w
def positions(w, letter):  # 1-indexed
    return np.nonzero(w==letter)[0] + 1
