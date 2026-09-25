# Slice 0: results (agent 0)

Work directory: `/home/user/work/agent0/`. Every counterexample below was reproduced by at least two independent
implementations. Each implementation first reproduced the entry's own data. I grepped the local OEIS snapshot
for prior mentions, and in a few cases also ran a web search. Items are ordered by strength. "Bonus" items are
entries outside slice 0 that fell out of the same computation.

---------------------------------------------------------------------------------------------------------

## 1. A073631 / A130058: COUNTEREXAMPLE

* **Conjecture.** In A073631 (Benoit Cloitre) and A130058 (Alexander Adamchuk, May 04 2007): "Conjecture: All
  nonsquarefree terms of A073631 are the multiples of 23^2." A073631 also says: "It appears that a(1) = 1 and
  a(4) = 529 = 23^2 are the only perfect squares."
  A073631 is the list of nonprime k with k | 3^(k-1) - 2^(k-1).
* **Certificate.** Let p = 3842760169 (prime) and k = p^2 = 14766805716452908561.
  * p^2 divides 3^(p-1) - 2^(p-1). So p is a base-3/2 Wieferich prime; it is term a(2) of A376896 (Jianing Song,
    Oct 2024).
  * (3/2)^(p-1) = 1 mod p^2, and p-1 divides k-1 = (p-1)(p+1). Hence k | 3^(k-1) - 2^(k-1), so k is in A073631.
  * k is not squarefree, and k mod 529 = 349, so 23^2 does not divide k. k is also a perfect square other than
    1 and 529.
  * One-line GP check: `p=3842760169; k=p^2; Mod(3,k)^(k-1)==Mod(2,k)^(k-1) && k%529` returns 1 and 349.
* **Why it is the smallest counterexample.**
  * Suppose q^2 | k for a term k. Then q > 3. The order of 3/2 mod q^2 divides k-1, and q does not divide k-1.
    So (3/2)^(q-1) = 1 mod q^2, i.e. q is a base-3/2 Wieferich prime. So every nonsquarefree term is divisible by
    p^2 for some such prime p.
  * My own search (Montgomery arithmetic, all 189,961,810 primes below 4·10^9) finds only 23 and 3842760169.
    So 3842760169^2 is the smallest nonsquarefree term of A073631 that is not a multiple of 23^2.
  * v_23((3/2)^22 - 1) = 2, so 23^4 is not a term. So 3842760169^2 is also the third perfect-square term, after
    1 and 529.
* **Verification.** PARI (`a073631/v.gp`), Python `pow` / sympy, and C `a073631/wief.c` (output in
  `a073631/run4e9.txt`).
* **Novelty.** The consequence is not recorded in A073631 or A130058. Neither entry cross-references A376896,
  and A376896 is referenced by no other entry. A web search found no mention.

## 2. A376360: COUNTEREXAMPLE (and a structural disproof of the whole family)

* **Conjecture.** "Conjecture: {a(n+1) - a(n) : n >= 1} = {4,5,6,7,8,9,10,11,13}. It has been checked that
  a(n+1) - a(n) is not 12 for 1<=n<=300000." A376360 lists the positions of numbers whose greedy
  representation in base of squares (A007961) ends in 3.
* **Certificate.**
  * a(65603) = 336391 = 579^2 + 33^2 + 7^2 + 3^2 + 3·1, which ends in 3.
  * a(65604) = 336403 = 580^2 + 3, which ends in 3.
  * None of 336392..336402 ends in 3.
  * So the difference 12 occurs, at an index within the range the entry says was checked.
  * Further differences: 14 at a(361753) = 1830598, and 16 at a(362286) = 1833303 → 1833319.
* **Verification.** Three independent implementations, each reproducing the data first:
  * C greedy brute force, `a376360/t.c`;
  * Python with exact `isqrt`, `a376360/big.py`;
  * PARI greedy digit vector, `a376360/v.gp`.
* **Why the gaps are unbounded.**
  * For n in [s^2, (s+1)^2) with s >= 3, the greedy digit at s^2 is 1. So last(n) = last(n - s^2), with
    n - s^2 in [0, 2s].
  * Hence the gaps inside block s repeat earlier gaps. The gap across blocks is 2s + 1 + m0 - t. Here t is the
    largest earlier element <= 2s, and m0 is the smallest m with last digit c (m0 = c).
  * A gap g whose right end is odd therefore produces a later gap g + m0.
  * So for final digits 1, 2 and 3 the gaps are unbounded. For final digit 0 they are bounded.
  * The same argument applies to the triangular base (A000462), with block [T_k, T_{k+1}) and cross gap
    k + 1 + m0 - t.
* **Bonus counterexamples (same family, not in my slice).** Each was verified by C and by exact Python
  (`a376360/t.c`, `big.py`, `tri.py`):
  * A376355 ({2..6} conjectured): gap 7 from 2598054 to 2598061.
  * A376356 ({3..9} conjectured): gap 10 from 5256895 to 5256905.
  * A376358 ({2..7} conjectured): gap 8 from 7789633076174397 to 7789633076174405 (built with the recursion,
    checked directly).
  * A376359 ({3..10} conjectured): gap 12 from 18819188658570294 to 18819188658570306.
* **Proof for A376354 (in my slice).** Conjecture: {a(n+1)-a(n)} = {1,2,3}, for triangular base, final digit 0.
  * Let S = {n >= 0 : last(n) = 0}. The elements of S in [T_k, T_{k+1}) are T_k + (S ∩ [0,k]).
  * By induction S ∩ [0,T_k] has all gaps <= 3 and contains T_k > k. Hence max(S ∩ [0,k]) = M >= k-2.
  * The cross gap T_{k+1} - (T_k + M) = k + 1 - M is therefore <= 3.
  * The gaps 1, 2 and 3 all occur (9→10, 13→15, 3→6). So the set of differences is exactly {1,2,3}.
  * The same argument proves A376357 ({1,2,3,4}, squares base, final digit 0).

## 3. A289035 and A289239: COUNTEREXAMPLE (also refutes A289001, A289242 and A289004)

* **Conjecture.** "Conjecture: the number of letters (0's and 1's) in the n-th iterate of the mapping is given
  by A289004." A289004 is defined by a recurrence of order 10. The mappings are:
  * A289035: 00->0010, 01->010, 10->010;
  * A289239: 00->0010, 01->100, 10->010.
  * The same conjecture appears in A289001 (01->001), A289242 (01->100, 10->100), and in A289004's own comment.
    A289071's comment points to A289010, which already fails at n = 4 and is presumably a typo for A289004.
* **Certificate.** The mapping is applied with Mathematica StringReplace semantics: leftmost, non-overlapping,
  unmatched letters kept. With these semantics the iterates listed in A289001, A289035 and A289239 are
  reproduced exactly.
  * The lengths of iterates 0..21 agree with A289004.
  * Iterate 22 has **268184** letters, but A289004(22) = **268182**.
  * Later values also disagree: 457819 vs 457812, 781545 vs 781531, and so on.
  * All five mappings give identical lengths.
  * Kimberling's Mathematica only tabulated n <= 20.
* **Verification.** A C scanner (`iter/t.c`, `iter/run.py`) and an independent Python regex implementation
  (`iter/indep.py`, `iter/fam.py`).
* **Related (A288926, in my slice; A288710 bonus).** Both conjecture that the length of iterate n equals
  A288925(n) for the mapping 00->1000, 10->0001. But the entry itself lists iterate 3 as `10000100011000`,
  which has 14 letters, while A288925(3) = 13. Later lengths are 26, 48, 90 versus 26, 47, 89. So the
  conjecture is false on the entry's own data; A288925's formula belongs to some other mapping.
* **Held.** The other length conjectures agree as far as I computed:

  | Mapping (length sequence) | Iterates checked |
  |---|---|
  | A288524 (A288523) | 45 |
  | A288633 (A288465) | 31 |
  | A288668 | 45 |
  | A288732 | 101 |
  | A289107 | 38 |
  | A288932 (A123720, offset shifted by 1) | 26 |

## 4. A062854: PROOF

* **Conjecture.** "Conjecture: a(n) > n/log(n) for n > 2" (Thomas Ordowski, Jan 28 2017). Here a(n) is the
  number of new products in row n of the multiplication table.
* **Proof.**
  * For a prime p with sqrt(n) < p <= n and p ∤ n, put i = p·floor(n/p) <= n. Write m = floor(n/p) < sqrt(n) < p.
  * Suppose n·i = x·y with x, y <= n-1. Since v_p(n·i) = 1, p divides exactly one factor, say x = p·u.
  * Then u <= (n-1)/p < m+1. Also y = n·m/u <= n-1, which forces u > m. This is a contradiction, so n·i is a
    new product.
  * Different primes p give different i, because p is the largest prime factor of i.
  * At most one prime > sqrt(n) divides n. Hence a(n) >= pi(n) - pi(sqrt n) - 1.
  * Dusart (1999): pi(x) >= x/ln x·(1 + 1/ln x) for x >= 599. Rosser–Schoenfeld: pi(y) < 1.25506·y/ln y.
    Together: a(n) - n/ln n >= n/ln^2 n - 2.51012·sqrt(n)/ln n - 1 > 0 for all n >= 599. At n = 599 the right
    side is 4.04, and it increases.
  * For 3 <= n <= 20000 the inequality, and the lower bound itself, were checked by direct computation. The
    minimum of a(n)·ln(n)/n is 1.0397, at n = 4.
* **Code.** `a062854/a.c`, `a062854/check.c`, and Python `a062854/a.py`, which reproduces the data.
* **Novelty.** The entry states it only as a conjecture. I found no prior proof.

## 5. A397683 (Sep 2026, "new"): PROOF

* **Conjecture.** "for odd m, f(m) = 0 iff m is a power of 3 or a power of 7." Here f(m) counts the x for which
  x and x+1 are units with ord_m(x) = ord_m(x+1).
* **Proof.**
  * *f(3^a) = 0.* A unit pair needs x ≡ 1 (mod 3). Then ord(x) divides 3^(a-1), which is odd, while
    x+1 ≡ -1 (mod 3) has even order.
  * *f(7^b) = 0.* The prime-to-7 part of the order mod 7^b equals the order mod 7. The possible pairs
    (ord_7 x, ord_7 (x+1)) are (1,3), (3,6), (6,3), (3,6), (6,2). In each pair the 2-parts or the 3-parts differ.
  * *Prime powers p^k with p >= 5, p ≠ 7.* By Cohen (Proc. AMS 94 (1985) 605–611), F_p has consecutive
    primitive roots g, g+1 for every p other than 2, 3, 7. Exactly one lift g + tp fails to be a primitive root
    mod p^2, and likewise for g+1. With p >= 5 there is a t for which both g + tp and g + 1 + tp are primitive
    roots mod every p^k. That gives a witness with a common even order.
  * *Combining coprime moduli.* By CRT, witnesses with orders E_i combine to order lcm(E_i) for both x and x+1.
  * *m = 3^a·s or 7^b·s with gcd(s,21) = 1 and s > 1.* Take an even-order witness mod s. Mod 3^a use x ≡ 4
    (orders 3^(a-1) and 2·3^(a-1)), or x ≡ 1 when a = 1. Mod 7^b use x ≡ 3 (orders 6·7^(b-1) and 3·7^(b-1)).
    Since the order mod s is even, the lcm's agree.
  * *m = 3^a·7^b with a, b >= 1.* For a >= 2 use x ≡ 4 (mod 3^a) and x ≡ 5 (mod 7^b): both orders equal
    2·3^(a-1)·7^(b-1). For a = 1 use x ≡ 1 (mod 3) and x ≡ 3 (mod 7^b): both orders equal 6·7^(b-1).
* **Verification.**
  * The explicit witness from the proof was built and checked with znorder for every odd m <= 200001 that is not
    a power of 3 or 7.
  * f(3^k) = 0 for k <= 9 and f(7^k) = 0 for k <= 5 by brute force.
  * The data was reproduced. Code: `a397683/proof_check.gp`.

## 6. A220846: COUNTEREXAMPLE (visible in the entry's own data)

* **Conjecture.** "Conjecture: sequence is injective" (Jaroslav Krizek, Dec 2012). Here
  a(n) = Sum_{d|n} (Prod_{d|n} d)/d.
* **Certificate.**
  * a(4) = 8/1 + 8/2 + 8/4 = 14, and a(13) = 13 + 1 = 14. Both values appear in the data.
  * a(6) = a(71) = 72. Up to 20000 the collisions are (4,13), (6,71), (10,179), (15,359), (26,1091), and more.
  * In general a(pq) = pq(p+1)(q+1) and a(r) = r+1, so a collision occurs whenever pq(p+1)(q+1) - 1 is prime.
* **Verification.** Python (sympy divisors) and PARI. Code in `a220846/`.

## 7. Kimberling discrepancy conjectures on substitution words: COUNTEREXAMPLES

Violations were found directly in the data and confirmed by an exact high-precision recursion over the
substitution (`kimb/kall.py`, `kimb/exactdp.py`).

* **A285130.** Conjecture: -1 < n·r - a(n) < 3 with r = 3.5621...
  * a(2) = 3 gives 2r - 3 = 4.12 > 3. This is false for any r in [3.56, 3.57].
  * Structurally, the morphism 0->10, 1->0000 has eigenvalues (1 ± sqrt 17)/2, and |λ2| = 1.56 > 1 (not Pisot).
    So n·r - a(n) is unbounded for every r. For r = 3.5615, D(1152469) = 4009.
  * The siblings A285126, A285127 and A285129 (not in my slice) use the same morphism and are false for the same
    reason.
* **A284946.** Conjecture: -1 < n·r - a(n) < 3 with r = 2 + sqrt 2.
  * a(2) = 3 gives 2(2+√2) - 3 = 3.83.
  * The density of 1's gives r = sqrt 2, and with r = sqrt 2 the range is (-0.586, 2.414). So the constant in the
    entry is wrong.
* **A285141.** Conjecture: -1 < n·r - a(n) < 1 with r = 1 + sqrt 3, which is the correct density.
  * a(6) = 15 gives 6(1+√3) - 15 = 1.392.
  * The exact range is (-1.4226, 3.3094).
  * Bonus: A285140 ((3+√3)/3, bound (-1,1)) is violated at n = 2 (1.1547); its true range is (-1.333, 1.821).
* **Checked and holding** (Pisot cases; exact inf/sup inside the stated bounds): A026364, A045671, A283967,
  A284370, A284654, A284678, A284774, A284903, A285033, A285085, A285275, A285342, A285359, A285420.
* **A287726: PROOF (easy).**
  * a(n) = floor(n·φ^2) + 2n - 2. This holds because the {0->1, 1->011}-image of the Fibonacci word has its
    n-th 0 right after the image of the n-th 1, and the 1's of A003849 sit at A001950(n) - 1.
  * Hence n·r - a(n) = 2 + {n·φ^2}, which lies in (2,3).

## 8. A327138: COUNTEREXAMPLE (trivial)

* **Conjecture.** "2.07 < n*Pi - a(n) < 3.08 for n >= 1."
* **Certificate.** a(1) = 2 gives π - 2 = 1.14. Also a(5) = 12 gives 5π - 12 = 3.71.
* **Why it fails.** The sequence {k : cos 2k < cos(2k+2)} = {k : sin(2k+1) < 0} has density 1/2. So
  n·π - a(n) ~ (π-2)n → ∞.
* The bounds look like they belong to A327139 (density 1/π).

## 9. A030229: FALSE AS STATED (trivial)

* **Conjecture.** "For the matrix M(i,j) = 1 if j|i and 0 otherwise, Inverse(M)(a,1) = -1 for any a in this
  sequence."
* **Why it fails.** Inverse(M)(i,j) = μ(i/j)[j|i] (Möbius inversion). So Inverse(M)(a,1) = μ(a) = +1 for every
  term. For example, a = 1 or a = 6 gives +1.
* The statement is true with -1 for A030059, so it was probably placed on the wrong entry.

---------------------------------------------------------------------------------------------------------

## 10. Easy proofs (all short; each was sanity-checked numerically)

* **A057015** (H. Dale, Sep 2026): terms after the first are ≡ 0 (mod 10). The term k is even, or else k^2+1 is
  even. If 5 ∤ k then 5 | k^2+1 or 5 | k^2+9, and these exceed 5 once k > 2.
* **A059324**: no primes p, q with q - p^2 = 6n - 4 (6n+5 composite).
  * p = 2 gives q = 6n.
  * p = 3 gives q = 6n+5, which is composite.
  * p >= 5 gives q ≡ 3 (mod 6).
* **A133907**: by Lucas, C(n+p,p) ≡ floor(n/p) + 1 (mod p). By Fermat, Σ_{k<=n} k^(p-1) ≡ n - floor(n/p)
  (mod p). Both conditions are "p | floor(n/p)", so the least primes coincide.
* **A135954**: for prime p >= 5, F_p = F_m^2 + F_{m+1}^2 with m = (p-1)/2 and coprime squares. So every prime
  factor of F_p is ≡ 1 (mod 4) and is a sum of two squares.
* **A140444**: ((x+1)^7 - 1)/x = Φ_7(x+1) is irreducible over Q. For p ≡ 1 (mod 7) it splits into 6 distinct
  linear factors x - (ζ - 1).
* **A182207**: a Carmichael C = p(2p-1)m needs pm ≡ 1 (mod 2p-2). Since p^2 ≡ 1 (mod 2(p-1)), this gives
  m ≡ p (mod 2p-2). The sibling A182515 already has Greathouse's Korselt remark; A182207 does not.
* **A190302**: a(n) < 6. For a mantissa x in [1,10): x ∈ [1,2) → h=1; [2,2.5) → 5; [2.5,10/3) → 4; [10/3,5) → 3;
  [5,10) → 2. Verified by the entry only to 10^7.
* **A247938**: max σ(2^p - 1)/2^p = 135/128, at p = 11.
  * Distinct prime factors of M_p satisfy q_i >= 2ip + 1, and there are s < p/log2(2p+1) of them.
  * So the ratio is < σ(M)/M < exp(H_s/(2p)) < 135/128 for p >= 19, checked by GP up to 2000 and trivially
    beyond.
  * Primes p <= 67 were computed exactly.
* **A270096**: a(n) <= n/3 for n > 8. Write n = 2^e·o and t = ord_o(2); then a(n) = min{m >= e : m ≡ n (mod t)}.
  * Odd n: a(n) < t <= λ(n) <= 4n/15, or a(p^k) = p^j <= n/p.
  * e = 1: a(2p^k) = 2p^j, or 2·3^j <= n/3; otherwise a <= λ(o) <= 2n/15.
  * e >= 2: a <= e - 2 + n/4 <= n/3, or a(2^e) = e <= 2^e/3 for e >= 4.
  * Checked for 9 <= n <= 20000.
* **A302975**: all terms are squares.
  * The exponent of q in the denominator is max(0, τ·v_q(n) - n·v_q(τ)).
  * If q ∤ τ, this is even: τ is even, or n is a square.
  * If q | τ, it is 0 whenever τ·v_q(n) <= n, which holds for n >= 256 since τ <= 2 sqrt n.
  * Checked for n <= 10^5.
* **A305214**: x^3 + y^3 misses some residue mod n iff 7 | n or 9 | n.
  * By CRT it suffices to check prime powers. For p ≡ 2 (mod 3), cubing is bijective.
  * For p ≡ 1 (mod 3) with p >= 13, Hasse gives >= p + 1 - 2 sqrt p - 3 > 0 affine points on x^3 + y^3 = d, and
    these Hensel-lift. d ≡ 0 is handled via x = 1, y = -1 + t.
  * Mod 7 the residues 3 and 4 are missed. Mod 9 cubes are {0, ±1}; mod 3 everything is hit.
  * Checked for n <= 3000.
* **A331021**: every term is a multiple of a Wieferich prime.
  * gcd(k^2, 2^(k-1)-1) > k gives a prime p | k with p^(v_p(k)+1) | 2^(k-1) - 1.
  * Since p ∤ k-1, ord_{p^2}(2) = ord_p(2) divides p-1, so p is Wieferich.
* **A363151**: denominators of B_j(1) are squarefree (von Staudt–Clausen). So every product's denominator has
  v_q <= 2, and so does the sum's. Checked for n <= 400.
* **A374571**: mod 2, A(x) ≡ A(x^2) + x·A(x^4), which is the same functional equation as the Fibbinary
  indicator. So a(n) is odd iff n is Fibbinary. Checked to 16384.
* **A384819**: integrality is equivalent to the Gauss congruences. They give a(p) ≡ -1 and
  a(p^k) ≡ a(p^(k-1)) (mod p^k), because p^(2k) - p^(2k-2) ≡ 0. So a(p^k) = p - 1.
* **A207969** (all k >= 0):
  * 5^k F(n)^(2k) is an integer combination of traces of powers of integer matrices (L((2k-2j)n)·(-1)^(jn), plus
    a constant), so it satisfies the Gauss congruences.
  * Dividing by 5^(k-1) keeps them: v_5(5·F(d)^(2k)) >= 1 + 2k(a-1) >= a when 5^a || n.
  * So exp(Σ 5F(n)^(2k) x^n/n) is in Z[[x]]. Checked for k <= 7 and n <= 300.
* **A395839**, both conjectures:
  * a = 10C^2 - C ≡ C (mod 2), and Catalan(n) is odd iff n = 2^k - 1.
  * Mod 3, D = (1 + x^2 C(x^3))/(1-x) satisfies xD^2 - D + 1 ≡ 0 (the numerator reduces to
    x^2(x^3E^2 - E + 1) with E = C(x^3)). Hence C ≡ D and a(x) ≡ x·C(x^3) (mod 3).
* **A395754**: for odd m, one of k, k+1 is even, so its radical cannot divide m.
* **A394757** (both conjectures):
  * If 3 || k then σ(3) = 4 forces 2 | gcd. With 4 ∤ gcd we get v2(k) = 1, and then σ(2) = 3 adds 3 to the gcd.
    So 9 | k and 18 | k.
  * A prime gcd q >= 5 would need σ(k) odd, i.e. k a square or twice a square. A square k = s^2 has
    k - 1 = (s-1)(s+1) composite. Twice a square has v2 odd, so 3 | σ(2^v2) and 3 | gcd.
* **A111499**: by Dusart 2010, x/(ln x - 1) < π(x) < x/(ln x - 1.1) for x >= 60184. So for n >= 5,
  10^n/π(10^n) - (n·ln 10 - 1) lies in (-0.1, 0). Consecutive differences therefore lie in
  (ln 10 - 0.1, ln 10 + 0.1) ⊂ (2,3), so the floors differ by 2 or 3. For n = 3,4 check directly.
* **A160627**: v2(4^k/k!) = k + s2(k) >= 2 for k >= 1, so L_n(4) ≡ 1 (2-adically) and the numerator is odd.
* **A143132**: Δ^j of a(n+4) - a(n) at n = 1 equals 320, 550, 560, 280, 0, all ≡ 0 (mod 10). Together with the
  last digits 1, 6, 6, 6 this gives the period.
* **A195986**: by LTE, v2(5^n - 3^n) = 1 for odd n and v2(n) + 3 for even n. A090740 = v2(3^n - 1) equals 1 or
  v2(n) + 2 in the same cases.
* **A341239**: with x = {√2 n}, r·s·n - a(n) = (1+√2)x + {-√2 x}. This equals 1 + x or 2 + x, so it lies in
  (1, 1.707) ∪ (2.707, 3).
* **A023105**: #{A004215 < 2^n} = Σ_j 2^(n-3-2j), which equals the known formula a(n) - 2.
* **A247250**: Carmichael's theorem (1913) on primitive divisors of Lucas sequences with real roots. The only
  small indices that need checking are n = 2, 6, 12; they have the primitive divisors 2, 7, 11.
* **A249759**: conjectures 2) and 3) hold. σ(p-1) prime forces p - 1 = 2^k (p odd), so p is a Fermat prime and
  σ = 2^(k+1) - 1 is a Mersenne prime.
* **A003625**: disc(x^2 + x + 2) = -7. The quadratic is irreducible iff (-7/p) = -1 iff p ≡ 3, 5, 6 (mod 7)
  (p = 2 and p = 7 are reducible).
* **A129194**: gcd(2(2n-1), n^2) = gcd(2, n^2).
* **Periodicity mod k, period dividing φ(k).** Mod k, all j >= J (with k | J!) drop out, so a(n) mod k is a
  fixed integer combination of i^n. Checked for k <= 100 and n in [300,700].
  * A064618: a(n) = Σ_j j!·(j!S(n,j)), with j!S(n,j) = Σ_i (-1)^(j-i) C(j,i) i^n.
  * A179929: e.g.f. 3/(1 + 2e^(-3x)), handled the same way.
  * A258899: a(n) ≡ 2 + 2^n eventually, since the middle terms vanish.

## 11. No counterexample, up to the stated bounds

| A-number | What was checked |
|---|---|
| A366833 | at most 2 proper prime powers between consecutive primes: brute force to 10^7, then all pairs of prime powers p^k (k >= 3) up to 10^18. No 3 powers in one gap. |
| A049048 | no composite c has two k >= 2 with k! ≡ 1 (mod c). Complete for witnesses n2 <= 2500 (gcd(n1!-1, n2!-1) with small primes removed), and for c = q·r or q^2 with primes <= 10^5. |
| A135508 | McEachen, Sep 2025. Proved that both parts follow from "every term is 1 or prime" (Cloitre); that statement verified for n <= 2·10^7. |
| A059992 | every HCN except 2, 6 is a record of τ - ω, up to 10^30 (292 HCNs); the margin grows fast. |
| A060957 | contiguity of p-exponents, n <= 30. |
| A375785 | all terms odd, n <= 4000. |
| A071823 | a(n) - n/2 > sqrt(n) for 1000 < n <= 4·10^8 (min margin at n = 1234). |
| A377142 | no other terms for m <= 2·10^8. |
| A138467 | the Dekking-corrected formula floor(r(p)(n+1)) for p = 3..12, n <= 10^8. |
| A320625 | a(n) mod 3 pattern for n <= 18. |
| A211193 | a(n) ≡ 1 (mod n), n <= 600. |
| A079128 | (n^2 - 1) \| a(n) and gcd(a(n), n) = 1, n <= 1500. |
| A364822 | both congruences, n <= 1500. |
| A371652 | integrality, n <= 1500. |
| A046528 | σ(n), τ(n) multiplicatively dependent only for products of Mersenne primes: holds for n <= 4·10^8 (`a046528/t.c`, `a046528/run4e8.txt`). |
| A288229, A288235, A289245, A289912 | strictly increasing, n <= 3000. |
| A195415, A221077 | purely periodic mod odd p with period dividing p - 1, p <= 79, n <= 160. For p = 2 the literal statement fails: a(1) = 1, a(2) = 8 (A221077) and 1, 2 (A195415) are not constant mod 2. |
| A343802 | not refuted. Heuristically the "floor or floor+1" pattern fails with probability about 0.1% per n, because E(k)/k ranges over roughly (-0.11, 0.71) for k <= 2·10^8. |
| A352743 | not run. The valuation random walk has positive drift (checked to 10^6 in the entry). |
