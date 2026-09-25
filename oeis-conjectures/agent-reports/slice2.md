# Slice 2 report (agent2)

Work dir: `/home/user/work/agent2/` (morphic-word work in `/home/user/work/agent2/morph/`).
All statements quoted below are from the local OEIS snapshot (2026-09-24).

## Top findings (strongest first)

| # | A-number(s) | Verdict | One-line certificate |
|---|---|---|---|
| 1 | **A066803** | **COUNTEREXAMPLE** | p = 3*2^41+1 = 6597069766657 divides both 2^(2^38)+1 and 3^(2^38)+1, so a(2^38) >= p > 1 |
| 2 | **A284365** (and the same conjecture in A284364, plus A284366) | **COUNTEREXAMPLE** | n = 8933313, a(n) = 20222898: n*(9+sqrt(21))/6 - a(n) = 2.00487... >= 2 |
| 3 | 13 more Kimberling morphic "discrepancy" conjectures in this slice | **PROOF** for 9 as stated plus 2 after fixing an obvious typo in r; **literally FALSE** (small n) for 4 | exact closed-form inf/sup, verified as an exact Bellman fixed point in Q(sqrt D) |
| 4 | **A373308** (3 conjectures, Hanna 2024) | **PROOF** (all three) | Frobenius mod 3; A(x)=(1-x)^3(1-x^2)^3 A(x^4) gives a(4j+2)=8a(j-1), a(4j+3)=8a(j); a(n) = floor(n/2)+1 (mod 2) |
| 5 | **A115770** (Karttunen, Dec 2025) | **PROOF** | the product automaton (carry, 3-bit window) has 14 reachable states, and no state accepts one language but not the other |
| 6 | **A342070** (Schoenfield 2021) | **PROOF**: 1323 is the last term (32 terms) | Dusart bounds for k >= 355991, plus a sieve for k < 400000 |
| 7 | **A061164, A295454, A295468, A295481** (Bala, Jun/Jul 2026) | **PROOF** (a(n/2) is an integer) | a Landau-type step-function check with half-integer shifts, plus an exact formula for v_2 |
| 8 | **A000139** (Bala, Jul 2025) | **PROOF** | v_2(a(n)) = s(n)+s(n+1)-s(3n), then a carry analysis |
| 9 | **A037301, A330904** (König 2020) | **PROOF** (no five consecutive terms) | parity of the digit-sum increments, then mod 3 |
| 10 | Easy proofs: A361034, A038867, A111869 (3 conj.), A225004, A340896, A187941, A233398, A207480, A208548 | PROOF (easy) | see Section 10 |
| 11 | A028576, A171481, A319227 | NO COUNTEREXAMPLE (bounds below) | |

---

## 1. A066803: COUNTEREXAMPLE (strongest result)

**Entry:** A066803, a(n) = gcd(2^n + 1, 3^n + 1).

**Conjecture** (Jianing Song, Nov 20 2021): "Conjecture: a(2^k) = 1 for k != 1. That is to say, there is no prime p > 5 such that ord(2,p) and ord(3,p) is the same power of 2, where ord(a,p) is the multiplicative order of a modulo p."

**Verdict: FALSE.** k = 38 is a counterexample, and so are k = 39, 207 and 157167.

**Certificate (k = 38).** Let p = 3*2^41 + 1 = 6597069766657 (prime).
- 2^(2^38) ≡ -1 (mod p) and 3^(2^38) ≡ -1 (mod p).
- Therefore p | gcd(2^(2^38)+1, 3^(2^38)+1) = a(2^38), so a(2^38) >= 6597069766657 > 1.
- Equivalently, ord(2,p) = ord(3,p) = 2^39, which violates the "no prime p > 5" form of the conjecture.
- One line of GP: `p=3*2^41+1; [isprime(p), Mod(2,p)^(2^38)==-1, Mod(3,p)^(2^38)==-1, znorder(Mod(2,p))==2^39, znorder(Mod(3,p))==2^39]` gives all 1.

**Why this happens (short proof of a family).** Let p = 3*2^n + 1 be a prime dividing the Fermat number F_m = 2^(2^m)+1, with n odd.
1. From p = 3*2^n + 1 we get 3 ≡ -2^(-n) (mod p).
2. Hence 3^(2^m) ≡ (2^(2^m))^(-n) ≡ (-1)^(-n) = -1 (mod p).

So p | gcd(2^(2^m)+1, 3^(2^m)+1). The known Fermat factor 3*2^41+1 | F_38 is such a case (n = 41 is odd).

**Further counterexamples (all verified):**
- 21*2^41+1 = 46179488366593 divides both 2^(2^39)+1 and 3^(2^39)+1, so a(2^39) > 1.
- 3*2^209+1 divides both 2^(2^207)+1 and 3^(2^207)+1.
- 3*2^157169+1 divides both 2^(2^157167)+1 and 3^(2^157167)+1. Primality is not needed for this: any common divisor > 1 refutes the claim. This check took 581 s with gmpy2.

**Smaller k.** Direct GMP computation of gcd(F_k, (3^(2^k) mod F_k) + 1) gives a(2^k) = 1 for 2 <= k <= 29. Whether 38 is the smallest counterexample, i.e. whether 30..37 are all 1, is not settled.

**Verification (three independent methods):**
- Python/sympy: `pow`, `n_order` and `isprime`.
- PARI/GP: `/home/user/work/agent2/a066803_check.gp`, using `isprime(p,1)` (a certificate) and `znorder`.
- Plain C with `__int128` and trial-division primality: `/home/user/work/agent2/a066803_int128.c`.
- Direct gcds for k <= 29: `/home/user/work/agent2/a066803_direct.c`, output in `a066803_direct_23_29.out`.
- Family search: `a066803_family.py`. Big cases: `a066803_big.py`.

**Novelty.**
- A066803 (last edited Dec 07 2021) does not mention the failure.
- The needed facts are scattered elsewhere in the OEIS but were never connected:
  - A171381 lists "(3^(2^38)+1)/2 has factors: 6597069766657".
  - A023394 and A229851 list 6597069766657 as a Fermat-number factor (of F_38).
- Calvo (Applied Math. Letters 13 (2000), cited in A171381) gives divisibility criteria for 3^(2^m)+1 by primes 3*2^n+1 that divide Fermat numbers. The underlying fact is therefore likely implicit in the literature, but the OEIS conjecture was never corrected.
- A WebSearch found no mention. oeis.org and primepuzzles.net are blocked from this machine, so the live pages could not be checked.

---

## 2. A284365 / A284364 / A284366: COUNTEREXAMPLE (non-trivial, first failure near n ≈ 9e6)

**Setup.**
- A284364 is the fixed point of the morphism 0->1, 1->101010.
- A284365(n) is the position of the n-th 0 (offset 1). A284366(n) is the position of the n-th 1.

**Conjectures** (Clark Kimberling, Mar 26 2017):
- A284365: "Conjecture: -2 < n*r - a(n) < 2 for n >= 1, where r = (9+sqrt(21))/6."
- A284364 repeats it: "-2 < n*r - u(n) < 2 and -1 < n*s - v(n) < 2 for n >= 1", with s = (-1+sqrt(21))/2.
- A284366: "Conjecture: -1 < n*s - a(n) < 2 for n >= 1, where s = (-1+sqrt(21))/2."

Only A284365 is in slice 2. A284364 and A284366 are the same system (slices 1 and 3).

**Verdict: FALSE (all three upper bounds).**

**Certificate for A284365.** n = 8933313, a(n) = 20222898.
- n*(9+sqrt(21))/6 - a(n) = 2.0048721733261288479...
- Exact integer form: the claim n*r - a(n) >= 2 is equivalent to n*sqrt(21) >= 6(a(n)+2) - 9n = 40937583. And 21*n^2 - 40937583^2 = 2393460 > 0.
- This is the first violation.
- Up to 10^10 letters there are 1104 violations. Largest value found: 2.078977 at n = 3353220813.

**Certificate for A284366 (and the v-part of A284364).** n = 2977771, a(n) = 5334043.
- n*(sqrt(21)-1)/2 - a(n) = 2.0048721733... >= 2.
- Exact form: 21n^2 - (2a(n)+4+n)^2 = 265940 > 0.
- This is the first violation; there are 4069 violations up to 10^10 letters.

**Exact extremes (proved; see Section 3).** The set {n*r - a(n)} has closure [-4/5 - 2*sqrt(21)/15, 6/5 + sqrt(21)/5] = [-1.41101..., 2.11651...]. For A284366 it is [-9/5 + sqrt(21)/5, 6/5 + sqrt(21)/5]. So the upper bound 2 is exceeded infinitely often, and the lower bounds hold.

**Verification (three independent implementations):**
1. Streaming C with exact `__int128` comparisons, which found the first violations:
   - `morph/a284365_exact.c`, output in `a284365_exact.out`
   - `morph/a284366_exact.c`, output in `a284366_exact.out`
2. Python random access. It locates the n-th 0 by descending the derivation tree with letter counts of σ^k(c), a different algorithm. It agrees on a(8933313) = 20222898 and matches all 61 listed terms. File: `morph/a284365_ra.py`.
3. Python/numpy full-word iteration, mirroring the entry's Mathematica program. It finds the same first violating n for both sequences:
   - `morph/a284365_fullword.py`
   - `morph/a284366_fullword.py`

PARI evaluation of the final real number also agrees.

**Novelty.**
- No mention in A284364, A284365 or A284366; their last edits (Apr 2025) only add density conjectures.
- The b-file covers only n <= 10000, and the first failure is at n ≈ 8.9e6.
- A grep for 8933313, 20222898 and 2977771 in the local OEIS finds only an unrelated coincidental substring.

---

## 3. Kimberling fixed-point "discrepancy" conjectures (Mar–Apr 2017): exact resolution

**Method (rigorous and computer-assisted).**
1. For a 2-letter substitution τ = σ or σ², with a Pisot matrix and second eigenvalue λ, let δ_t(w) = |w|_t - f_t|w|. This is a left eigen-functional of the substitution matrix, so δ_t(τ^i(p)) = λ^i δ_t(p).
2. By the Dumont–Thomas prefix decomposition, every value n*r - a(n) equals r(Σ_i λ^i δ_t(p_i) + 1 - f_t), where (p_i) runs over admissible reversed prefix-automaton paths from the letter t.
3. The inf and sup over all such paths are the unique fixed point (J, S) of a contracting Bellman system with 4 unknowns.
4. I find the optimal policy numerically. I then solve the linear system exactly in Q(sqrt D) and verify every Bellman (in)equality exactly. This certifies (J, S), and any admissible path's value lies in [J, S].
5. Values n*r - a(n) are never rational (r is irrational), so a bound equal to an attained-in-the-limit extreme is never reached.

**Cross-checks.**
- For every case, the level-K extremes from the DP coincide exactly with brute-force extremes over τ^K(start): `morph/dp_vs_brute.out`.
- A streaming 10^10-letter scan approaches each limit from inside: `morph/run_1e10*.out`.
- Code: `morph/exact_bellman.py` (exact, with `exact_qsqrt.py`) and `morph/exact_extremes.py` (50-digit DP). Output: `exact_bellman.out`.

| A-number | Stated bounds | Exact closure of {n r - a(n)} | Verdict |
|---|---|---|---|
| A026368 | (-2, 4), r = 2+√3 | [-1-√3/3, 2+2√3/3] = [-1.577, 3.155] | PROOF |
| A283963 (u) | (-1, 2), r = (3+√3)/2 | [-1/2-√3/6, 1+√3/3] | PROOF |
| A283963 (v) | (-1, 2), s = √3 | [-1+√3/3, 1+√3/3] | PROOF |
| A284365 | (-2, 2) | [-4/5-2√21/15, 6/5+√21/5] = [-1.411, **2.1165**] | **COUNTEREXAMPLE** (Section 2) |
| A284386 (u) | (0, 2), stated r = (5+**√3**)/2 | with the literal r the conjecture fails at n = 2 (value -0.268) | FALSE as stated (typo) |
| A284386 (u), corrected | r = (5+√13)/2, forced by the entry's "1/r+1/s=1" | [(1+√13)/6, (7+√13)/6] = [0.768, 1.768] | PROOF |
| A284386 (v) | (-1, 1), s = (-1+√13)/2 | [(-5+√13)/6, (1+√13)/6] | PROOF |
| A284505 (u) | (-3, 4) | [-3/2-5√3/6, 2+2√3/3] = [-2.943, 3.155] | PROOF |
| A284505 (v) | (-2, 4) | [-1-√3/3, 2+2√3/3] | PROOF |
| A284657 | (-1, 3) | [**-1**, (3+√3)/2]; -1 is a limit value, never attained | PROOF |
| A284752 | (-1, 3) | [**-1**, 1+2√3/3]; -1 is never attained | PROOF |
| A284852 | (-2, 2) | [-2/3-√3/3, 4/3+√3/3] | PROOF |
| A285036 | (-1, 2) | [-3/2+√2/2, 1/2+√2] | PROOF |
| A285135 | (-1, 1) | [-3-√3/3, 2+5√3/3] = [-3.577, 4.887] | FALSE: fails already at n = 1 (a(1) = 4 gives 1+√3-4 = -1.268); first failures n = 1, 3, 5, 9, ... |
| A285144 | (-1, √3) | [-2+√3/3, 1+4√3/3] = [-1.423, 3.309] | FALSE: equality at n = 1, then 2.464 > √3 at n = 2 |
| A285206 | (-1, 1) | [-2/3, 1/3+√3/3] | PROOF |
| A285278 | (0, 6) | [**0**, 3+2√2]; 0 is never attained | PROOF |
| A285374 | (-4, 1) with "n*sqrt(2)" | literal statement fails at n = 2 (2√2 - 8 < -4). The data give a(n)/n -> 2+√2 | FALSE as stated (typo) |
| A285374, r = 2+√2 | (-4, 1) | [-2-√2, 0] | PROOF |
| A285423 | (-2, 2) | [-3/2+√3/6, 2√3/3] | PROOF |

Notes on this table:
- The "literally false" cases are visible in the listed data and look like editing slips. The genuine, non-trivial failure is A284365 and its siblings.
- Related entries outside this slice (slice 1) fail the same way:
  - A285134 ("-1 < n*r-a(n) < 1", r = 1+sqrt(1/3)) fails at n = 2. Its closure is [-5/3-√3/3, 4/3+√3].
  - A285143 ("-1 < n*r-a(n) < 1", r = (3+√3)/3) fails at n = 12 (a(12) = 20). Its closure is [-4/3, 2/3+2√3/3].

---

## 4. A373308: PROOF of all three conjectures (Paul D. Hanna, Jun 20 2024)

**Entry:** A373308, the expansion of Product_{n>=0} (1 - x^(2^n))^3.

**Conjectures:**
- "(1) a(3*n) == A001285(n) (mod 3)"
- "(2) a(3*n+1) and a(3*n+2) are divisible by 3"
- "(3) a(n) = 0 iff n = 3*A000695(k) - 1 for k >= 1"

**Proof of (1) and (2).**
1. Mod 3, (1-y)^3 ≡ 1-y^3. So A(x) ≡ T(x^3) (mod 3), where T(x) = Prod(1-x^(2^k)) = Σ (-1)^(s_2(m)) x^m.
2. Hence a(n) ≡ 0 unless 3 | n, and a(3m) ≡ (-1)^(s_2(m)) ≡ A001285(m) (mod 3).

**Proof of (3).**
1. Parity. Mod 2, (1-y)^3 ≡ (1+y)(1+y^2). So A ≡ Prod_{k>=0}(1+x^(2^k)) · Prod_{k>=1}(1+x^(2^k)) = 1/((1-x)(1-x^2)), which gives a(n) ≡ floor(n/2)+1 (mod 2). So a(n) is odd, hence nonzero, when n ≡ 0 or 1 (mod 4).
2. A base-4 recursion. From A(x) = (1-x)^3(1-x^2)^3 A(x^4), with (1-x)^3(1-x^2)^3 = 1-3x+0x^2+8x^3-6x^4-6x^5+8x^6+0x^7-3x^8+x^9, we get:
   - a(4j+2) = 8a(j-1)
   - a(4j+3) = 8a(j), with a(-1) := 0.
3. Let D be the set of m >= 0 whose base-4 digits all lie in {0,3}. Claim: for n >= -1, a(n) = 0 iff n+1 ∈ D. Proof by induction on n:
   - Base case n = -1: n+1 = 0 ∈ D and a(-1) = 0.
   - n ≡ 0, 1 (mod 4): a(n) is odd, and n+1 ends in base-4 digit 1 or 2, so n+1 ∉ D.
   - n = 4j+2: a(n) = 8a(j-1), and n+1 = (base-4 digits of j) followed by 3, so n+1 ∈ D iff j ∈ D.
   - n = 4j+3: a(n) = 8a(j), and n+1 = 4(j+1), so n+1 ∈ D iff j+1 ∈ D.
4. For n >= 0, n+1 ∈ D \ {0} iff n+1 = 3m with m having base-4 digits in {0,1} and m >= 1, i.e. m ∈ A000695 with m >= 1. ∎

**Checks.** Numerically verified all three to n = 2^22, and the product against the recurrence. File: `/home/user/work/agent2/a373308.py`, output in `.out`. Novelty: the entry states all three as conjectures, with no proof.

---

## 5. A115770: PROOF (Antti Karttunen, Dec 21 2025)

**Statement.** "Numbers k such that 7*k = A048720(11,k)". Conjecture: "also numbers k such that 5*k = A048720(13,k). This has been checked for all k in range 0 .. 2^25."

**Proof (decision procedure).**
1. For odd a, b, the set {k : a*k = b ⊗ k} is recognized reading k LSB-first, with state = (carry, previous W bits of k) and W = max bit position of a and b. At bit i:
   - bit i of a*k is (Σ_{j∈a} k_{i-j} + carry) mod 2;
   - bit i of b⊗k is XOR_{j∈b} k_{i-j}.
   A mismatch kills the run.
2. Acceptance means that feeding zeros never produces a mismatch. The zero-feed terminates because the carry decreases once the window is zero.
3. BFS over the product automaton for (7,11) and (5,13) reaches only 14 state pairs, and in every one the two acceptance values agree. Hence the two sets are equal for all k.
4. The automaton model was checked against the direct definition for all k < 2^16.

File: `/home/user/work/agent2/a115770_automaton.py`, output `a115770.out`.

---

## 6. A342070: PROOF that 1323 is the final term (Jon E. Schoenfield, Mar 23 2021)

**Statement.** "Numbers k such that there are more primes in the interval [2*k+1, 3*k] than there are in the interval [k+1, 2*k]." Conjecture: "1323 is the final term."

**Proof.**
1. Known explicit bounds:
   - π(x) <= x/L (1+1/L+2.51/L^2) for x >= 355991 (Dusart 1999);
   - π(x) >= x/L (1+1/L+2/L^2) for x >= 88783 (Dusart 2010).
   Here L = ln x.
2. For k >= 355991 these give π(3k) + π(k) - 2π(2k) <= k*h(ln k)·(-1), where h(L) = 2Lo(2,L+ln2) - U(3,L+ln3) - U(1,L).
3. h(L) = N(L)/(100 L^3 (L+ln2)^3 (L+ln3)^3), where N has degree 7.
4. Every coefficient of N(12+y) is positive (smallest leading coefficient 52.32). So N(L) > 0 for L >= 12, which includes L >= ln 355991 = 12.78.
5. Hence π(3k)-π(2k) < π(2k)-π(k) for all k >= 355991.
6. A sieve for k <= 400000 finds exactly 32 terms, the last being 1323, identical to the 32 listed terms.

The sequence is therefore finite and complete (it could take keywords fini, full). File: `/home/user/work/agent2/a342070_proof.py`, output `a342070.out`.

---

## 7. Bala's "a(n/2) is an integer" conjectures: PROOF

**Entries and dates:**
- A061164 (Jul 31 2026): (10n)!(n/2)!/((5n)!(7n/2)!(2n)!)
- A295454 (Jun 13 2026): (15n)!(9n/2)!(5n/2)!/((9n)!(15n/2)!(5n)!(n/2)!)
- A295468 (Jul 30 2026): (15n)!(5n/2)!(3n/2)!n!/((15n/2)!(5n)!(4n)!(3n)!(n/2)!)
- A295481 (Jul 31 2026): (12n)!(2n)!(3n/2)!/((6n)!(9n/2)!(4n)!n!)

Each is "is an integer" with (x)! := Γ(x+1).

**Proof.** Write a(n/2) = Π (k_i n/2)!^{e_i}. Then:
- For n even, this is the original factorial ratio. Landau's step function Σ e_i ⌊k_i y⌋ >= 0 is checked on the grid y = j/lcm.
- For n odd, (M/2)! = M!·√π/(2^M ((M-1)/2)!). The √π cancels because Σ_{k_i odd} e_i = 0.
- For odd p, v_p((M/2)!) = Σ_j ⌊M/(2p^j) + 1/2⌋, using Hermite's identity. So v_p = Σ_j Φ(n/(2p^j)), where Φ(y) = Σ_{k even} e⌊ky⌋ + Σ_{k odd} e⌊ky+1/2⌋ has period 1 (Σ e_i k_i = 0). Φ >= 0 is checked exactly on the grid j/(2 lcm).
- For p = 2, v_2((M/2)!) = -(M+1)/2 exactly. This gives v_2 = n Σ_{k even} e k - Σ_{k even} e s_2(k n/2), which is positive; this is checked by an explicit bound plus odd n <= 2000.

All four pass. They were also checked by exact rational evaluation for n <= 300. File: `/home/user/work/agent2/bala_halfint.py`, output `bala_halfint.out`. The script is generic and can be reused for other Bala "a(n/2)" conjectures in other slices.

---

## 8. A000139: PROOF (Peter Bala, Jul 24 2025)

**Statement.** "Conjecture: a(n) is odd iff n is a term of A022341." A022341 are the odd Fibbinary numbers, i.e. odd n with no two adjacent 1-bits.

**Proof.**
1. By Legendre, v_2(a(n)) = s(n)+s(n+1)-s(3n), where s is the binary digit sum.
2. Write s(3n) = 2s(n) - c(n), where c(n) is the number of carries in n + 2n. Write s(n+1) = s(n)+1-t, where t is the number of trailing 1s of n. Then v_2 = 0 iff c(n) = t-1.
3. Case n even (t = 0): impossible, so a(n) is even.
4. Case t >= 2: the trailing block alone produces >= t carries, so a(n) is even.
5. Case t = 1: we need zero carries, which holds iff n has no two adjacent 1s.
6. So a(n) is odd iff n is odd and Fibbinary, which is exactly A022341. ∎

Checked for n <= 2*10^5 (and exactly for n < 400). File: `easy_checks.py`.

---

## 9. A037301 and A330904: PROOF of "no five consecutive terms" (Thomas König)

**Statements:**
- A037301 (s_2(n) = s_3(n)): "Conjecture: There is no occurrence of five or more consecutive terms ... Tested by exhaustive search up to a(n) = 3^29." (Aug 15 2020)
- A330904 (binary weight = balanced-ternary trit sum): same conjecture, "tested ... up to 3^30" (Jul 19 2020).

**Proof.**
1. s_3(m+1)-s_3(m) = 1-2c, where c is the number of trailing 2s. The balanced-ternary analogue is 1-2c with c the number of trailing 1-trits. Both increments are always odd.
2. s_2(m+1)-s_2(m) = 1-t, where t is the number of trailing 1-bits.
3. If m and m+1 are both terms, then for odd m (t >= 1) we need c >= 1, i.e. m ≡ 2 (mod 3) (resp. m ≡ 1 (mod 3) for A330904).
4. Five consecutive terms n..n+4 contain two odd m in {n,...,n+3} that differ by 2, and they cannot be congruent mod 3. ∎
5. Bonus: 4-runs must start at n ≡ 4 (mod 6) (resp. n ≡ 0 (mod 6)).

Verified to 2*10^8, where the maximum run is 4 and all 4-runs start in the predicted classes. File: `runs.c`.

---

## 10. Easy proofs (labelled easy)

- **A361034** (Bala 2023): "a(n) is odd iff n = 2^k - 2". We have v_2(a(n)) = 3 + (4n - s(n)) - (n - s(n)) - 3(n+2 - s(n+2)) = 3(s(n+2) - 1). Checked n < 600.
- **A038867** (Purath, May 15 2026): "no squares in (n+5)^3-n^3 = 5(3n^2+15n+25)". A square forces 5|y, then 5|n (n = 5m), then y = 5y1 with y1^2 = 5(3m^2+3m+1), then 5 | 3m^2+3m+1. That is impossible because 3m^2+3m+1 mod 5 ∈ {1,2,4}.
- **A111869** (Corneth, Aug 15 2025), all three conjectures, via Kummer's theorem:
  - v_q(C(2m,m)) is the number of carries of m+m in base q, and m < q^j has at most j carries. So getting j carries requires m >= (q^j-1)/2+1, which gives Conj. 1 (j = 2) and Conj. 2 (j = 2e).
  - v_2(C(2m,m)) = s_2(m), which gives Conj. 3: a(2^k) = 4^k-1.
- **A225004** (conj. "a(n) | n^2") and **A340896** (conj. "row n contains n^2 iff n is a prime power"):
  - If m is a multiple of n with d(m) < 2d(n), then m has no new prime (a new prime would double d), and each exponent f_p <= 2e_p (else the ratio (f_p+1)/(e_p+1) >= 2). So m | n^2.
  - d(n^2)/d(n) = Π(2e+1)/(e+1) is < 2 iff ω(n) <= 1, since each factor is >= 3/2 and 9/4 > 2.
- **A187941**: "a(n) = 2^n only if n is prime or n = 1". For composite n = ab (1 < a, b), the number 2^a·(least odd number with b divisors) <= 2^a 3^(b-1) is < 2^n. For prime n the only options are 2^n and 2·3^(n-1) > 2^n.
- **A233398** (Dale): n = 3m gives n^n = 3^n m^n ≡ 0 (mod 3^n).
- **A207480 / A208548** (Seidov 2012), "a(n) > 0": this follows from Nagura (a prime in (x, 6x/5] for x >= 25), since 6p/5 < min(3(p+1)/2, (4p+5)/3). Small n are covered by the data.

---

## 11. Tested, no counterexample

- **A028576** (F. Chapoton, Feb 25 2026): "a(n) is divisible by n and 3*a(n) by n^2". Holds for all n <= 6000 (`a028576.py`).
  - For primes p >= 5 it follows from Jacobsthal's congruence C(2mp^r, mp^r) ≡ C(2mp^(r-1), mp^(r-1)) (mod p^(3r)) via the standard Möbius-sum reduction.
  - p = 2 and p = 3 need care. I did not finish a proof, so the verdict is NO COUNTEREXAMPLE up to 6000.
- **A171481** (Krizek): Conjecture 1 "a(n)-a(n-1) = 0 or 1" holds for n <= 4*10^8 (`a171481.c`). a(4e8)/4e8 = 0.26861 vs e/10 = 0.27183 (Conj. 2, not tested further).
- **A319227** ("Conjecture: a(n) <= 2", twin primes in Collatz trajectories):
  - Among all 3424506 twin pairs with p+2 <= 10^9, only (3,5), (5,7), (11,13), (17,19), (71,73), (107,109) have one member in the other's trajectory.
  - No trajectory contains three of these pairs, so any n with a(n) >= 3 would need a Collatz-linked twin pair with p > 10^9 (`collatz_twin.c`).

## Files

`/home/user/work/agent2/`:
- `a066803_check.gp`, `a066803_direct.c`, `a066803_int128.c`, `a066803_family.py`, `a066803_big.py`
- `a373308.py`, `a115770_automaton.py`, `a342070_proof.py`, `bala_halfint.py`, `easy_checks.py`, `runs.c`, `a028576.py`, `a171481.c`, `collatz_twin.c` (outputs in `*.out`)

`/home/user/work/agent2/morph/`:
- `morphs.c` (streaming scan), `a284365_exact.c`, `a284366_exact.c`, `a284365_ra.py`, `a284365_fullword.py`, `a284366_fullword.py`, `exact_bellman.py`, `exact_qsqrt.py`, `exact_extremes.py`, `dp_vs_brute.py`, plus outputs.
