# Slice 1 results (agent 1)

Work dir: /home/user/work/agent1/ (one subdirectory per sequence). All counterexamples below were
checked with two independent implementations (different language and algorithm). Where a certificate
is given, it can be checked by hand or with one line of GP.

Note: the b-files in the local snapshot are git-LFS pointers, not data, so every "reproduced" check is
against the %S/%T/%U terms (plus cross-referenced sequences where noted).

---------------------------------------------------------------------------------------------------

## 1. A100682: COUNTEREXAMPLE (three new exceptions, far outside the listed set)

- Entry: a(n) = floor(C(n+3,4)^(1/4)) ("Floor of 4th root of pentatope numbers"), offset 0.
- Conjecture (Charles R Greathouse IV, May 01 2012), quoted: "Conjecture: a(n) = floor((n - 3/2)/24^(1/4))
  for n not in {0, 1, 6, 17, 2403, 5318}."
- Indexing remark: taken literally with the entry's offset, the formula fails at almost every n (e.g. n=2:
  a(2)=1 but floor(0.5/24^(1/4))=0). The exception list {0,1,6,17,2403,5318} is the correct list up to
  2*10^6 only when the pentatope index N = n+3 is used, i.e. for floor(binomial(N,4)^(1/4)) =
  floor((N-3/2)/24^(1/4)). That is plainly the intended statement, and it is the one refuted here.
- **Verdict: COUNTEREXAMPLE.** Three more exceptions exist:
  N = 634027531, 1705327318, 55292025086 (sequence indices n = N-3 = 634027528, 1705327315, 55292025083).
- Certificate for N = 634027531, with k = 286454273:
  - binomial(N,4) < k^4, so floor(binomial(N,4)^(1/4)) = k-1 = 286454272. GP also confirms
    binomial(N,4) >= (k-1)^4.
  - 384*k^4 <= (2N-3)^4, i.e. (N-3/2)/24^(1/4) >= k. Numerically, (N-3/2)/24^(1/4) =
    286454273.00000000034367...
  - One line of GP: `N=634027531;k=286454273;[binomial(N,4)<k^4, 384*k^4<=(2*N-3)^4]` returns [1,1].
  - The other two exceptions work the same way, with k = 770468590 and k = 24980992325.
- Why exceptions keep appearing: with m = N-3/2, binomial(N,4) = (m^4 - 5m^2/2 + 9/16)/24, so the 4th root
  is about m/c - 0.625/(m c), where c = 24^(1/4). An exception happens exactly when frac(m/c) < ~0.625/(m c),
  i.e. when k*c + 1/2 lies within about 0.625/N below an integer. This is an inhomogeneous Diophantine
  approximation condition. Its expected count grows like 0.28*ln(N), so infinitely many exceptions are
  expected; this is heuristic, not a proof.
- Search completeness: a 128-bit fixed-point scan over all k <= 2*10^11 (N <= 4.4*10^11) flagged every k with
  delta*N < 1, where delta = N - 3/2 - k*c; an exception needs delta*N < ~0.63. All flagged k were then
  checked exactly. So the complete list of exceptions with N <= 4.4*10^11 is
  {0, 1, 6, 17, 2403, 5318, 634027531, 1705327318, 55292025086}. The near misses k = 21, 82, 157 are not
  exceptions.
- Verification: (1) Python exact integer 4th roots (math.isqrt), plus a brute-force check of all N <= 2*10^5;
  (2) PARI/GP `sqrtnint(binomial(N,4),4)` against `floor((N-3/2)/24^(1/4))` at 115-digit precision, plus a GP
  brute-force check of all N <= 2*10^6, which reproduces exactly {6,17,2403,5318}.
- Code: /home/user/work/agent1/A100682/{scan.c, verify.py, verify.gp, check.py}
- Novelty: none of these numbers occurs anywhere in the local OEIS snapshot (grep), and the entry still
  lists only the six exceptions.

---------------------------------------------------------------------------------------------------

## 2. A284364 (and the same conjectures in A284365 / A284366): COUNTEREXAMPLE

- Entry: fixed point of the morphism 0->1, 1->101010 (Clark Kimberling, Mar 26 2017).
- Conjecture, quoted: "Let u(n) = # 0's <= n and v(n) = # 1's <= n. Let r = (9+sqrt(21))/6 and
  s = (-1+sqrt(21))/2, so that 1/r + 1/s = 1. Conjecture: -2 < n*r - u(n) < 2 and -1 < n*s - v(n) < 2
  for n >= 1."
  - Read literally ("# 0's <= n" as a count), n*r - u(n) is unbounded, so the statement would be trivially
    false.
  - The intended meaning, confirmed by the companion entries, is u(n) = position of the n-th 0 (A284365)
    and v(n) = position of the n-th 1 (A284366). Those entries state the same bounds:
    - A284365: "-2 < n*r - a(n) < 2"
    - A284366: "-1 < n*s - a(n) < 2"
- **Verdict: COUNTEREXAMPLE** to both upper bounds.
  - v: the smallest counterexample is n = 2977771, where the 2977771-th 1 is at position v(n) = 5334043,
    and n*s - v(n) = 2.00487217332612884794...
    Exact check: 21*n^2 > (2*v+4+n)^2 (both sides positive), i.e. n*sqrt(21) > 2v+4+n.
    Further violations up to 3*10^7 letters: n = 5409958, 6051478, 7672936, 7842145 (value 2.0367),
    7886776, 8483665, 14631079.
  - u: the smallest counterexample is n = 8933313, where the 8933313-th 0 is at position u(n) = 20222898,
    and n*r - u(n) = 2.00487217332612884794...
    Exact check: 21*n^2 > (6u+12-9n)^2 with 6u+12-9n > 0, i.e. n*r - u > 2.
    This is the only violation for zeros among the first 3*10^7 letters.
  - The lower bounds held on all 3*10^7 letters: min n*r - u(n) = -1.310, min n*s - v(n) = -0.795.
- The substitution matrix has eigenvalues (3 +/- sqrt(21))/2, which is Pisot, so the discrepancy is bounded.
  The true supremum is simply a little above 2 (at least 2.0367 for v).
- Verification (three independent runs):
  (1) numpy iterated-morphism generator with float check (kimberling/run.py, a284364.py);
  (2) C "self-reading" fixed-point generator with exact __int128 sqrt(21) comparisons
      (kimberling/verify284364.c), which reproduces the same first violations;
  (3) PARI/GP Vecsmall iteration, exact position lookup and exact inequality (kimberling/v284364.gp).
  The word's prefix matches the %S data of A284364, and the positions match the data of A284365/A284366.
- Novelty: the values 2977771, 5334043, 8933313, 20222898 do not occur in the OEIS snapshot (the grep hits
  were unrelated digit strings). A web search found nothing.

---------------------------------------------------------------------------------------------------

## 3. A071622: COUNTEREXAMPLE

- Entry: a(n) = (-1)*Sum_{k=1..n} (-1)^floor((4/3)^k) (Benoit Cloitre, Jun 22 2002).
- Conjecture, quoted: "Conjecture: for n>2300, a(n) > log(n)^2."
- **Verdict: COUNTEREXAMPLE.**
  - With log = ln: the first failure is n = 16954, where a(16954) = 94 and log(16954)^2 = 94.8337.
  - With log = log10: the first failure is n = 18860, where a = 18 and log10(18860)^2 = 18.28.
  - For any base: a(18966) = 0. The sequence then goes negative (a(60000) = -204), so it does not even
    satisfy the "nonn" keyword beyond the displayed terms.
- Computation: floor((4/3)^k) is computed exactly as 4^k \ 3^k with big integers. The cross-referenced sister
  sequence A071532 ((3/2)^k) had its positivity conjecture refuted in Sep 2026 (a(331523) = -1, S.
  Schlesinger); the (4/3)^k version was not touched there. Note that the entry's PARI program uses
  floating-point floor((4/3)^i), which becomes unreliable for large i.
- Verification: Python/gmpy2 exact computation (/home/user/work/agent1/A071622/t.py, t2.py), which
  reproduces the listed terms; and PARI/GP exact computation (v.gp), which gives a(16954) = 94 and a first
  zero after 2300 at k = 18966.
- Novelty: nothing in the entry or cross-references; a web search found nothing.

---------------------------------------------------------------------------------------------------

## 4. Kimberling discrepancy bounds already contradicted by the listed data (easy counterexamples)

These are weaker because the failure is visible in the displayed terms, but the conjectures are still
stated in the entries.

- **A285134** (positions of 0 in the 0-limiting word of 0->10, 1->0001).
  - Conjecture, quoted: "-1 < n*r - a(n) < 1 for n>=1, where r = 1 + sqrt(1/3)."
  - **COUNTEREXAMPLE at n = 2:** a(2) = 2 (in %S), and 2r - 2 = 2/sqrt(3) = 1.1547 > 1.
  - Up to 3*10^7 letters the observed range is [-2.2198, 3.0563].
- **A285143** (positions of 0 in the 1-limiting word of 0->10, 1->0010).
  - Conjecture, quoted: "-1 < n*r - a(n) < 1 for n>=1, where r = (3 + sqrt(3))/3."
  - **COUNTEREXAMPLE at n = 12:** a(12) = 20 (in %S), and 12r - 20 = 4*sqrt(3) - 8 = -1.0718 < -1.
  - Observed range up to 3*10^7 letters: [-1.3300, 1.8061].
- **A341249**: a(n) = floor(r*floor(s*n)), with r = 2+sqrt(2), s = sqrt(2).
  - Conjecture, quoted: "1 < r*s*n - a(n) < 2 for n >= 1."
  - **COUNTEREXAMPLE at n = 2:** a(2) = 6, and r*s*2 - 6 = 4+4*sqrt(2) - 6 = 3.657 > 2.
  - **PROOF of the correct statement.** Write f = frac(n*sqrt(2)) and F = floor(n*sqrt(2)). Then
    r*s = 2+2*sqrt(2), so r*s*n = 2n + 2F + 2f and r*F = 2n + 2F - sqrt(2)*f. Hence
    a(n) = 2n + 2F + floor(-sqrt(2)*f), and r*s*n - a(n) = 2f - floor(-sqrt(2) f). This equals 2f+1 when
    f < 1/sqrt(2) and 2f+2 when f > 1/sqrt(2); f = 1/sqrt(2) is impossible by irrationality.
    So r*s*n - a(n) lies in (1, 1+sqrt(2)) union (2+sqrt(2), 4), and it exceeds 2 exactly when f > 1/2,
    which happens for a set of n of density 1/2.
  - The same computation proves the sister conjecture in **A341239** (r = 1+sqrt(2), s = sqrt(2),
    "1 < r*s*n - a(n) < 3"): there r*s*n - a(n) = f + 1 or f + 2, which lies in
    (1, 1+1/sqrt(2)) union (2+1/sqrt(2), 3). So that conjecture is TRUE. (Easy.)
  - Both closed forms were checked numerically for n <= 20000 (kimberling/a341249.py).
- Code: /home/user/work/agent1/kimberling/{run.py, first.py}.

Other Kimberling bounds in this slice checked up to 3*10^7 letters with no violation found (observed
min/max in brackets):

| Entry | Conjectured bounds | Observed range |
|---|---|---|
| A026367 | (-1,2) | [-0.781, 1.572] |
| A045672 | (-1,3) | [-0.819, 2.459] |
| A284015 | (-1,2) | [-0.719, 1.280] |
| A284371 (read as -2 < n*sqrt(3) - a(n) < 3) | (-2,3) | [-1.990, 2.718] |
| A284655 | (-1,2) | [-0.995, 1.723] |
| A284679 | (-1,1) | [-0.697, 0.303] |
| A285035 | (-1,2) | [-0.646, 1.561] |
| A285276 | (-2,1) | [-1.9992, 0.9994] |
| A285343 | (-1,1) | [-0.9992, 0.9994] |
| A285360 | (0,2) | [0.0004, 1.414] |
| A285422 | (-1,5) | [-0.415, 4.285] |
| A287727 | (-1,1) | [-0.553, 0.447] |

Several of these sit right against their bounds and look like sharp, non-attained limits.

---------------------------------------------------------------------------------------------------

## Conjectures tested with no counterexample found

(Continued below.)
