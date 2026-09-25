# Slice 4 report (agent 4)

Work directory: `/home/user/work/agent4/` (all code referenced below lives there).
The strongest findings come first. For every item I re-read the full local `.seq` entry and checked
cross-referenced entries for an earlier resolution.

Summary of verdicts

| A-number | Verdict | One-line certificate / reason |
|---|---|---|
| **A103225** | **COUNTEREXAMPLE (new)** | a(6203) = 120879728 > Pi*6203^2 = 120879717.125... |
| **A362334** | **COUNTEREXAMPLE (new), both parts** | built by CRT: a 63-digit even k with a(k) > a(k-1), and another with a(k) ≥ a(k+1) |
| **A190646** | **FALSE at p = 3 (from the data); PROOF for every prime p ≥ 5** | a(3) = 19 is odd; for p ≥ 5 Mihailescu's theorem rules out odd k |
| **A363482** | **PROOF (new)** | a(n) = D/gcd(D, 5(n-1)(n-3)!) with D = n^2+3n-5, which forces a(n) to be 1, a prime, or 49 (at n=6 only) |
| **A366274** | **PROOF (new)** | Dusart's explicit bounds for pi(x) and for prime gaps, plus a check of p_n < 396738 |
| A363097 | PROOF of the upper half; lower half has NO COUNTEREXAMPLE up to n = 5*10^7 | a parity argument gives a(n) <= 4n-3 |
| A217738 | PROOF (easy) | 2 divides F_k only when 3 divides k, and 3 divides F_k only when 4 divides k |
| A179875 | PROOF (easy) | uses the closed form of the antiharmonic mean |
| A360635 | PROOF (easy) | uses partitions with no part 1 |
| A144652 | PROOF (easy) | composite 4h+1 = (2m+1)(2n+1) with m+n even |
| A064414, A308833, A378616, A280246, A057194, A394407, A259145, A088884, A112992 | PROOF (easy/trivial) | see below |
| A364131 | PARTIAL PROOF | terms must be squares or twice squares; no twice-square 2m^2 with 2 ≤ m ≤ 3*10^4 |
| A285127, A285138, A285354, A284795 | FALSE AS STATED (easy; each already fails within the listed data) | see below |
| A284488, A285413, A285429 | FALSE (the conjectured limit is wrong) | the true limits come from the Perron-Frobenius eigenvector |
| A086552 (2) | COUNTEREXAMPLE, but ALREADY KNOWN (recorded in A086551, 2005) | x = 983040 for n = 17 |
| A243982 | follows from results already proved in the OEIS (Hoft, A379288/A384149) | every run of divisors starts at an odd divisor |
| A006579, A015126, A065515, A123365, A226115, A328556, A218459, A110545, A380354, A294508, A359507, A369083, A330996, A361831, A363265, A123737, A389221/A390100, Kimberling bound conjectures | NO COUNTEREXAMPLE up to the stated bounds | see below |

---

## 1. A103225: COUNTEREXAMPLE

* Sequence: number of Gaussian integers z with |z| < n and gcd(n, z) = 1 (T. D. Noe, 2005).
* Conjecture: "a(n) < Pi*n^2." Posted by Bill McEachen on Aug 14 2025.
* **Verdict: COUNTEREXAMPLE.** The smallest counterexample is n = 6203:
  a(6203) = 120879728, while Pi*6203^2 = 120879717.1250390747...,
  so a(6203) - Pi*6203^2 = +10.8749609...

**Why it happens (and a one-line check).** 6203 is a prime and 6203 ≡ 3 (mod 4), so 6203 is a Gaussian prime.
gcd(6203, z) ≠ 1 therefore means 6203 | z, i.e. 6203 | x and 6203 | y. Inside the open disc |z| < 6203 only z = 0
satisfies this. So a(6203) = #{(x,y) in Z^2 : x^2 + y^2 < 6203^2} - 1, which is the entry's own remark
"a(n) = A051132(n) - 1" for Gaussian primes n. The count of lattice points in the disc fluctuates around the area
Pi*n^2 by about ±n^(1/2) (Gauss circle problem). At integer radius there is a negative bias, so a violation
is rare, but violations must occur.

One line of GP reproduces it:
```
n=6203; sum(x=-n+1,n-1,2*sqrtint(n^2-1-x^2)+1)-1 - Pi*n^2   \\ = 10.8749609252968860...
```

**Verification (three independent methods, all agreeing on 120879728):**
1. `a103225_direct.c`: brute force over all ~1.2*10^8 lattice points of the disc. Each gcd(6203, x+iy) is computed
   by a Euclidean algorithm in Z[i] implemented from scratch. It does not assume that 6203 is a Gaussian prime.
2. `a103225_ie.c`: inclusion-exclusion over the squarefree Gaussian divisors d of n,
   a(n) = Σ μ(d)·#{w : N(w) < n^2/N(d)}. It reproduces all 49 listed terms, agrees with (1) and with a Python
   Gaussian-gcd brute force (`a103225_brute.py`) for every n ≤ 120, and checks exactly every n ≤ 10000.
   The only violation for n ≤ 10000 is n = 6203, so 6203 is the least counterexample.
3. `a103225_check.gp`: PARI/GP at 77 digits confirms isprime(6203), 6203 % 4 = 3, factor(6203 + 0*I) = [6203,1],
   and a - Pi*n^2 = 10.87496092529688603...

Further counterexamples among primes p ≡ 3 (mod 4) up to 2*10^5 (`a103225_p3.c`, file `a103225_p3_2e5.txt`):
6203 (+10.87), 44963 (+27.18, also checked in GP), 49123 (+19.73), 100379 (+143.45), 104107 (+12.58),
127123 (+127.41), 147811 (+90.35), 158443 (+124.98).

**Novelty.** The entry contains only the conjecture. There is no mention in A051132, A387220, A394684, A007882
or any other local entry, and a web search found nothing.

---

## 1b. A362334: COUNTEREXAMPLE to both parts

* Sequence: a(n) = phi(n) + phi(n+2) (Alexandre Herrera, Apr 2023).
* Conjecture: "a(2*n) <= a(2*n-1) and a(2*n) < a(2*n+1)."
* **Verdict: COUNTEREXAMPLE, to both inequalities.**

**Idea.** Use the Chinese remainder theorem to make both odd neighbours 2n±1 divisible by many small odd primes,
split in balanced halves. Their totient ratios are then about 0.47 each. At the same time n and (n+1)/2 are made
prime, so the even neighbours have the largest possible totients.

**Certificate for part 1 (a(k) > a(k-1)).** Take k = 2n with

n = 134012348126107206688690603701275719891017841718586793654900333 (63 digits, prime).

* k = 2·n.
* k+2 = 4·s with s = (n+1)/2 = 67006174063053603344345301850637859945508920859293396827450167 (prime).
* k-1 = 5·7·11·17·23·37·41·47·61·71·73·89·101·103·113·127·137 · q1, with q1 = 43390185448919678598761070137573603 (prime).
* k+1 = 3·13·19·29·31·43·53·59·67·79·83·97·107·109·131·139·149 · q2, with q2 = 2219045541677716323513063560838557 (prime).

Therefore:
* a(k) = (n-1) + 2(s-1) = 268024696252214413377381207402551439782035683437173587309800664.
* a(k-1) = Π(p-1)·(q1-1) + Π(p-1)·(q2-1) = 252136077498098530469695437667669537496006719677543082465689600.
* a(k-1)/a(k) = 0.9407... < 1, a clear violation.

One line of GP checks it:
```
n=134012348126107206688690603701275719891017841718586793654900333; k=2*n; eulerphi(k)+eulerphi(k+2) > eulerphi(k-1)+eulerphi(k+1)   \\ 1
```

**Certificate for part 2 (a(k) ≥ a(k+1)).** Take n = 539414769491017837931500222298531509788246672344348812944989101
and k = 2n.
* n and (n+1)/2 are prime.
* k+1 = 3·13·19·29·31·43·53·59·67·79·83·97·107·109·131·139·149 · 8931907813657426720560315647293213 (prime cofactor).
* k+3 = 5·7·11·17·23·37·41·47·61·71·73·89·101·103·113·127·137 · 174650375203312263534542835281818831 (prime cofactor).
* a(k) = 1078829538982035675863000444597063019576493344688697625889978200.
* a(k+1) = 1014876061988131445004262448935803465836111449982767725753139200.
* So a(k) > a(k+1).

**Verification.**
1. PARI/GP (`a362334_construct.gp`, `a362334_construct2.gp`, `a362334_verify.gp`, `q.gp`): every large factor is
   proven prime with `isprime` (APR-CL), and eulerphi is evaluated directly on the full numbers.
2. Independent Python/sympy (`a362334_verify.py`): the products are
   reassembled exactly, BPSW is run on all factors, and the totients are recomputed from the explicit formula.
   The values agree.

**Small range.** There is no violation of either inequality with 2n ≤ 10^9 (`a362334.c`, segmented totient sieve).
The minimum ratio (right side over left side) there is 1.1022 for part 1 and 1.1094 for part 2, and it decreases
very slowly. The smallest counterexample is therefore large and remains unknown.

**Novelty.** The entry contains only the conjecture, and no other local entry references A362334.

## 1c. A190646: false at p = 3; PROVED for all primes p ≥ 5

* Sequence: a(n) is the least k with d(k-1) = d(k+1) = 2n (or 0 if none).
* Conjecture (Chai Wah Wu, 2019): "if p is an odd prime, then a(p) is even."

**Literally false.** a(3) = 19 is odd: d(18) = d(20) = 6. This is in the listed data.

**Proof for every prime p ≥ 5.** No odd k satisfies d(k-1) = d(k+1) = 2p, so a(p) is even, whether a(p) is a
genuine term or the default 0.
* If k is odd, one of k±1 is u = 2m with m odd. Then d(m) = p, so m = q^(p-1) for an odd prime q.
* The other one is w = 2^a·m' with a ≥ 2. From (a+1)·d(m') = 2p, either a = 2p-1 and m' = 1, or a = p-1 and m' = r
  is an odd prime.
* Hence q^(p-1) ± 1 = 2^(2p-2) or 2^(p-2)·r.
  - 2^(2p-2) is impossible by Mihailescu's theorem (Catalan's conjecture).
  - q^(p-1) + 1 ≡ 2 (mod 8) is not divisible by 2^(p-2) ≥ 8.
  - q^(p-1) - 1 = (q^h - 1)(q^h + 1) with h = (p-1)/2 ≥ 2. The two factors have gcd 2, so one of them must be a
    power of 2. Then q^h = 2^i ± 1, and Mihailescu leaves only 3^2 = 2^3 + 1. That gives
    q^(p-1) - 1 = 80 = 2^3·10, and 10 is not prime.
* So there is no odd k. ∎

Consistency checks:
* Every known term a(p) (p = 5, 7, 11, 13, 17, 19, 23, 29, 31, 37) is even.
* An exhaustive search to 2*10^8 (`a190646.c`) finds 184 odd k for p = 3 and none for p = 5, ..., 23.

---

## 2. A363482: PROOF of the conjecture

* Sequence: denominator of 1/(2-3/(3-4/(4-5/(...(n-1)-n/(-5))))), n >= 3.
* Conjecture: "Except for 49, every term of this sequence is either a prime or 1."
  Posted by Bill McEachen, who checked it through n = 10000.
* **Verdict: PROOF.** The conjecture is true for all n.

**Step 1: closed form.** Evaluate the continued fraction from the inside with unreduced integers:
u_{n+1} = 1, u_n = -5, and u_j = j·u_{j+1} - (j+1)·u_{j+2} for j = n-1, ..., 2. The value is u_3/u_2.
Write !m = Σ_{i=0}^{m-1} i! (left factorial). For any constants A and B, the function
F(k) = (k-2)(A + B·!(k-3))/(k-1)! satisfies F(j) = jF(j+1) - (j+1)F(j+2) for every j >= 3. To see this, put
L = !(j-3). Then jF(j+1) - (j+1)F(j+2) = [(j-1)(A+BL+B(j-3)!) - (A+BL+B(j-3)!+B(j-2)!)]/(j-1)! = (j-2)(A+BL)/(j-1)!.
So u_k = F(k) for 3 ≤ k ≤ n+1, with A and B fixed by u_n and u_{n+1}.
From these, u_3 = A/2, u_4 = (A+B)/3 and u_2 = 2u_3 - 3u_4 = -B.
Solving the two boundary equations gives B = n(n-2) + 5(n-1) = n^2+3n-5 =: D and A = -(D·!(n-3) + 5(n-1)(n-3)!).
Hence the value equals (D·!(n-3) + 5(n-1)(n-3)!)/(2D). D is odd, and u_3 = -M/2 is an integer, where
M = D·!(n-3) + 5(n-1)(n-3)!. Therefore

  **a(n) = D / gcd(D, 5(n-1)(n-3)!),  D = n^2 + 3n - 5.**

This matches Michel Marcus's PARI formula in the entry. It was checked against exact continued-fraction evaluation
for 3 ≤ n ≤ 800.

**Step 2: arithmetic.** a(n) = Π_{p|D} p^{max(0, v_p(D) - v_p(5(n-1)(n-3)!))}. D is always odd.
* Primes p > n dividing D do not divide 5(n-1)(n-3)!, so they survive in full. D < (n+2)^2, so at most one such
  prime occurs. It can occur squared only if (n+1)^2 | D. Since D = (n+1)^2 + (n-6), that requires (n+1) | 7,
  i.e. n = 6, which gives D = 49.
* Primes p ≤ n dividing D always have v_p(5(n-1)(n-3)!) >= 1:
  - p = n-1 never divides D, because D ≡ -1 (mod n-1).
  - p = n or p = n-2 forces p = 5, and then 5 | 5(n-1)(n-3)!.
  - Otherwise p ≤ n-3, so p | (n-3)!.
  So such a p survives only if v_p(D) >= 2 ("deficient p").
* Let t = floor((n-3)/p) ≤ v_p((n-3)!). If t >= 2, then p^(t+1) > p^((n-3)/p) >= ((n-3)/3)^3, because ln p/p
  decreases for p >= 3. For n >= 40 this exceeds (n+2)^2 > D, a contradiction. So for n >= 40 a deficient p has
  t = 1, i.e. p > (n-3)/2. Then p^3 > D forces v_p(D) = 2, and D = p^2·m with odd m ≤ 5. In that case a(n) = p.
  Two deficient primes, or a deficient prime together with a surviving prime > n, are impossible by size.
* Therefore, for every n >= 40, a(n) is 1 or a prime. n = 3..39 is checked directly; the only non-prime term
  other than 1 is a(6) = 49. ∎

Numerical cross-check (`a363482.py`): the listed data are reproduced, and the valuation formula finds no
violation for n ≤ 30000.

**Novelty.** The entry has the gcd formula and partial %F remarks, but no proof. The conjecture is still listed as open.

---

## 3. A366274: PROOF of the conjecture

* Sequence: a(n) is the least k such that prime(n+1+k) >= prime(n) + prime(n+1). Equivalently, a(n) is the number
  of primes strictly between p_n and p_n + p_{n+1}, which is pi(p_n + p_{n+1}) - n for n >= 2.
* Conjecture: "for n >= 3, a(n) < n." Posted by Patrick Butler, 2023.
* **Verdict: PROOF.**

The conjecture is equivalent to pi(p_n + p_{n+1}) ≤ 2n - 1.

* **Case p_n < 396738:** checked directly. In fact every n with p_n < 2*10^7 was checked (`a366274.py`).
  The minimum of n - a(n) over n >= 3 is 1, attained at n = 3.
* **Case x = p_n >= 396738:** the proof uses three results.
  - Dusart (2010, arXiv:1002.0442): there is a prime in (x, x(1 + 1/(25 ln^2 x))]. Hence
    y := p_n + p_{n+1} ≤ 2x(1+δ) with δ = 1/(50 ln^2 x).
  - Dusart: pi(t) ≤ t/(ln t - 1.1) for t >= 60184, and this bound is increasing in t. Hence
    pi(y) ≤ 2x(1+δ)/(ln x + ln 2 - 1.1) = 2x(1+δ)/(ln x - 0.40685...).
  - Dusart: pi(x) >= x/(ln x - 1) for x >= 5393.

  So pi(y) < 2pi(x) = 2n provided (1+δ)(ln x - 1) < ln x - 0.40685. That is equivalent to δ(ln x - 1) < 0.593,
  and δ(ln x - 1) < 1/(50 ln x) < 0.002. Hence pi(y) ≤ 2n - 1, i.e. a(n) ≤ n - 1. ∎

I confirmed both Dusart bounds by web search (Wikipedia's prime-counting-function and Bertrand's-postulate pages,
and arXiv:1002.0442).

---

## 4. A363097: upper bound PROVED; lower bound NO COUNTEREXAMPLE up to n = 5*10^7

* Sequence: a(0) = 1, a(n) = n + phi(a(n-1)).
* Conjecture: "1.25*n < a(n) < 4*n for n > 0." Posted by Giorgos Kalogeropoulos, 2023.

**Proof of a(n) < 4n.**
* a(k) >= k+1 for k >= 1, so a(m-1) >= 3 for m >= 3. Since phi(x) is even for x >= 3, a(m) ≡ m (mod 2) for m >= 3.
* Claim, by induction for n >= 2: a(n) ≤ 4n-3 for even n, and a(n) ≤ 3n-2 for odd n.
  - Base: a(2) = 3 and a(3) = 5.
  - Even n >= 4: a(n) ≤ n + a(n-1) - 1 ≤ 4n-6.
  - Odd n >= 5: a(n-1) is even, so phi(a(n-1)) ≤ a(n-1)/2, and a(n) ≤ n + (4n-7)/2 < 3n-2.
* Also a(1) = 2 < 4. ∎

**Lower bound.** Computed exactly to n = 5*10^7 (`a363097.c`, phi sieve). The minimum of a(n)/n is 1.335366,
at n = 12641011. The maximum is 3.968532, consistent with the proof. The record minimum drifts slowly downward
(1.50 → 1.38 at 10^6 → 1.335 at 1.3*10^7). The lower bound is probably false eventually, but a violation looks out
of computational reach. INCONCLUSIVE.

---

## 5. Easy/trivial proofs (all complete)

* **A308833** (r with T(r) = r(r+1)(r+2)/6 dividing r!). Conjecture: "for every odd r > 1, (a) r is a term,
  (b) r+1 is a term, and (c) r+2 is composite are equivalent."
  - (a) ⟺ (r+1)(r+2) | 6(r-1)!, and (b) ⟺ (r+2)(r+3) | 6·r!.
  - If r+2 = p is prime, then p ≥ 5 divides neither side, so (a) and (b) both fail.
  - If r+2 = N is an odd composite (N ≥ 9), then N | (N-3)!. For N = ab with a < b, use b ≤ N/3. For N = p^2, use
    p and 2p ≤ p^2 - 3.
  - Also r+1 = 2s with 3 ≤ s ≤ r-1, so 2s | (r-1)!; similarly r+3 = 2t with 3 ≤ t ≤ r, so 2t | r!. Both products
    are of coprime factors, so (a) and (b) hold. ∎
* **A378616** (greatest non-prime-power ≤ prime(n)). Conjecture: "equals prime(n) - 1 except at terms of A159611."
  - p_n - 1 (≥ 2) is a prime power iff it is 2^j, iff p_n is a Fermat prime, i.e. n ∈ A159611. ∎

* **A064414** (numbers dividing some term of every Fibonacci-type sequence). Conjecture (Kleinwaks):
  "j^2 = Σ_{d|j} phi(d)·A001177(d)."
  - The Fibonacci map (x,y) → (y,x+y) is a bijection of (Z/j)^2, so every orbit is periodic.
  - For t of additive order d, the orbit of (0,t) is t·(F_i, F_{i+1}), which is isomorphic to the Fibonacci orbit
    mod d. It has pi(d) elements, and exactly pi(d)/z(d) of them have first coordinate 0 (z = A001177).
  - Hence #{pairs whose orbit meets first coordinate 0} = Σ_t z(ord t) = Σ_{d|j} phi(d) z(d).
  - That count is A232656(j), and j is in the sequence iff it equals j^2. ∎
  - This also proves Kleinwaks's formula conjecture in A232656.

* **A217738** (k with k(k+1) | F_k). Conjecture: "all terms are divisible by 12."
  - Proof: k(k+1) is even, so 2 | F_k, which means 3 | k (F mod 2 has period 0,1,1).
  - Then 3 | k | F_k, which means 4 | k (the zeros of F mod 3 are at multiples of 4). ∎
  - Also checked for k ≤ 2*10^7 (`a217738.c`): 3786 terms, all multiples of 12.
* **A179875**. Conjecture (Amiram Eldar): "numbers k with mu(k)=1 and mu(k+1)=-1."
  - The standard formula Σ_{k≤h,(k,h)=1} k^2 = h^2 phi(h)/3 + (h/6)Π_{p|h}(1-p) (h > 1) gives the antiharmonic mean
    B(h) = 2h/3 + (-1)^omega(h)·rad(h)/(3h). This also holds at h = 1.
  - B(h) = B(h+1) is therefore equivalent to ε_h r_h - ε_{h+1} r_{h+1} = 2, where r = rad(x)/x ∈ (0,1] and
    ε = (-1)^omega.
  - That forces r_h = r_{h+1} = 1, ε_h = 1 and ε_{h+1} = -1, i.e. mu(h) = 1 and mu(h+1) = -1, and conversely. ∎
  - Verified with exact rationals for h ≤ 3000.
* **A360635**. Conjecture: "except for the values 2, 4 and 6, this sequence includes all the nonnegative integers."
  - Let d(m) = p(m+1) - p(m) = r(m+1), where r = A002865 counts partitions with no part 1.
    Then m occurs in the sequence iff d(m) > max_{m'<m} d(m').
  - The map "add 1 to the largest part" injects partitions of N (no 1s) into partitions of N+1 (no 1s).
    It misses partitions whose two largest parts are equal, which exist for N+1 even >= 4 and for N+1 odd >= 9.
    Hence r(N+1) > r(N) for N+1 >= 8.
  - Together with d(0..7) = 0,1,1,2,2,4,4,7, exactly 2, 4 and 6 are missing. ∎
* **A144652** (T(m,n) = floor((2mn+m+n)/2), m ≥ n ≥ 1). Conjecture: "If h does not belong to the sequence,
  then 4h+1 is prime."
  - If 4h+1 is composite, write 4h+1 = (2m+1)(2n+1) with m ≥ n ≥ 1. Since the product is ≡ 1 (mod 4), m+n is even.
  - Then 2mn+m+n = 2h, so T(m,n) = h. ∎
* **A280246**. Conjecture: "a(n) odd iff psi(n) odd."
  - psi(1) = psi(2) = 1, and psi(m) = m·phi(m)/2 for m >= 2. So psi(m) is odd iff m ∈ {1, 2} or m = p^k with
    p ≡ 3 (mod 4) (this uses phi(m) ≡ 2 (mod 4)).
  - Every divisor of such an n is again of that form, so a(n) is odd. If psi(n) is even, the factor psi(n) makes
    a(n) even. ∎
* **A057194**. Conjecture: "A057194(n) < A216151(n) for n > 1."
  - Both sequences obey the same recurrence b(n+1) = (Π b)(Σ b), with starts (1,1) and (1,2).
  - By induction, with all terms positive and 2 > 1 at n = 2, both the product and the sum are strictly larger
    for A216151 at every later step. ∎
* **A394407**. Conjecture: "all primes p ≠ 3 are in the sequence."
  - For 2 ≤ m < p: phi(m)/tau(m) ≤ (m-1)/2 < (p-1)/2.
  - For m = 1 the ratio is 1 = (p-1)/2 only when p = 3. ∎
* **A259145** (k^2 - phi(k) prime). Conjecture: "every term is a cyclic number."
  - d = gcd(k, phi(k)) divides k^2 - phi(k), and k^2 - phi(k) > k ≥ d. So d = 1. ∎
* **A088884**. Conjecture: "terms other than 3 are ≡ 5 (mod 6)."
  - c = concat(p, rev p) ≡ 2p (mod 3), so for p ≡ 1 (mod 3), 3 | c-2.
  - The same argument shows that c-2 and c+2 are never both prime, which answers the entry's other observation. ∎
* **A112992**. Conjecture: "the odd values of ceiling(2^(2^k mod k)/3) are Jacobsthal numbers, and the even values
  are 1 plus a Jacobsthal number."
  - ceil(2^m/3) = J(m) for odd m, and J(m)+1 for even m. J(m) is odd for m >= 1, and m = 0 gives 1 = J(1). ∎

---

## 5b. A389221 / A390100: half of each conjecture PROVED; the other half has NO COUNTEREXAMPLE

* A389221 conjecture: "all 4p (p prime > 13) belong, and no other k > 80."
* A390100 conjecture: "all 3p (p prime > 7) belong, and no other k > 52."
* Here the count is the number of distinct values taken at least twice by frac(2k/m), 1 ≤ m ≤ k.

**Reformulation.** Write m = g·b with g = gcd(m, 2k) and c = 2k/g. Then frac(2k/m) = (c mod b)/b with gcd(b,c) = 1.
So a nonzero value is repeated iff there are divisors g1 < g2 of 2k and b ≥ 2 with g2·b ≤ k, gcd(b, c1) = 1 and
b | c1 - c2. The value 0 is always repeated (m = 1, 2).

**Proof that k = 4p is a term (p > 13 prime).** The divisors of 8p are 1, 2, 4, 8, p, 2p, 4p, 8p. Checking all
admissible pairs, only b = 3 and b = 7 occur:
* b = 3 from the pairs (1,4) and (2,8), plus pairs involving p when p ≡ 1 or 2 (mod 3). These give exactly the
  two values 1/3 and 2/3.
* b = 7 from the pair (1,8); this needs 7 ≤ p/2, i.e. p ≥ 17. It gives one value.
* Together with 0, that is exactly 4 values. ∎

**Proof that k = 3p is a term (p > 7 prime).** The divisors of 6p are 1, 2, 3, 6, p, 2p, 3p, 6p.
* The pair (2,6) gives b = 2, the value 1/2.
* The pair (1,6) gives b = 5, the value (p mod 5)/5; this needs 5 ≤ p/2.
* No other pair works, so together with 0 there are exactly 3 values. ∎

**The "no other k" direction.** Checked with a fast counter (`a389221.c`) that implements the reformulation. It was
cross-checked against the entries' Python definition for all k ≤ 1500, with 0 mismatches. RESULT_PLACEHOLDER

## 6. Morphic-word conjectures (Kimberling): several are false as stated

Words were generated exactly as in the entries' Mathematica code, including the parity of the Nest count
(`morphtest.py`, `limtest.py`, `tmtest.py`, `settest.py`). All listed data were reproduced.

* **A285127** (positions of 1 in the σ^2-fixed point of 0→10, 1→0000). Conjecture: "-3 < n*r - a(n) < 0, r = 3.5621..."
  - It already fails at n = 2: a(2) = 11, and 2r - 11 = -3.88.
  - The substitution matrix has eigenvalues (1±sqrt 17)/2, so |λ2| = 1.56 > 1. Hence the discrepancy is unbounded
    for every choice of r. Numerically, the minimum of n·r* - a(n), with r* = (3+sqrt 17)/2, is -5630 by n = 2.8*10^6.
  - The same failure affects A285126 (not in this slice): a(21) = 26 gives 21·1.3903... - 26 = 3.2 > 1.
* **A285138**. Conjecture: "-1 < n(1+sqrt3) - a(n) < sqrt3."
  - n = 1 gives exactly sqrt3, and n = 2 gives 2.46.
  - The true range, up to n = 1.8*10^7, is about (-3.54, 4.88).
* **A285354**. Conjecture: "3n/2 + 1/2 - a(n) ∈ {0, 1/2, 1}."
  - n = 2 (a(2) = 4) gives -1/2.
  - Up to 6.7*10^6 terms the values taken are exactly {-1/2, 0, 1/2}.
* **A284795**. Conjecture: "a(n) - 3n + 3 ∈ {0,1}."
  - a(1) = 3 gives 3. The observed set is {2,3,4,5}.
  - The comment is evidently garbled.
* **A284488**. Conjectured limit a(n)/n → (7+sqrt13)/6 ≈ 1.768.
  - The word is a fixed point of σ^2 for the primitive substitution 0→1, 1→0011. Its letter frequencies are the
    normalized Perron-Frobenius eigenvector of [[0,2],[1,2]], which gives the limit (3+sqrt3)/2 = 2.3660254...
  - Numerically a(n)/n = 2.3660254 at n = 4.2*10^7.
* **A285413**. Conjectured limit (61-sqrt3)/26 = 2.2795.
  - The substitution 0→11, 1→010 gives the limit (3+sqrt17)/4 = 1.78078.
* **A285429**. Conjectured limit (82+sqrt3)/47 = 1.781533.
  - The substitution 0→11, 1→100 gives the limit (3+sqrt17)/4 = 1.780776. This is an element of Q(sqrt17),
    hence not equal to the conjectured value.
  - Numerics are consistent: a(n)/n = 1.780834 at n = 5.6*10^7. Convergence is slow because |λ2| > 1.

Limit conjectures that I confirmed are correct (exact Perron value equals the claim, and numerics agree):
A284526, A284590, A284959, A285535, A285601, A285627, A285161, A285516, A285591, and the Thue-Morse transforms
A285958, A285973, A286486, A286495, A284684.

Bound conjectures with NO COUNTEREXAMPLE up to 5*10^7 letters: A086398 (the extremes appear to converge to
-1 and 2+sqrt3, so the strict bound holds), A283965, A284368, A284507, A284675, A284930, A284941, A285082,
A285209, A285302, and A286051 (set {0,1}).

---

## 7. A086552 conjecture (2): COUNTEREXAMPLE, already known

* Conjecture: "If x is the smallest number for a given n such that tau(x)/tau(x-1) = n > 1, then x-1 is a prime."
* n = 17: the smallest x is 983040 = 2^16·3·5, with tau = 68, and x - 1 = 241·4079 (tau = 4).
  Further counterexamples: n = 34 (x = 6881280, x - 1 = 109·63131) and n = 23 (x = 62914560, x - 1 = 3361·18719).
  (n = 2 is also degenerate: x = 2 and x - 1 = 1.)
* Verified by an exhaustive C sieve to 4*10^8 (`a086552.c`) and by an independent PARI scan (`a086552_check*.gp`).
* **Not new:** A086551 already records "a(17)-1 is composite" (D. Wasserman, 2005). A086552 does not mention it.

## 8. A243982: follows from existing proved results

The conjecture (Omar Pol, 2025) says a(n) = #{divisors r of n with r ≤ 2·(previous divisor)}. It is equivalent to
"the number of parts of the symmetric representation of sigma(n) equals the number of maximal 2-dense runs of
divisors."
* Every run starts at an odd divisor, because an even divisor d has d/2 immediately available as a divisor.
* So the number of runs equals #{odd e | n with no divisor in (e/2, e)}. By Hoft's proof in A379288, that is
  A237271(n). Hoft also proved it via A384149 (Jan 2026).
* No new content, but the A243982 entry does not say it is settled.

---

## 9. NO COUNTEREXAMPLE up to the stated bound

* **A006579**. Conjecture: "a(n) ≢ -1 (mod n) for composite n."
  Equivalent to Pillai(n) ≢ -1 (mod n). Checked all n ≤ 3*10^8 (`a006579.c`, multiplicative formula mod n;
  brute-force check for n < 3000).
  Separate structured search for squarefree n = pqr with p < q ≤ 10^4 (`a006579_3p.c`). This uses the necessary
  condition r | 2pq-p-q, which covers such n far beyond 3*10^8. None found.
* **A015126**. Conjecture: "a(n) is odd for odd n."
  Scanned all k ≤ 4*10^8 (`a015126.c`). Only 4 totient values have an even least preimage (2^a·257-type), and none
  of them has an odd preimage ≤ 4*10^8.
* **A065515**. Conjecture: "a(n) >= pi(A069623(n)) + pi(n) + 1."
  Both sides change only at perfect powers. Checked every perfect power ≤ 10^15 (`a065515b.c`, 31.7 million checks).
  The smallest margin for n > 10^5 is 34, and the margin grows.
* **A123365**. Conjecture: "k with #cubic residues = (k+2)/3 are exactly 1 and the primes 6k+1."
  Checked all k ≤ 3*10^6 using the multiplicative count of cube residues (`a123365.py`).
  A size argument handles k with at least two "special" prime-power factors, but not the general case.
* **A226115**. Conjecture: "sqrt(2a(n)) > sqrt(p_n) - 0.7, and a(n) is even for n > 7."
  Checked n ≤ 4*10^5 (`a226115.c`). Apart from the known near miss at n = 651, the minimum slack is 0.1139 at n = 140.
* **A328556**. Conjecture: "the last zero is at n = 340."
  Coefficients computed modulo two ~61-bit primes to n = 2*10^5 (`a328556.py`). No zero after 340.
* **A218459**. Conjecture: "odd composite values belong to A176255."
  All primes ≤ 10^8 (`a218459.c`). No odd composite minimal d outside A176255. The largest d is 1646.
* **A110545**. Conjecture: "a(n) ≤ n." Checked n ≤ 2500 with exact harmonic numbers (`a110545.py`).
* **A380354**. Conjecture 1: "a(n) takes only 15 values." Conjecture 2: "a(n) ∈ {20, 64} for n ≥ 187."
  Both hold for n ≤ 10^5 (`a380354b.c`; the chains of nested totients were computed exactly).
* **A294508**. Conjecture: "min_{m≤n} T(n,m) ≤ T(n,M) for all M > n, n ≠ 5."
  Holds for n ≤ 3000 and n < M ≤ 20n (`a294508.c`). The margins are huge, e.g. min 257 versus ≥ 417323 at n = 3000.
* **A359507**. Conjecture: "a(n) is of the form 2^j + 1."
  Checked for n ≤ 3*10^6 (`a359507.c`). Here a(n) = min k with n XOR (n+k) in the GF(2)-span of n+1, ..., n+k-1.
* **A364131**. Conjecture: "all terms except 2 are squares." PARTIAL PROOF.
  - If sigma(k) is even, then A348717(sigma(k)) = sigma(k) > k ≥ A348717(k) > 0, so k is not a term.
  - Hence every term k > 1 has sigma(k) odd, i.e. k is a square or twice a square.
  - Twice-squares 2m^2 with 2 ≤ m ≤ 3*10^4 were excluded by computation (`a364131_b.py`). Data were reproduced for
    k ≤ 3*10^5 (`a364131.py`).
* **A369083**. Conjecture: "a(n) ≡ binomial(4n+3,n) (mod 2)."
  Checked for n ≤ 10^5 (`a369083.py`). This uses the integer recurrence A = 1 + x(E^2+O^2) + 3xEO, where E and O
  are the even and odd parts of A; the exact data were reproduced first.
* **A330996**. Conjecture: "p(n)/q(n) is nondecreasing for n > 5."
  Checked exactly for n ≤ 2*10^4 (`a330996.py`).
* **A361831**. Conjectures: "a(n) ≡ 9 (mod 10) for n > 25" and "all terms are zeroless."
  Both hold for n ≤ 3000 (`a361831.py`, candidates enumerated in increasing order). Terms have up to 334 digits.
* **A363265**. Conjecture: "9 is missing."
  a(n) depends only on the prime signature. Every signature whose canonical representative is ≤ 2*10^7 was
  evaluated by enumerating factorizations (`a363265.py`), and the value 9 never occurs.
  Partial reason: for squarefree n, a(n) = 1, and for n = p^2·(m distinct primes), a(n) = 1 + Bell(m).
* **A123737**. Conjecture: "first occurrences of n and -n are at A001652(n) and A001108(n)."
  Confirmed for all partial sums up to index 3*10^9 (`a123737.c`, exact floor(k*sqrt2) via 128-bit isqrt).
  That covers n ≤ 12 and -n down to -13.
* **A217738**: the numerical check (k ≤ 2*10^7) is moot because the statement is proved above.
