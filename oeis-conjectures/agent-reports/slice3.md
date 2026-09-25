# Slice 3 report (agent 3)

Work directory: `/home/user/work/agent3/` (one sub-directory per A-number).
All counterexamples below were checked by at least two independent implementations
(C and PARI/GP and/or Python). None of them is mentioned in the entry or in any
local OEIS entry (grep of the 2026-09-24 snapshot). Web searches found no prior mention.

Summary of the strongest findings (details follow):

| A-number | Verdict | One-line certificate |
|---|---|---|
| A225577 (main conjecture) | COUNTEREXAMPLE | n = 2^30: a(n) = 49, but the conjecture predicts 61. 2^49-1 = 127*4432676798593 (prime > 2^31) |
| A225577 (Sun's Fibonacci conjecture, same entry) | COUNTEREXAMPLE | n = 1485607537 = (F(47)+1)/2: least Fibonacci modulus is F(65) = 5*233*14736206161 (composite), not F(83) |
| A114782 | COUNTEREXAMPLE | p = prime(4966) = 48247 == 1 (mod 3), yet 10^k+48247 is always divisible by 7, 11, 13 or 37, so a(4966) = 0 |
| A072872 | COUNTEREXAMPLE | a(6298) = 77742 > prime(6298) = 62753 (also n = 51169, 148755) |
| A126762 (Ordowski's conjecture) | COUNTEREXAMPLE | a(363) = 366 (gcd 3), but the least k > 363 with 363^(k-1) == 1 (mod k) is 367 |
| A074882 (R. Israel, Aug 10 2026) | PROOF | a(n) = sigma(n)phi(n)/n + E with E < 2^(omega-1) <= n - sigma(n)phi(n)/n |
| A222014, A375439, A361035 | PROOF (easy) | parity / 2-adic arguments |
| A289921, A289261, A182336, A123723, A277030, A286348 | PROOF (easy) | see below |

---------------------------------------------------------------------------

## 1. A225577: COUNTEREXAMPLES to both conjectures in the entry

**Entry.** A225577 "Least integer m>1 such that 1^2,2^2,...,n^2 are pairwise incongruent modulo 2^m-1."
(Zhi-Wei Sun, May 10 2013). Comments in the entry:

* (C1) "Conjecture: a(n) is the least prime p such that 2^p-1 is a Mersenne prime greater than 2n-1."
  ("This conjecture implies that there are infinitely many Mersenne primes.")
* (C2) "Zhi-Wei Sun also conjectured that for each n>17 the least Fibonacci number modulo which
  1^2,2^2,...,n^2 are pairwise incongruent is just the first Fibonacci prime greater than 2n-1."

### Verdict for (C1): COUNTEREXAMPLE. Smallest counterexample n = 2^30 = 1073741824, where a(n) = 49 but (C1) predicts 61.

**Certificate (checkable by hand/one line of GP).**
* 2^49 - 1 = 127 * 4432676798593, and q = 4432676798593 is prime (`isprime(4432676798593)`).
* Take n = 2^30. If i^2 == j^2 (mod 2^49-1) with 1 <= i < j <= n, then q | (j-i)(j+i). But
  0 < j-i < j+i <= 2^31 - 1 < q, so this is impossible. So 1^2,...,n^2 are pairwise incongruent
  modulo 2^49-1, and a(2^30) <= 49.
* (C1) predicts a(2^30) = 61: 2n-1 = 2^31-1 = M31 is itself a Mersenne prime and is not "greater than 2n-1".
  The next Mersenne prime is M61. (Mod M31 the squares collide: (2^30)^2 - (2^30-1)^2 = 2^31-1.)
  Also, no Mersenne-prime exponent p < 61 can be a(2^30): for prime M = 2^p-1 <= 2^31-1 we have
  j = (M+1)/2 <= 2^30, i = (M-1)/2, and i+j = M.
* In fact a(2^30) = 49 exactly. For every m in [2,48] there is an explicit collision with j <= 2^30
  (listed by `a225577/cert2.gp`; e.g. m=37: 308159200^2 == 308158977^2 (mod 2^37-1),
  m=47: 11937296^2 == 1327233^2 (mod 2^47-1)).

**Exact description.** For odd M (here M = 2^m-1, which is never a square), 1^2,...,n^2 are
pairwise distinct mod M iff n < F(M) := min over d | M with d < M/d of (d + M/d)/2.
(Proof: a collision is a pair u = j-i < v = j+i of the same parity with M | uv; with d = gcd(u,M)
one gets d | u and M/d | v, so u+v >= d + M/d, and (u,v) = (d, M/d) itself is a collision.)
Hence a(n) = least m with F(2^m-1) > n. Using the factorizations of 2^m-1 (m <= 64):
* a(n) agrees with (C1) for all n < 2^30;
* a(n) = 49 for 2^30 <= n <= 2216338399359 = (127 + 4432676798593)/2 - 1, while (C1) gives 61
  for this whole range (F(59) = 1601715980144 is smaller).

**Independent verifications.**
1. Algebraic certificate above (factorization + primality in PARI; `a225577/cert.gp`, `cert2.gp`).
2. Brute force in C (`a225577/verify.c`): all 2^30 squares k^2 mod (2^49-1) were computed
   (incrementally, k^2 = (k-1)^2 + 2k - 1), split into 64 hash buckets, each bucket sorted.
   Result: 1073741824 residues, 0 duplicates (`verify_m49.out/.err`).
   The same program reproduces the exact thresholds, e.g. for 2^37-1 it finds a duplicate for
   N = 308159200 and none for N = 308159199, matching F(2^37-1) = 308159200.
3. Separate brute force (`a225577/brute.c`, sorting residues) reproduces all 70 data terms
   and agrees with the F-formula for every n <= 5000. (The b-files in the snapshot are Git-LFS
   stubs, so only the %S/%T/%U data could be compared.)

### Verdict for (C2) (Fibonacci version): COUNTEREXAMPLE. Smallest counterexample n = 1485607537 = (F(47)+1)/2.

**Certificate.**
* F(65) = 17167680177565 = 5 * 233 * 14736206161, with q = 14736206161 prime and q > 2n = 2971215074.
  As above, a collision mod F(65) with i < j <= n needs q | (j-i)(j+i), which is impossible.
  So 1^2..n^2 are pairwise incongruent modulo the composite Fibonacci number F(65).
* F(47) = 2971215073 is prime and 2n-1 = F(47), so the first Fibonacci prime greater than 2n-1 is
  F(83) = 99194853094755497, which is what (C2) predicts. Every F(k) with k <= 64 fails: for F(47)
  take j = n, i = n-1 (i+j = F(47)); for the other k an explicit collision with j <= n is produced
  by `a225577/fib/cert.gp`. So the least Fibonacci modulus is F(65), not F(83).
* For general m (also even m) I used H(m) = least j having a collision = min over d | m and small
  multiples s,t of (ds + (m/d)t)/2 over same-parity pairs ds < (m/d)t. With H(F(k)) for k <= 100
  (`fib/H.txt`), (C2) holds for 18 <= n < 1485607537 and fails for all
  1485607537 <= n <= 46090235747454 (least modulus F(65), then F(71), then F(79)).

**Independent verification.** A C brute force (`fib/verify_F65.*`) computed all 1485607537
squares mod F(65): 0 duplicates.

**Novelty.** No other OEIS entry refers to A225577 and no Fibonacci version has its own entry.
Web searches (Sun's paper arXiv:1304.5988 / JNT 2015, OEIS pages) found no mention that
(C1) or (C2) fails. (C1) is claimed to imply infinitely many Mersenne primes; it simply fails
because 2^49-1 has only one small factor.

---------------------------------------------------------------------------

## 2. A114782: COUNTEREXAMPLE

**Entry.** "Smallest prime of the form 10^k + prime(n), k >= d, the number of digits in prime(n).
0 if no such primes exist." Comment: "Conjecture a(n) = 0 iff prime(n) + 1 == 0 (mod 3)."
(Amarnath Murthy, Nov 17 2005; more terms by Joshua Zucker.)

**Verdict: COUNTEREXAMPLE**, n = 4966 with prime(4966) = 48247. Here 48247 == 1 (mod 3),
so prime(n)+1 is not divisible by 3, but a(4966) = 0.

**Certificate (covering set {7, 11, 13, 37}).** The order of 10 is 6 mod 7, 2 mod 11, 6 mod 13
and 3 mod 37, so 10^k mod each of them depends only on k mod 6:

| k mod 6 | prime dividing 10^k + 48247 |
|---|---|
| 0 | 37 |
| 1 | 11 |
| 2 | 13 |
| 3 | 11 (and 37) |
| 4 | 7 |
| 5 | 11 |

Every 10^k + 48247 (k >= 0) is larger than 37, so all are composite and no admissible prime exists.
GP one-liner:
`for(r=0,5,print(r," ",[q|q<-[7,11,13,37],(10^r+48247)%q==0]))`.

**Verification.** (1) PARI (`a114782/cert.gp`): the table above, `isprime(48247)`, `primepi(48247)=4966`,
and a direct check that each of the 2996 numbers 10^k+48247 with 5 <= k <= 3000 has a factor in {7,11,13,37}.
(2) An independent Python/sympy scan over all primes up to 2*10^6 lists the primes p == 1 (mod 3)
covered by {7,11,13,37}: 48247, 56473, 135937, 149269, 358159, ... (31 primes below 2*10^6),
so there are many more counterexamples.
The "if" direction of the conjecture is trivially true (p == 2 (mod 3) gives 3 | 10^k+p).

**Is 48247 the smallest counterexample?** It is the smallest one with a proof. Every prime p < 48247 with p != 2 (mod 3) has a
probable prime 10^k+p with d <= k <= 2500 (`small.gp`, then the sieved search `sieve_search.py`), except these 8
low-weight values: 2971, 9811, 15817, 20089, 25609, 28909, 33331, 35839. For each of them I ran an exact test for a
covering with period L: class r mod L is covered iff gcd(10^r+p, 10^L-1) > 1. No covering exists with any period
L <= 1000 (`covgcd.py`). The same test finds period 6 for 48247. So 48247 is the smallest prime counterexample that
has a covering-set proof. The 8 values above are undecided, but almost certainly have a prime at larger k.

**Novelty.** Nothing in the entry says this. 48247 appears in A243969 (j*10^k+1 covered by
{7,11,13,37}), which is the "dual" form: q | 48247*10^k+1 iff q | 10^(-k)+48247. So the covering itself
is known in the dual Sierpinski setting (also in a covering-set table in arXiv:1903.05023), but it was not
connected to A114782's conjecture.

---------------------------------------------------------------------------

## 3. A072872: COUNTEREXAMPLE

**Entry.** "a(n) is the smallest positive number k such that n divides 2^k - k." Comment:
"If n is a power of 2, a(n) = n. Conjecture : if n > 47, a(n) < prime(n)." (Benoit Cloitre, Jul 28 2002;
b-file to n = 1000.)

**Verdict: COUNTEREXAMPLE.** For 47 < n <= 10^6 exactly three n violate the bound:

| n | factorization | a(n) | prime(n) |
|---|---|---|---|
| 6298 | 2*47*67 | 77742 | 62753 |
| 51169 | prime | 857178 | 627619 |
| 148755 | 3*5*47*211 | 2255896 | 1997459 |

Certificate: `k=77742; Mod(2,6298)^k==k` is true, `prime(6298)=62753`, and no k < 77742 works.
**Verification:** (1) C program (`a072872/c.c`) that, for every n <= 10^6, searches k < prime(n) with
2^k == k (mod n) (it reproduces the 73 data terms). (2) The entry's own PARI program
`a(n)=for(k=1,oo,if(Mod(2,n)^k==k,return(k)))` gives a(6298)=77742, a(51169)=857178,
a(148755)=2255896 (`v.gp`, `v2.gp`). (3) A Python `pow(2,k,n)==k%n` scan gives the same values.
Heuristically n | 2^k-k holds with density about 1/n in k, so P(a(n) > prime(n)) is about 1/(n log n).
The sum of this diverges like log log n, so there should be infinitely many exceptions.

---------------------------------------------------------------------------

## 4. A126762: COUNTEREXAMPLE to Ordowski's conjecture

**Entry.** "a(n) is the least k > n such that the remainder when n^k is divided by k is n."
Comment: "a(n) is the smallest number k > n such that n^k == n (mod k). Conjecture: a(n) is the smallest
number k > n such that n^(k-1) == 1 (mod k). Thus a(n) is coprime to n." (Thomas Ordowski, Aug 03 2018)

**Verdict: COUNTEREXAMPLE**, n = 363: a(363) = 366 and gcd(363, 366) = 3. The least k > 363 with
363^(k-1) == 1 (mod k) is 367.

Hand certificate: 366 = 2*3*61. 363 == 1 (mod 2); 363 == 0 (mod 3); 363 == -3 (mod 61) and
(-3)^366 == (-3)^6 = 729 == -3 (mod 61). So 363^366 == 363 (mod 366). For k = 364: 363 == -1 and
(-1)^364 = 1 != -1. For k = 365: mod 73, 363 == -2 and (-2)^365 == (-2)^5 = -32 == 41 != -2.
So a(363) = 366. Since 3 | gcd(363,366), 363^365 cannot be == 1 (mod 366), and 367 is prime.
**Verification:** C (`a126762/c.c`, reproduces the 74 data terms) and PARI (`a126762/v.gp`,
independent definitions of both versions). Up to 10^6 there are 163 such n: 363, 801, 2115, 3145, 4535,
5537, 6923, 7375, 7929, ... (`c1e6.out`). Note that 363 and 801 lie inside the range of Harvey Dale's
b-file (n <= 996), so the b-file very likely already shows a(363)=366, but the entry never notes that
the conjecture fails.

---------------------------------------------------------------------------

## 5. A074882: PROOF of Robert Israel's conjecture (Aug 10 2026)

**Statement.** A074882: a(n) = #{1 <= k <= sigma(n): gcd(k,n)=1}. "a(n) <= n, with equality if n is in
A000961. Conjecture: a(n) < n if n is not in A000961." - Robert Israel, Aug 10 2026.

**Proof.** Let n > 1, n = prod_{i=1..w} p_i^{e_i}, s = sigma(n). By inclusion-exclusion,
a(n) = sum_{d|n} mu(d) floor(s/d) = s*phi(n)/n - sum_{d|n} mu(d) {s/d}.
Put E = -sum_{d|n} mu(d){s/d}. The terms with mu(d) = +1 contribute <= 0 and each {.} < 1, so
E < #{d | n : mu(d) = -1} = 2^(w-1).
Also s*phi(n)/n = n * prod_i (1 - p_i^{-(e_i+1)}), so G := n - s*phi(n)/n = n(1 - prod_i(1 - x_i)) with
x_i = p_i^{-(e_i+1)}. Then a(n) = n - G + E, and it is enough to show G >= 2^(w-1) when w >= 2.
* w = 2, n = p^a q^b (p < q): G = q^b/p + p^a/q - 1/(pq) >= q/p + p/q - 1/(pq)
  = 2 + ((q-p)^2 - 1)/(pq) >= 2.
* w >= 3: 1 - prod(1-x_i) >= x_1, so G >= n/p_1^{e_1+1} >= (p_2 p_3 ... p_w)/p_1 > p_3...p_w >= 5^{w-2} >= 2^{w-1}.
So a(n) < n. QED. (For prime powers a(p^e) = s - floor(s/p) = p^e, as the entry states.)
Numerical check: `proofs/a074882.gp` confirms a(n) < n for all non-prime-powers n <= 2*10^5, and
G >= 2^(omega-1) for all of them.

---------------------------------------------------------------------------

## 6. Easy proofs (short, complete; labelled easy)

* **A222014** (Hanna, Dec 2024: "a(n) is odd iff n = 2^k - 1"). **PROOF (easy).** Reduce the functional
  equation mod 2. For n >= 2 the summand has the factor n! == 0 and is otherwise in Z[[x]] (its denominator
  has constant term 1). So A == 1 + xA/(1+xA), i.e. A + xA^2 == 1 (mod 2). The Catalan g.f. C = 1 + xC^2
  satisfies the same equation, and that equation determines the coefficients recursively, so A == C (mod 2).
  Cat(n) is odd iff n+1 is a power of 2, since v_2(Cat(n)) = s_2(n+1) - 1. Checked numerically for n <= 40.
* **A375439** ("a(n) odd iff n in A038754 = {3^k, 2*3^k}"). **PROOF (easy).** Work in Z_(2)[[x]].
  1/3 == 1 and 2/3 == 0 mod 2, so A == x + x^2 + A(x^3) (mod 2), giving A == sum_k (x^{3^k} + x^{2*3^k}).
  Checked for n <= 250.
* **A361035** ("a(n) odd iff n = 2^k - 3"). **PROOF (easy).** With v_2(m!) = m - s_2(m) and v_2(9979200) = 6:
  v_2(a(n)) = 6 + (4n - s(n)) - (n - s(n)) - 3(n+3 - s(n+3)) = 3 s_2(n+3) - 3. This is 0 iff n+3 is a power of 2.
* **A289921** ("all terms nonnegative", Kimberling). **PROOF (easy).** Because floor(1+(k+1)9/10) = k+1 for
  k <= 9 and increases by 9 every 10 steps, the g.f. equals (1+x)^2(1-x^10)/(1-2x^10-x^11). This was checked
  against the definition to x^300 and matches the data. Let b_n = [x^n](1+x)^2/(1-2x^10-x^11) >= 0; then
  b_n = 2b_{n-10} + b_{n-11} for n >= 3, and a_n = b_n - b_{n-10} = b_{n-10} + b_{n-11} >= 0 for n >= 10,
  while a_n = b_n for n < 10.
* **A289261** ("strictly increasing", Kimberling, r = 13/8). **PROOF (easy, computer-assisted).**
  The differences have g.f. (1-x^2)(1-x^8)/Q(x) with Q = 1-2x+x^2-2x^3+2x^4-x^5+2x^6-2x^7. Q has a simple
  dominant reciprocal root 1.76404... and all other reciprocal roots have modulus <= 1.07853. The
  partial-fraction expansion (134-digit precision) shows the dominant term exceeds the sum of the other
  terms for all n >= 5, and d(1..399) > 0 exactly (`proofs/a289261b.gp`).
* **A182336** (Greathouse: "for n > 96, n+1 <= a(n) <= 9n/8+1"). **PROOF (easy).** The lower bound is
  trivial. Let t >= 3 be the least position with bit t of n equal to 0. Bits 3..t-1 of n are 1, so
  n >= 2^t - 8. If t >= 6, set bit t and clear bits t-1, t-2, t-3: m = n + 2^(t-3) <= n/8 + 1 + n with
  D(n,m) = 4. If t in {3,4,5}, a 4-bit flip gives m - n <= 15, 11 or 9, which is <= n/8+1 for n >= 112.
  The cases 97 <= n <= 111 were checked directly (also all n <= 3*10^5; `a182336/c.py`).
* **A123723** (Layman: "if n>4 and a(n) is a multiple of 4 then a(n)/4 is prime"). **PROOF (easy).**
  For N = 4m with m odd, A000224(N) = 2*A000224(m). For odd m, A000224(m) = prod A000224(p^e) <= (m+1)/2,
  with equality iff m is prime: A000224(p^e) < (p^e+1)/2 for e >= 2, and (x+1)(y+1)/4 < (xy+1)/2 for x,y >= 3.
  For 8 | N the formula a(2^e) = floor(2^e/6)+2 gives A000224(N) < N/4 + 1 except for N = 8.
* **A277030** ("a(n) > A002322(n) only for n = 8 and 24"). **PROOF (easy).** b^m == b^phi(n) for all b holds iff
  lambda(n) | m - phi(n) and m >= e_max(n), the largest exponent in n. Since lambda | phi, a(n) is the least
  multiple of lambda(n) that is >= e_max(n). So a(n) > lambda(n) iff e_max(n) > lambda(n). That happens only
  for e_max = 3 at the prime 2 with lambda(n) = 2, i.e. n | 24 and 8 | n, so n = 8 or 24.
* **A286348** ("if (1+y)^x + (-y)^x is prime then x = 0, an even power of 2, or an odd prime"). **PROOF (easy).**
  This is the usual algebraic factorization of a^x + b^x (x even with an odd factor > 1) and of a^x - b^x
  (x odd composite). The case y <= -1 reduces to z = -1-y >= 0.
* **A300657** ("a(n) = A054024(n) only for noncomposites"). Trivial: for composite n the proper divisor d = lpf(n)
  adds sigma(d) mod d = 1.
* **A143772** (Wilson: "the only odd terms are 1 and 3"). Easy: for odd terms m is even, and the gcd divides
  both (1+m) and (2+m/2), hence divides 2(2+m/2) - (1+m) = 3. (The "all even numbers occur" half is not treated.)
* **A060264** (Greathouse: least prime p with 1^2..n^2 distinct mod p is nextprime(2n), n > 2). Easy: for prime
  p <= 2n-1, take i = (p-1)/2, j = (p+1)/2; for p > 2n-1 we have 0 < j-i < j+i < p.
* **A328959** (all terms >= 0 except a(1)). Easy: with e_i = 1 + y_i,
  prod(2+y_i) >= 2^k + 2^{k-1} sum y_i >= k^2 - k + 2 + k sum y_i, since 2^k >= k^2-k+2 and 2^(k-1) >= k.
  This is exactly sigma_0(n) >= 2 + (Omega(n)-1)*omega(n).
* Trivial cases (already obvious from elementary congruences): A034496 (1+2^n+4^n+8^n = (1+2^n)(1+4^n)),
  A098016 (the mean of consecutive odd primes lies strictly between them), A112041/A177680 (mod-5 argument),
  A136050 (p(p+2) = (p+1)^2 - 1 with 3 | p+1), A233656 (a(n) = n + (3^n+1)/2, so the last digit has period 20, and the stated block is a(0..19)), A230168, A231329
  (19/4 == -1 (mod 23) forces n odd; then algebraic factorization forces n prime), A390088.

---------------------------------------------------------------------------

## 7. Tested, no counterexample found

| A-number | Conjecture | Result |
|---|---|---|
| A214074 | a(n)=3 iff n == 121 (mod 330) (Kimberling) | NO COUNTEREXAMPLE for n <= 10^5 (GMP gcds, data reproduced; `a214074/`). Exactly 303 n have a(n)=3, and they are exactly the n == 121 (mod 330). Side remark: a(86668) = 4 is the first value > 3 (PARI-confirmed), which is outside the scope of the conjecture |
| A338472 | (1+sum_{k even<n} 2k^(n-1))/n is an integer iff n is an odd prime (Rotondo) | NO COUNTEREXAMPLE for odd 3 <= n <= 10^5 (direct O(n log n) check per n; `a338472/`). Even n give odd/even, never an integer. The degenerate n = 1 gives the empty sum and 1/1 |
| A051924 | a(n) mod n^2 = n+2 iff n is an odd prime (Detlefs) | NO COUNTEREXAMPLE for 3 <= n <= 150000 (C(2n,n) mod n^2 via prime factorization; `a051924/`) |
| A227202 | a(n) < prime(n*e) (R. G. Wilson v) | NO COUNTEREXAMPLE for n <= 10^5 with prime(floor(n e)), data reproduced (`a227202/`). Heuristically a(n)/prime(n e) tends to e^-1/Artin = 0.984 |
| A294646 | (1/2)^(2n) mod (2n+1) is never 2, 2n, 2n-2 | Values 2 and 2n are impossible: 2^m == 1 (mod m) has no solution m > 1, and a v_2-of-orders argument rules out 2^(m-1) == -1. The value 2n-2 means m | 3*2^(m-1)+1 with m = 2n+1, which is impossible for prime m. NO COUNTEREXAMPLE for n <= 10^8 (`a294646/c.c`, which checks all three forbidden values) |
| A279884 | (n-1)^(n+1)+1 prime => n prime | Reduction by algebraic factorization: a composite counterexample must be n = 2^s-1. PRP-tested s = 4,6,8,9,10,11,12: all composite, plus direct check n <= 300. NO COUNTEREXAMPLE for n <= 4095 |
| A302092 | only semiprimes are 4 and 25 | Equivalent to: no Bell prime B(n), n > 3, has a prime digit reversal. The reversals of all known Bell primes B(7), B(13), B(42), B(55), B(2841) are composite |
| A217497 / A243958 | 2^p-1 not prime for primes p = 2n^2+54n+25 (resp. 2n^2+86n+41, except 521) | None of the 52 known Mersenne exponents has either form, except 521 |
| A346154 | a(n) > 0 unless n == 1 (mod 3) | No covering-type obstruction for n <= 3*10^7: for every such n some k <= 80 gives an n^k+n+1 without a prime factor < 300 and without the algebraic factor n^2+n+1 |
| A331234 | only 5 terms | Equivalent to: Pell(k) and the companion half-Pell A001333(k) are both prime. The known index lists intersect only in {2,3,5,29,59}. No new information |
| A372457, A000224, A349459, A392775, A248035, A248197 | various | Already verified far (10^3 .. 10^8 per the entries). Heuristics make failure unlikely, so skipped |

## 8. Code / data locations

* A225577: `/home/user/work/agent3/a225577/` (`f.gp` F(m) table, `cert.gp`, `cert2.gp`, `brute.c`, `verify.c`,
  `verify_m49.out/.err`). Fibonacci version: `a225577/fib/` (`h.gp`, `H.txt`, `cert.gp`, `verify_F65.out/.err`)
* A114782: `/home/user/work/agent3/a114782/` (`cert.gp`, `small.gp`, `cover.gp`, `sieve_search.py`, `sieve.out`, `covgcd.py`)
* A072872: `/home/user/work/agent3/a072872/` (`c.c`, `c1e6.out`, `v.gp`, `v2.gp`)
* A126762: `/home/user/work/agent3/a126762/` (`c.c`, `c1e6.out` = all 163 exceptions <= 10^6, `v.gp`)
* Proofs: `/home/user/work/agent3/proofs/` (`a074882.gp`, `par.gp`, `a289921.gp`, `a289261b.gp`, `misc.gp`),
  `/home/user/work/agent3/a182336/c.py`
* Other tests: `a214074/`, `a338472/`, `a051924/`, `a279884/`, `a302092/`, `a346154/`, `a227202/`, `a294646/`
