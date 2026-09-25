# Integer Lunar Lander: proofs of the open conjectures in OEIS A360923 / A360925

**Status of the problem before this work.** The OEIS still lists these as open, as of the snapshot of
2026-09-24:

* **A360923, Conjecture 2** (N. J. A. Sloane, Feb 25 2023). Write $t_k = k(k+1)/2$. Then
  $T(0,j) = 1+\lfloor\sqrt{4j-3}\rfloor$ for $j>0$, and $T(i,j) = T(0,\,j+t_{i-1}) + i$ for $i>0$.
* **A360925, Conjecture** (Sloane, Feb 26 2023). $a(n) = n+1+\lfloor\sqrt{2n^2-2n-3}\rfloor$ for $n\ge 2$.
  Sloane also asked: "Are all the differences after the start either 2 or 3?"
* **A360923, Conjecture 1** (Sloane, Feb 25 2023; refined by M. F. Hasler, Feb 27 2023). $T(i,j)$ differs
  from each of its eight neighbours by at most 3. The only exception is the pair $(1,0),(2,1)$.
* **A360923, open question.** "Are any of the numbers different if crashes are forbidden?"
* **A360923, suggestion.** "Solution lengths for the corresponding game on triples would be interesting
  for (0,0,n) or (n,0,0)."

The rest-to-rest case $T(0,j)=\lceil 2\sqrt j\rceil$ (A360924) was already known: Casteigts, Raffinot and
Schoeters (2020), cited in A360924. This note proves the general case and settles every item above.
It also computes the three-dimensional ("triples") version, which is new.

## The game

A position is $(i,j)\in\mathbb Z^2$: velocity $i$ and altitude $j$. A move picks $a\in\{-1,0,1\}$ and goes
to $(i+a,\; j+i+a)$, so the velocity changes first and then the altitude changes by the new velocity.
$T(i,j)$ is the least number of moves needed to reach $(0,0)$.

## 1. Exact characterisation on all of $\mathbb Z^2$

Call $v_0,\dots,v_n$ a **slow walk** if $|v_k-v_{k-1}|\le 1$ for every $k$. An $n$-move play from $(i,j)$ is
the same thing as a slow walk $v_0=i,\dots,v_n$ of velocities, and it ends at altitude
$j+\sum_{k=1}^n v_k$. So

$$ n \text{ moves suffice} \iff \exists \text{ slow walk } i=v_0,\dots,v_n=0 \text{ with } \textstyle\sum_{k=1}^n v_k = -j. $$

**Lemma 1 (envelopes).** Suppose $n\ge|i|$ and $v$ is a slow walk from $i$ to $0$ of length $n$. Then
$L_k\le v_k\le U_k$, where $L_k=\max(i-k,\,k-n)$ and $U_k=\min(i+k,\,n-k)$. Both $L$ and $U$ are
themselves slow walks from $i$ to $0$.

*Proof.* A slow walk changes by at most 1 per step, so $|v_k-i|\le k$ and $|v_k-0|\le n-k$. $L$ and $U$
are the pointwise max and min of two lines with slopes $\pm1$. Their increments therefore lie in
$\{-1,0,1\}$. Their endpoints are $i$ and $0$ because $n\ge|i|$. $\square$

**Lemma 2 (every intermediate sum occurs).** The sums $\sum_{k\ge1}v_k$ over all slow walks from $i$
to $0$ of length $n\ge|i|$ form exactly the integer interval $[\Sigma L,\ \Sigma U]$.

*Proof.* Let $v\ne L$ be such a walk and let $D=\{k: v_k>L_k\}$; the endpoints are not in $D$. Pick
$k\in D$ with $v_k$ as large as possible, and lower $v_k$ by 1. Each neighbour $v_{k\pm1}$ is at least
$v_k-1$ by slowness. It is also at most $v_k$: if the neighbour is in $D$, this holds by the choice of
$k$. If it is not in $D$, it equals $L_{k\pm1}\le L_k+1\le v_k$. So the lowered sequence is still a slow
walk, it still lies above $L$, and its sum is exactly one less. Repeating this from $U$ down to $L$
passes through every integer sum in between. $\square$

**Theorem 1.** For all $(i,j)\in\mathbb Z^2$,
$$T(i,j)=\min\{\,n\ge|i| \;:\; \Sigma L^{(i,n)}\le -j\le \Sigma U^{(i,n)}\,\}.$$
For $i\ge0$ and $n\ge i$ the envelope sums are
$$\Sigma L^{(i,n)} = t_{i-1}-\Big\lfloor \tfrac{(n-i)^2}{4}\Big\rfloor,\qquad
  \Sigma U^{(i,n)} = \tbinom n2-\Big\lfloor\tfrac{(n-i-1)^2}{4}\Big\rfloor .$$
The case $i<0$ follows from the symmetry $T(i,j)=T(-i,-j)$.

*Proof of the sums.* For $k\le i$ we have $L_k=i-k$, because $2k\le 2i\le i+n$; these terms add up to
$t_{i-1}$. For $k=i+m$ with $1\le m\le M:=n-i$ we have $L_k=\max(-m,\,m-M)$, which adds up to
$-\sum_m\min(m,M-m)=-\lfloor M^2/4\rfloor$. For the upper sum,
$\sum_k\min(i+k,n-k)=\binom n2-\sum_{k\ge1}\max(0,M-2k)=\binom n2-\lfloor (M-1)^2/4\rfloor$. $\square$

*Machine check.* Theorem 1 agrees with a brute-force BFS of the game at every one of the 97,281
positions with $|i|\le 40$, $|j|\le 600$, including negative velocities and altitudes. The code is in
`bfs2.c` and `check2.py`.

## 2. Conjecture 2 of A360923 and the formula in A360925 are true

**Theorem 2.** For $i,j\ge0$,
$$T(i,j) = i + g\big(j+t_{i-1}\big),\qquad g(0)=0,\quad g(J)=\lceil 2\sqrt J\,\rceil = 1+\lfloor\sqrt{4J-3}\rfloor\ (J\ge1).$$
In particular, $T(0,j)=1+\lfloor\sqrt{4j-3}\rfloor$ for $j>0$ and $T(i,j)=T(0,j+t_{i-1})+i$, which is
Sloane's Conjecture 2. Setting $j=0$ gives $T(n,0)=n+1+\lfloor\sqrt{2n^2-2n-3}\rfloor$ for $n\ge2$, which
is the conjecture in A360925.

*Proof.* Take $i,j\ge0$ and $n\ge i$. Every $U_k\ge0$, so $-j\le 0\le\Sigma U$ always holds. The only
binding condition in Theorem 1 is therefore $t_{i-1}-\lfloor (n-i)^2/4\rfloor\le -j$, which says
$\lfloor M^2/4\rfloor\ge J:=j+t_{i-1}$ with $M=n-i$. Since $J$ is an integer, this is equivalent to
$M^2\ge 4J$. The least such $M$ is $\lceil 2\sqrt J\rceil$.

It remains to check $\lceil2\sqrt J\rceil=1+\lfloor\sqrt{4J-3}\rfloor$. The right side is the least
integer $m$ with $m^2\ge 4J-2$. Squares are $0$ or $1\pmod 4$, so no square equals $4J-2$ or $4J-1$.
Hence $m^2\ge 4J-2$ is equivalent to $m^2\ge 4J$. $\square$

**Interpretation.** One optimal strategy is always "brake to zero velocity first, then do the optimal
rest-to-rest landing from wherever you are." The braking phase is forced to be the start of the
lower envelope $L$.

## 3. Sloane's question on A360925: the differences are always 2 or 3

We have $a(n)=T(n,0)=n+g(t_{n-1})$, so $a(n+1)-a(n)=1+g(t_n)-g(t_{n-1})$. Since $t_n-t_{n-1}=n$,

$$2\sqrt{t_n}-2\sqrt{t_{n-1}} = \frac{2n}{\sqrt{t_n}+\sqrt{t_{n-1}}}\in\Big(\sqrt{\tfrac{2n}{n+1}},\ \sqrt{\tfrac{2n}{n-1}}\Big)\subset(1,2]\quad (n\ge2).$$

A difference of ceilings is an integer strictly between (real difference) $-1$ and (real difference)
$+1$, so it lies in $\{1,2\}$. Hence $a(n+1)-a(n)\in\{2,3\}$ for all $n\ge2$. The proportion of 3s tends
to $\sqrt2-1$; numerically it is 0.41422 over the first $2\cdot10^5$ terms.

## 4. Conjecture 1 of A360923 is true, with exactly one exceptional pair

**Theorem 3.** On $i,j\ge0$, two 8-neighbours differ in $T$ by more than 3 only for the pair
$\{(1,0),(2,1)\}$, where $T=1$ and $T=5$.

*Proof.* Write $J=j+t_{i-1}$. Every neighbour difference is one of the following:
* $T(i,j+1)-T(i,j)=g(J+1)-g(J)\in[0,2]$;
* $T(i+1,j)-T(i,j)=1+g(J+i)-g(J)$;
* $T(i+1,j+1)-T(i,j)=1+g(J+i+1)-g(J)=:\Delta$;
* the anti-diagonal $T(i+1,j)-T(i,j+1)=1+g(J+i)-g(J+1)$. This lies in $[-1,1]$ when $i=0$ and in $[1,\Delta]$ when $i\ge1$.

All of these lie in $[-1,\max(2,\Delta)]$, so it is enough to show $\Delta\le3$. For $J\ge1$, the
bound $\lceil x\rceil-\lceil y\rceil<x-y+1$ gives
$$g(J+i+1)-g(J) < \frac{2(i+1)}{\sqrt{J+i+1}+\sqrt J}+1 < \frac{i+1}{\sqrt J}+1 .$$
This is $<3$, hence $\le2$, whenever $(i+1)^2\le 4J$. Since $J\ge t_{i-1}$, that holds for every $i\ge5$
because $2i(i-1)\ge(i+1)^2$. It also holds for $i\le4$ once $j\ge7$. The finitely many remaining cells
($i\le4$, $j\le6$) were checked by computer; in fact the whole region $i,j<1500$ was checked
(`conj1.py`). Only the pair above violates the bound. $\square$

## 5. Crashes are never needed

**Theorem 4.** From every start $(i,j)$ with $j\ge0$ from which a soft landing is possible, some
*optimal* play never goes below altitude 0. Therefore forbidding crashes changes no value of $T$.
Soft landing is possible exactly when $j\ge0$ and, if $i<0$, also $j\ge t_{|i|-1}$.

*Proof.* **Case $i\ge0$.** Let $n=T(i,j)$ and $M=n-i$. Brake for $i$ moves, climbing to altitude
$j+t_{i-1}$ with velocity 0. Next we need a slow walk from 0 to 0 of length $M$ whose values are all
$\le0$ and whose sum is exactly $-(j+t_{i-1})$. Run the lowering argument of Lemma 2 between the zero
walk and $L$; both are $\le0$, and so is every walk in between. This produces every sum in
$[-\lfloor M^2/4\rfloor,0]$, which contains $-(j+t_{i-1})$. The altitude then only decreases, from
$j+t_{i-1}$ to 0, so it never goes negative.

**Case $i<0$.** Every slow walk from $i$ with all values $\le0$ has sum at most
$-t_{|i|-1}$, with equality for the fastest braking. Lemma 2 applied between $L$ and the walk
$\min(i+k,0)$ shows that non-positive walks realise every sum in $[\Sigma L,\,-t_{|i|-1}]$. If
$j\ge t_{|i|-1}$, then $-j$ lies in this range at $n=T(i,j)$, so an optimal play exists whose altitude
decreases monotonically to 0. If $j<t_{|i|-1}$, even maximal braking hits the ground first. $\square$

## 6. The game on triples (new sequences)

A position is now $(a,v,h)$: acceleration, velocity, altitude. A move picks $\delta\in\{-1,0,1\}$ and
sets $a\mathrel{+}=\delta$, then $v\mathrel{+}=a$, then $h\mathrel{+}=v$. Write $T_3$ for the least
number of moves to reach the origin.

As in Section 1, $N$ moves suffice from $(a_0,v_0,h_0)$ exactly when there is a slow walk
$a_0,\dots,a_N=0$ with
$$\textstyle\sum_{k=1}^N a_k=-v_0\quad\text{and}\quad\sum_{k=1}^N k\,a_k=h_0-v_0 .$$
`dp3.c` and `dp3g.c` decide this exactly with a bitset DP. `bfs3.c` is an independent brute-force BFS
over the state space, and it agrees on every value it can reach.

**$T_3(0,0,n)$**, landing from rest at altitude $n$. It is exact for $0\le n\le 1912$ (DP) and
cross-checked by BFS for $n\le200$:

    0, 8, 4, 5, 6, 7, 6, 7, 7, 8, 8, 9, 8, 9, 9, 9, 8, 10, 9, 10, 9, 10, 10, 11, 10, 10, 10, 11, 11, 11,
    10, 11, 11, 11, 11, 12, 11, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 12, 13, 13, 13, 13, 13, 12, ...

Unlike the 2-D game, this sequence is **not monotone**. Landing from altitude 1 takes 8 moves, but
landing from altitude 2 takes only 4: $\delta=-1,+1,+1,-1$. The underlying reason is that the set of
altitudes that can be landed in exactly $N$ moves is not an interval. It has holes just below its
maximum (see `seq3.py`).

**A combinatorial reformulation.** Write the jerks as $\delta_1,\dots,\delta_N\in\{-1,0,1\}$ and
reverse time, $r=N+1-m$. Then the three landing conditions become $\sum\delta'_r=0$,
$\sum r\,\delta'_r=0$ and $\sum r^2\delta'_r=-2n$. Setting $P=\{r:\delta'_r=-1\}$ and
$M=\{r:\delta'_r=+1\}$:

> $T_3(0,0,n)$ is the least $N$ for which there are disjoint $P,M\subseteq\{1,\dots,N\}$ with
> $|P|=|M|$, $\sum P=\sum M$ and $\sum_{x\in P}x^2-\sum_{x\in M}x^2 = 2n$.

This is a signed version of the degree-2 Prouhet–Tarry–Escott problem. For example, $n=2$ with $N=4$
uses $P=\{1,4\}$ and $M=\{2,3\}$. In the same language the 2-D game says $T(0,j)$ is the least $N$ with
$|P|=|M|$ and $\sum P-\sum M=j$.

**Maximum landable altitude in exactly $N$ moves.** The DP gives $M_N$ for $1\le N\le 36$:

    0, 0, 0, 2, 3, 6, 8, 16, 20, 30, 36, 54, 63, 84, 96, 128, 144, 180, 200, 250, 275, 330, 360, 432, ...

**Theorem 5.** $M_{4k}=2k^3$ and $M_{4k+2}=k(k+1)(2k+1)$.

*Proof.* Let $Q(P,M)=\sum_P x^2-\sum_M x^2$. When $|P|=|M|$ and $\sum P=\sum M$, the linear and
constant parts of $(x-c)^2$ cancel, so $Q(P,M)=\sum_P f-\sum_M f$ with $f(x)=(x-c)^2$ for **any**
real $c$. Drop the constraint $\sum P=\sum M$ and keep only disjointness and $|P|=|M|$. By
rearrangement, the maximum of $\sum_P f-\sum_M f$ is $\sum_i\max\big(0,\ f_{(N+1-i)}-f_{(i)}\big)$,
where $f_{(1)}\le\dots\le f_{(N)}$ are the sorted values; this is an upper bound for $Q$.

Take $N$ even and $c=(N+1)/2$. The values $|x-c|$ are $\tfrac12,\tfrac32,\dots,\tfrac{N-1}2$, each
taken twice. The bound is attained by $P$ = the $x$ with $|x-c|$ in the upper half of these values and
$M$ = the lower half. If $N\equiv2\pmod4$, the two points at the median distance are left out; they
contribute 0. This $P$ and $M$ are symmetric about $c$, so $\sum P=\sum M$ holds automatically. Hence
the bound is exact.

Summing $\sum_{j<n}(j+\tfrac12)^2=n(4n^2-1)/12$ over the two halves gives $Q=4k^3$ for $N=4k$ and
$Q=2k(k+1)(2k+1)$ for $N=4k+2$. Finally $M_N=Q/2$. $\square$

For odd $N$ the same bound leaves a small gap, so it cannot be used directly. The DP matches
$$M_{4k+1}=k^2(2k+1),\qquad M_{4k+3}=2k(k+1)^2$$
for every odd $N\le 35$; this remains conjectural. Either way $M_N\sim N^3/32$, matching the
continuous bang-bang optimum (jerk pattern $+1,-1,-1,+1$ with distance $2\tau^3$ over time $4\tau$).
It gives the lower bound $T_3(0,0,n)\gtrsim(32n)^{1/3}$.

Neither these sequences nor $T_3(n,0,0)$ and $T_3(0,n,0)$ appear in the OEIS as of the 2026-09-24
snapshot. The first terms of those two are in `RESULTS-3D.md`.
