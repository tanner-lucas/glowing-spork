# Slice 5 report (agent 5)

Work dir: `/home/user/work/agent5/`. All heavy runs were single-core under `nice -n 10`. The b-files in the local snapshot are git-LFS pointers, so every check below was recomputed from the definitions and cross-checked against the %S/%T/%U data.

## Summary (strongest first)

| A-number | Verdict | One-line certificate |
|---|---|---|
| **A220956** | **COUNTEREXAMPLE** (substantive, double-verified) | n = 283686649 = 16843^2 is composite but a(n) = 0: C(2n,n) ≡ 2 and C(2n-2,n-1) ≡ n^2-n (mod n^2) |
| A285140 | COUNTEREXAMPLE (trivial, already visible in the data) | a(2)=2, and 2r-2 = 2/sqrt(3) = 1.1547 > 1. Exact extremes: inf D = -4/3, sup D = 1.8214 |
| A285129 | COUNTEREXAMPLE (trivial, in data) + PROOF that no bounds can hold | a(2)=4, and 2r-4 = -1.219 < -1. The substitution is not Pisot (λ2 = (1-√17)/2), so D(n) → -∞ along n = #0(σ^j(0)) |
| A327136 | COUNTEREXAMPLE to the literal statement + PROOF of the intended one | π·1 - a(1) = π - 1 = 2.14. Proved: a(n) = floor(nπ - π/4 - 1/2), so the constant is π/4+1/2 = 1.28540 |
| A096127 | **PROOF** (short, elementary) | a(n) = n+1 ⇔ n is a prime power, via digit sums: s_p(n^2) ≤ s_p(n)^2 |
| A001953 / A049473 (ζ(3) claim) | **PROOF** (elementary with explicit error terms; small n by 50-digit check) | tight cases are the Pell n with p^2 - 2n^2 = -1, where the margin is ~1/(3n^4) > 0 |
| A215926 | PROOF of **equivalence** with an open problem | "a(n) ∈ {1,3,2^k}" ⇔ "every almost perfect number (σ(k)=2k-1) is a power of 2". Also proves the second conjecture (first 2^m at nextprime(2^m)) given the same hypothesis |
| A287724 | PROOF (by hand) | D(n) = 2·frac(n/φ^2) - f(n) ∈ (0, 2/φ) |
| A283966 (u and v), A284369 (u and v), A284676, A284773, A284902, A284945, A285032, A285210, A285419, A285670 | PROOF (computer-assisted: exact Dumont–Thomas extremal DP at 60 digits, cross-checked by brute force to length 2·10^9) | exact inf/sup lie strictly inside the stated bounds (table below) |
| A284369 (v), A284931, A285084, A026363 | HOLDS (inf or sup equals the bound to 55+ digits; D(n) is irrational, so the bound is never attained) | same method |
| A091713, A396099 (all 3 mod-4 conjectures + parity), A374570, A177775, A389540, A368633, A378575, A380678 | PROOF (easy: identify the g.f. mod 2 or mod 4) | see §5 |
| A140869, A308090, A135953 | PROOF (easy, elementary) | see §6 |
| A023887 | PARTIAL: reduced to showing Φ_{p^p}(p) is composite for primes p ≡ 3 (mod 4), p ≥ 19 | explicit factors of sigma_n(n) for n = 9, 7^6, 11^10; n = 625 fails BPSW |
| A294509 | NO COUNTEREXAMPLE for n ≤ 1500, m ≤ 2·10^5 | only the known exception n=5 (m=7) |
| A356490 | NO COUNTEREXAMPLE for n ≤ 525 | no PRP |det| for 5 ≤ n ≤ 525 |
| A217499, A217621, A243888 | NO COUNTEREXAMPLE among all 52 known Mersenne prime exponents | only p=107, the stated exception of A243888 |
| A090698, A249902 | NO COUNTEREXAMPLE among the known terms of A050414, and of A028491/A003306/A003307 | |
| A394752 (octal .404) | INCONCLUSIVE | Grundy values keep growing (max 256 by n=20000), so the periodicity theorem does not apply |

---

## 1. A220956: COUNTEREXAMPLE

**Entry:** a(n) = (C(2n,n) - C(2n-2,n-1)) (mod n^2) - n - 2 (Gary Detlefs & Robert G. Wilson v, Feb 20 2013).
**Conjecture (quoted):** "Conjecture: a(n) = 0 iff n is an odd prime."

**Counterexample:** n = 283686649 = 16843^2 (composite). a(n) = 0.

* C(2n,n) mod n^2 = 2
* C(2n-2,n-1) mod n^2 = 80478114537162552 = n^2 - n
* C(2n,n) - C(2n-2,n-1) ≡ 2 - (n^2 - n) ≡ n + 2 (mod n^2), so a(n) = (n+2) - n - 2 = **0**.

**Why (proof of an exact characterization).** Put X = C(2n-1,n-1). Then C(2n,n) = 2X and (2n-1)·C(2n-2,n-1) = n·X. Since 2n-1 is a unit mod n^2, a(n)=0 (for n ≥ 3) is equivalent to X(3n-2) ≡ (n+2)(2n-1) ≡ 3n-2 (mod n^2), i.e. (3n-2)(X-1) ≡ 0 (mod n^2). For odd n this means **X ≡ 1 (mod n^2)**. So the odd zeros of A220956 are exactly the odd primes (Babbage) together with the composite terms of **A267824** (283686649, 4514260853041 = 2124679^2, …). 16843 is a Wolstenholme prime: C(2p,p) ≡ 2 (mod p^4) (one-line GP: `p=16843;Mod(binomial(2*p,p),p^4)` returns 2). By Jacobsthal's congruence, C(2p^2,p^2) ≡ C(2p,p) (mod p^6), so C(2n,n) ≡ 2 (mod n^2) for n = p^2.

**Verification (two independent programs):**
1. `a220956/direct.c`: exact GMP `mpz_bin_uiui` binomials (C(2n,n) has 567,373,284 bits), reduced mod n^2. Output: `a(n) = 0`, `C(2n-1,n-1) mod n^2 = 1` (`direct_283686649.out`, 67 s).
2. `a220956/padic.c`: independent p-adic factorial algorithm. It computes N! = p^{v_p(N!)}·U(N) with U(N) = ∏_{k≤N, p∤k} k · U(⌊N/p⌋) mod p^4 in 128-bit arithmetic, and was validated against PARI on random cases. Output (`padic.out`): C(2n,n) ≡ 2, C(2n-2,n-1) ≡ 80478114537162552, C(2n-1,n-1) ≡ 1 (mod 16843^4). Combined in GP, this gives a(n) = 0.
3. Sanity check: `a220956/small.gp` reproduces the data, and a(n) = 0 for n ≤ 3000 happens only at odd primes.

**Novelty:** The A220956 entry has no comment or cross-reference to A267824, A088164 or Wolstenholme primes. The number 283686649 appears in the local OEIS only in A267824. Web searches for "A220956" and "283686649" together with the conjecture found no prior mention. The next counterexample is n = 2124679^2 (by the same argument; McIntosh 1995).

## 2. Trivially false Kimberling / Beatty-type bounds

* **A285140** (Kimberling, Apr 20 2017): "Conjecture: -1 < n*r - a(n) < 1 for n>=1, where r = (3 + sqrt(3))/3." Here a(2) = 2 (data), and 2r - 2 = 2/√3 = 1.1547 > 1. Up to n = 136384 there are 7213 violations. The exact extremes (§4 method) are inf = -4/3 and sup = 1.82137. Brute force to length 2·10^9 gives min -1.3293 and max 1.8201. *Novelty:* not mentioned in the entry. Trivial, and possibly a typo in the bounds.
* **A285129** (Kimberling, Apr 19 2017): "Conjecture: -1 < n*r - a(n) < 1 for n>=1, where r = 1.3903..." Here a(2) = 4, and 2r - 4 = -1.2192. **Proof that no constant bounds hold:** σ: 0→10, 1→0000 has matrix [[1,4],[1,0]] with eigenvalues (1±√17)/2, and |λ2| = 1.56 > 1. Every σ^j(0) (j ≥ 1) ends in 0, and for odd j it is a prefix of the 1-limiting word A285128. Let h(x0,x1) = r·x0 - (x0+x1). It vanishes on the Perron vector, so it is a left λ2-eigenvector. Hence at n = N_j = #0(σ^j(0)) we get D(N_j) = h(M^j e0) = (r-1)λ2^j → -∞ (j odd). Brute force: min D = -23041.7 by n = 8.3·10^8. The sibling entries A285126, A285127 and A285130 (other slices) have the same defect.
* **A327136** (Kimberling, Aug 23 2019): "Conjecture: 1.285 < n*Pi - a(n) < 1.286 for n >= 1." This is literally false: n = 1 gives π - 1 = 2.14 (and nπ - a(n) is never in that window for n ≤ 14). **Proof of the intended statement a(n) = floor(nπ - c), c = π/4 + 1/2 = 1.285398…:** sin(2k+4) - sin(2k+2) = 2cos(2k+3)sin 1 and sin(2k) - sin(2k+2) = -2cos(2k+1)sin 1. So k is a term iff cos(φ+1) > 0 and cos(φ-1) < 0 with φ = 2k+2. Within one period this means φ ∈ (3π/2 - 1, 3π/2 + 1) (mod 2π), i.e. k ∈ (π(m+3/4) - 3/2, π(m+3/4) - 1/2). These are open intervals of length 1 with irrational endpoints, so each contains exactly one integer. Hence a(n) = floor(nπ - π/4 - 1/2) and π/4 + 1/2 < nπ - a(n) < π/4 + 3/2. This matches the data.

## 3. A096127: PROOF

"Conjecture: a(n)=n+1 only when n is prime or a power of a prime. [Verified for n=2..5000. - Amiram Eldar, Apr 06 2021]", where a(n) = max k with (n!)^k | (n^2)!.

a(n) = min_{p≤n} ⌊R_p⌋ with R_p = v_p((n^2)!)/v_p(n!) = (n^2 - S)/(n - s), where s = s_p(n) and S = s_p(n^2) are base-p digit sums (Legendre). Digit sums are submultiplicative, so S ≤ s^2. Also s < n for p ≤ n.
* R_p ≥ n+1 ⇔ S ≤ n(s-1)+s, which holds because s^2 ≤ n(s-1)+s ⇔ s(s-1) ≤ n(s-1).
* R_p < n+2 ⇔ S > n(s-2)+2s. With S ≤ s^2: for s = 2 this needs S > 4 ≥ S, impossible. For s ≥ 3 it needs s(s-2) ≥ S-2s > n(s-2), i.e. s > n, impossible. So it can only happen when s = 1, i.e. n is a power of p, and then R_p = (n^2-1)/(n-1) = n+1.

So a(n) ≥ n+1 always, and a(n) = n+1 iff n is a prime power. Checked numerically for n ≤ 20000 (`a096127.gp`).

## 4. Kimberling morphic-sequence bounds: computer-assisted PROOFS

Method (`morph/exact.py`, `morph/exact2.py`, `morph/table.py`): every prefix of the (limiting) word has a Dumont–Thomas decomposition σ^K(q_K)…σ^0(q_0), where the q_i are proper prefixes of images along an admissible path. The discrepancy D(n) = n·r - a(n) (a = positions of the target letter) equals Σ λ2^i h(q_i) + (r-1). Here h is the left λ2-eigenfunctional h(x) = r·x_c - |x|, and the letter after the prefix must be c. A min/max dynamic program over levels (400–500 levels at 60 digits, tail < |λ2|^400) gives the exact inf and sup over all n. This is cross-checked by brute force (`morph/disc.c`, recursive generator, length 2·10^9, `run2e9.out`), which agrees in every case, e.g. A283967 brute force [-0.49987, 2.28063] vs exact [-0.5, 2.28078]. The iteration parity and the morphism were checked against the OEIS data for every case (`cases.py`). Note that the %t of **A284901/A284902** has the wrong morphism (it shows 1→0011, but the data follow 1→1000 as in %N).

| sequence | σ(0),σ(1) | r | λ2 | stated bounds | exact inf D | exact sup D | verdict |
|---|---|---|---|---|---|---|---|
| A283966 u (A283967) | 1,10101 | 2.78078 | -0.5616 | (-1,3) | -0.5 | 2.280776 | PROOF |
| A283966 v (A284015) | 1,10101 | 1.56155 | -0.5616 | (-1,2) | -0.719224 | 1.280776 | PROOF |
| A284369 u (A284370) | 1,1001 | 2.36603 | -0.7321 | (-3,4) | -2.366025 | 3.732051 | PROOF |
| A284369 v (A284371) | 1,1001 | 1.73205 | -0.7321 | (-2,3) | -2 (limit) | 2.732051 | HOLDS (boundary) |
| A284676 | 1,0111 | 1.30278 | -0.3028 | (-1,4) | -0.697224 | 0.302776 | PROOF |
| A284773 | 01,0010 | 1.57735 | -0.7321 | (-1,2) | -1/3 | 1.244017 | PROOF |
| A284902 | 01,1000 | 1.57735 | -0.7321 | (-3,3) | -2.488034 | 2.821367 | PROOF |
| A284931 | 01,1011 | √2 | 0.5858 | (-1,1) | -1 (limit) | 0.414214 | HOLDS (boundary) |
| A284945 | 01,1110 | 3.41421 | 0.5858 | (-4,3) | -3.414214 | 2.414214 | PROOF |
| A285032 | 10,001 | 1.70711 | -0.4142 | (-1,2) | -0.646447 | 1.560660 | PROOF |
| A285084 | 10,011 | φ^2 | 0.3820 | (0,r) | 0 (limit) | r (limit) | HOLDS (boundary) |
| A285140 | 10,0010 | 1.57735 | -0.7321 | (-1,1) | -4/3 | 1.821367 | **FALSE** (§2) |
| A285210 | 10,0100 | 2.73205 | -0.7321 | (0,3) | 0.154701 | 2.154701 | PROOF |
| A285419 | 11,011 | 3.73205 | -0.7321 | (-1,5) | -0.422650 | 4.309401 | PROOF |
| A285670 | 11,1101 | 1.28078 | -0.5616 | (-1,4) | -0.589903 | 1.050485 | PROOF |
| A026363 | 11,101 (from 1) | 1.36603 | -0.7321 | (-1,2) | -1 (limit) | 1.366025 | HOLDS (boundary); checked independently via Cloitre's recursion to 3·10^8 |
| A287724 | Fib. word, τ:0→1,1→010 | 4-√5 | -0.618 | (0,3) | 0 | 2/φ | PROOF (by hand, below) |

For A283966/A284369, "u(n) = # 0's <= n" is read as the position of the n-th 0 (A283967). Any other reading makes the statement trivially false.
"HOLDS (boundary)": the exact extremum equals the bound to about 55 digits and is not attained, because D(n) is irrational. I do not claim these as fully rigorous proofs.

**A287724 hand proof:** The Fibonacci word satisfies f(n) = ⌊(n+1)α⌋ - ⌊nα⌋ with α = 1/φ^2. Each block τ(f(i)) contains exactly one 1, so a(n) = n + 2⌊nα⌋ + f(n). With r = 1 + 2α this gives D(n) = 2{nα} - f(n). Also f(n) = 1 ⇔ {nα} ≥ 1-α. Hence 0 < D(n) < 2(1-α) = 2/φ < 3.

## 5. Paul Hanna g.f. congruence conjectures: easy PROOFS

General principle: in each case a(n) is given by an integer recursion in a(1..n-1) with coefficient ±1 on a(n) (no division). Reduction mod m commutes with products and composition. So any integer series B with the right initial terms that satisfies the functional equation mod m is ≡ A (mod m). All definitions were recomputed and matched to the data (`hanna/check*.gp`, `check3.py`, `a380678.gp`).
* **A091713** (A = x + xA(A(A))): "all terms are odd" (Dec 01 2024). B = x/(1-x) satisfies B∘B = x/(1-2x) ≡ x, so x + xB∘B∘B ≡ x + xB = B (mod 2).
* **A396099** (A = x + A∘A · A∘A∘A; Jun 02 2026): all four conjectures hold. Parity: as above with B = x/(1-x). **Mod 4:** B = x/(1-x) + 2(x^4+x^5)/(1-x^4). As rational functions, x + B∘B·B∘B∘B - B = N/D with D(0) = -1 and content(N) = 4, so A ≡ B (mod 4), i.e. [1,3,3,1] repeating for n > 2. Likewise B∘B - x - 2x^2 and (B - xB∘B∘B) - x - 2x^3/(1-x) have numerator content 4 and D(0) = -1. This gives [x^n]A(A) ≡ 0 and [x^n](A - xA(A(A))) ≡ 2 (mod 4) for n > 2 (`hanna/a396099_c.gp`).
* **A378575** (A = x + xA^{∘5}): "a(n) ≡ 1 (mod 4)". B = x/(1-x) gives x + xB^{∘5} = x(1-4x)/(1-5x), whose coefficients 5^{m-2} (m ≥ 2) are ≡ 1 (mod 4).
* **A374570** (A^2 = A(A·C), C = x + C^2): C ≡ S = Σx^{2^k} (mod 2). B = x(1+C) gives B·C ≡ x(C + C(x^2)) = x^2, so B(BC) ≡ B(x^2) ≡ B^2. The coefficient of a(n) in the x^{n+1} equation is 2-1 = 1. So a(n) is odd iff n = 1 or n = 2^k+1.
* **A177775** ([x^n]A^{∘n} = [x^n]A^{∘(n-1)}): a(n) = P_{n-1,n} - P_{n,n}. S = Σx^{2^k} is additive mod 2, so S^{∘t} = Σ_m C(m+t-1,t-1)x^{2^m}. For n = 2^m ≥ 4, both C(m+n-1,n-1) and C(m+n-2,n-2) are even (Lucas). So a(n) is odd iff n is a power of 2.
* **A389540** (A^2 = A(2x-2A)/2): mod 2 the right side is x - A, so A ≡ x + A(x^2). Hence a(n) is odd iff n = 2^k.
* **A368633** (A = 1 + 2xA^2 - xA(-x)^2): mod 2, A ≡ 1 + xA(x^2), so the odd terms are at n = 2^k - 1.
* **A380678** (A(x - A^2/(1-A^2)) = x): T = x^2·Ã with Ã = Σ_m (x^{3·2^m-2} + x^{2^{m+2}-2}) satisfies T^2 + T = x^3 + x^4 over F2. Then u = Ã^2 satisfies u = x^2 + x^4 + x^4u^2, and F = x + u/(1+u) satisfies (1+x)^2F^2 + F + x = 0. This forces Z = Ã(F) (the unique small root of F^2Z^2 + Z + F + F^2 = 0) to equal x. Since a(n) enters [x^n]A(F) with coefficient 1, a(n) is odd iff n ∈ A027383 (checked to n = 80).

## 6. Other easy proofs
* **A140869** (Librandi): if 4h+5 is composite, write 4h+5 = (2m+1)(2n+1) with m ≥ n ≥ 1. Since 4h+5 ≡ 1 (mod 4), m+n is even, so T(m,n) = (2mn+m+n-2)/2 = h. Hence h not a term ⇒ 4h+5 prime.
* **A308090**: if n+1 > 4 is composite then n+1 | n!. So n+1 | 2^n and n+1 | 3^n, which is impossible. For n = 3, gcd(14,33,4) = 1. So gcd = n+1 ⇒ n+1 prime.
* **A135953**: for prime p ≥ 5, F_p = F_k^2 + F_{k+1}^2 with k = (p-1)/2 and gcd = 1, and F_p is odd. So every prime factor of F_p is ≡ 1 (mod 4) and is a sum of two squares.

## 7. A215926: equivalence with the almost-perfect-number conjecture (PROOF)

"Conjecture: a(n) is 1, 3, or a power of 2." (M. Marcus, 2012). Here a(n) is the least deficient k with k·n non-deficient.
* Even deficient n: 6 ∤ n (multiples of 6 are abundant or perfect), and σ(n)/n ≥ 3/2. So k = 3 works, and a(n) ∈ {2,3}.
* Odd deficient n: k = 2^j multiplies the abundancy by exactly 2 - 2^{-j}. Suppose a deficient non-power-of-2 k with 2^i < k < 2^{i+1} beats the powers of 2. Then σ(k)/k > 2 - 2^{-i} > 2 - 2/k, so σ(k) = 2k-1, i.e. k is almost perfect.
* Conversely, suppose k0 is the least non-power-of-2 almost perfect number, with 2^i < k0 < 2^{i+1}. Choose n odd, coprime to k0, with σ(n)/n ∈ [2k0/(2k0-1), 2^{i+1}/(2^{i+1}-1)). Such n exist, e.g. products of large primes. Then k0 works, since σ(k0 n)/(k0 n) = (2 - 1/k0)σ(n)/n ≥ 2. The powers 2^j ≤ 2^i fail. Every other deficient k' < k0 has σ(k') ≤ 2k'-2, so σ(k'n)/(k'n) ≤ (2 - 2/k')σ(n)/n < 2, because σ(n)/n < 2^{i+1}/(2^{i+1}-1) < k'/(k'-1). Hence a(n) = k0.

So the conjecture is equivalent to "all almost perfect numbers are powers of 2", which is open. The same analysis shows the first occurrence of 2^m is at the least prime > 2^m (A014210(m)), given that there is no almost perfect non-power of 2 below 2^{m+1}. Brute force agrees with the structural formula for n ≤ 6000 and with the data (`a215926.py`).

## 8. A001953 / A049473: PROOF of Kimberling's ζ(3) conjecture (Oct 2014)

"Let s(n) = zeta(3) - Sum_{k=1..n} 1/k^3. Conjecture: for n >= 1, s(a(n)) < 1/n^2 < s(a(n)-1), and the difference sequence of A049473 consists solely of 0's and 1's, in positions given by the nonhomogeneous Beatty sequences A001954 and A001953". Here a = A049473 = round(n/√2); in A001953 the text is a copy.

Let x = n/√2, a = round(x), y = a - 1/2, f(t) = t^{-3}.
* s(a) < 1/n^2: by strict convexity f(k) < ∫_{k-1/2}^{k+1/2} f, so s(a) < 1/(2(a+1/2)^2) < 1/(2x^2).
* s(a-1) > 1/n^2: the midpoint rule with remainders gives f(k) = I_k(f) - I_k(f'')/24 + f^{(4)}(η_k)/576 - f^{(4)}(ξ_k)/1920. Summing, s(a-1) ≥ 1/(2y^2) - 1/(8y^4) + 5/(48(y+1)^6) - 1/(32y^6) - 3/(16y^7). Let D = 2n^2 - (2a-1)^2 = 4(x^2-y^2), a positive odd integer. Then 1/(2y^2) - 1/(2x^2) - 1/(8y^4) = (2n^2(D-1) - D^2)/(32x^2y^4).
  * If D = 1 (Pell case), this is > -1/(32y^6), and the total is > 0 for y ≥ 17.5.
  * If D ≥ 3 and n ≥ 9, it is ≥ 1/(8y^4), which dominates.
  * Small n are covered by a 50-digit check of all n ≤ 5000.
  * At the Pell n (5, 29, 169, …, 1311738121) the margin n^2·s(a-1) - 1 is asymptotically 1/(3n^4) (`a049473.py`).
* Beatty part: the difference is round((n+1)/√2) - round(n/√2) ∈ {0,1}. It equals 1 iff n = ⌊(j+1/2)√2⌋, so the 1s sit at A001953 and the 0s at the complementary A001954 (Fraenkel's criterion; checked to n = 2000).

## 9. Partial or negative results
* **A023887** (R. Ahmed, Jun 19 2026: "5 is the only prime"). Since sigma_n is multiplicative and Σ_{i≤k} p^{ni} = ∏_{d | n(k+1), d ∤ n} Φ_d(p), a prime value forces n = p^{p-1}, with value Φ_{p^p}(p). Status of each case:
  * p=2 gives 5.
  * p=3: 109·433·8209.
  * p=5 (n = 625): BPSW says composite. It is also Aurifeuillian.
  * p=7 (n = 7^6): divisible by the prime 3294173 = 4·7^7+1.
  * p=11 (n = 11^10): divisible by the prime 3763497173422355909.
  * All primes p ≡ 1 (mod 4): Aurifeuillian factorization (standard, but I did not verify it independently).

  Open: p ≡ 3 (mod 4), p ≥ 19. Files: `a023887/`, `sig625.gp`.
* **A294509**: no n ≤ 1500 other than 5 has m ≤ 2·10^5 with pi(nm) - pi(n)pi(m) < a(n) (`a294509/t.c`).
* **A356490**: |det| is not a probable prime for 5 ≤ n ≤ 525 (`a356490/`).
* **A217499 / A217621 / A243888**: none of the 52 known Mersenne exponents satisfies 2p+1159, 2p+1939 or 2p+147 = odd square, except 107 in A243888 (`mers.gp`). **A090698**: no term k of A050414 has the form 2m^2 with 2m^2+1 prime. **A249902**: a counterexample needs n = 3^k with k+1 ∈ A028491, k ∈ A003306 ∩ A003307. Only k = 2 in the known lists.
* **A394752**: the Grundy values of .404 are unbounded-looking (256 by n = 20000), so it is INCONCLUSIVE.
* Checked earlier and dropped: A085577 (already proved, Fisher–Beel), A006255 (arXiv 2410.04728 addresses it), A225060 / A272817 / A110700 / A137248 / A362006 (heuristically safe).
