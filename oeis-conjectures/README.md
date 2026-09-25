# Open OEIS conjectures resolved in this session

**Source.** A full local snapshot of the OEIS (`oeis/oeisdata`, 2026-09-24, 399,566 entries) was
filtered to about 6,500 open conjectures that a computer could plausibly test. Six search agents each
worked through a share of them, and I independently re-checked the strongest results.

**Novelty.** "New" means two things. First, the entry, and every entry that cross-references it, still
states the conjecture as open in the snapshot. Second, a web search found no earlier report. A few
counterexamples follow from facts that were already known but had never been connected to the
conjecture; these are flagged.

## A. Counterexamples I re-verified independently

`verify_counterexamples.gp` re-checks all of these in about a second with PARI/GP:
`gp -q verify_counterexamples.gp`.

| Entry | Conjecture (author, year) | Counterexample / certificate | Notes |
|---|---|---|---|
| **A225577** | Zhi-Wei Sun (2013): a(n), the least m with 1²,…,n² distinct mod 2^m−1, is the least Mersenne-prime exponent p with 2^p−1 > 2n−1 | At n = 2³⁰: a(n) = **49**, but the conjecture predicts 61. 2⁴⁹−1 = 127·4432676798593, and that prime exceeds 2n, so no two squares collide. Every m ≤ 48 has an explicit collision. | Holds for all n < 2³⁰ and fails for every n from 2³⁰ to 2216338399359. |
| **A225577** | Sun, same entry: for n > 17, the least Fibonacci modulus is the first Fibonacci prime > 2n−1 | At n = (F₄₇+1)/2 = 1485607537 the least modulus is the **composite** F₆₅ = 5·233·14736206161, not F₈₃. | Smallest counterexample, per agent 3. |
| **A066803** | Jianing Song (2021): gcd(2^(2^k)+1, 3^(2^k)+1) = 1 for k ≠ 1 | p = 3·2⁴¹+1 is prime, and 2 and 3 both have order 2³⁹ mod p. So p divides a(2³⁸). The same happens at k = 39 via 21·2⁴¹+1. | The factor of F₃₈ is classical. Among all Fermat factors c·2^m+1 with c < 2·10⁵, only k = 38 and 39 work, so k = 30…37 stay open. |
| **A100682** | Charles R Greathouse IV (2012): floor(C(N,4)^¼) = floor((N−3/2)/24^¼) except for N ∈ {0,1,6,17,2403,5318} | Three new exceptions: **N = 634027531, 1705327318, 55292025086**. The scan is complete for N ≤ 4.4·10¹¹. | This is an inhomogeneous Diophantine-approximation phenomenon, so infinitely many exceptions are expected. |
| **A073631** | A. Adamchuk (2007): every non-squarefree term is a multiple of 23² | k = 3842760169² divides 3^(k−1) − 2^(k−1), and k mod 529 = 349. It is also a new square term, contradicting the remark that 1 and 529 are the only ones. | Follows from the base-(3,2) Wieferich-type prime in A376896, which no entry links to. |
| **A362334** | (2023): a(2n) ≤ a(2n−1) and a(2n) < a(2n+1), where a(n) = φ(n)+φ(n+2) | Explicit 63-digit counterexamples to **both** parts, built with the Chinese remainder theorem. | No violation for 2n ≤ 10⁹; the smallest counterexample is unknown. |
| **A103225** | Bill McEachen (2025): a(n) < πn² | a(6203) = 120879728 > π·6203² = 120879717.13. 6203 is a Gaussian prime, so this reduces to the Gauss circle problem. | Least counterexample. Others include 44963, 49123 and 100379. |
| **A376360** | Clark Kimberling (2024): the gaps are exactly {4,…,11,13}, with gap 12 checked absent for n ≤ 300000 | a(65603) = 336391 and a(65604) = 336403, a gap of 12. Gaps of 14 and 16 appear later. | This contradicts the entry's own verification claim. Agent 0 reports the same failure in A376355, A376356, A376358 and A376359. |
| **A071622** | Benoit Cloitre (2002): a(n) > log(n)² for n > 2300 | First fails at n = 16954 (a = 94 < 94.83). a(18966) = 0, and the sequence goes negative after that. | |
| **A072872** | Benoit Cloitre: a(n) < prime(n) for n > 47 | a(6298) = 77742 > prime(6298) = 62753 | Further exceptions at n = 51169 and 148755. |
| **A284364–A284366** | Clark Kimberling (2017): −2 < n·r − u(n) < 2 and −1 < n·s − v(n) < 2 | For v, first failure at n = 2977771 (value 2.00487…). For u, first failure at n = 8933313. | Found by agents 1, 2 and 5 and by my own generator. The exact supremum is 6/5 + √21/5. |
| **A126762** | Thomas Ordowski (2018): the least k > n with n^k ≡ n (mod k) equals the least k > n with n^(k−1) ≡ 1 (mod k) | At n = 363 these are 366 and 367. There are 163 such n up to 10⁶. | 363 lies inside the entry's b-file range, but the failure was never noted. |
| **A114782** | Amarnath Murthy: a(n) = 0 iff prime(n) + 1 ≡ 0 (mod 3) | p = 48247 = prime(4966) is 1 mod 3, but 10^k + p is always divisible by 7, 11, 13 or 37, so a(4966) = 0. | Smallest *proved* case. |
| **A220956** | Detlefs & Wilson (2013): a(n) = 0 iff n is an odd prime | n = 16843², where 16843 is a Wolstenholme prime. | Follows from known results (McIntosh 1995, A267824). Checked by agent 5 with two independent GMP programs; I did not rerun those. |

## B. Other counterexamples reported by the agents

Each of these was checked by at least two of the agent's own implementations, but I did not rerun them
myself. Details are in `agent-reports/`.

* **A289035, A289239, A289001, A289242, A289004** (Kimberling): the conjectured iterate lengths fail at
  iterate 22 (268184 letters versus 268182).
* **A288926, A288710**: fail at an iterate that is already listed.
* **A190646**: false at p = 3; proved for all p ≥ 5 (Mihailescu).
* **A220846**: the "injective" claim fails in the listed data.
* **A327136, A327138**: the literal statements fail at n = 1; the intended one is proved.
* **Kimberling morphic-word bounds (all 109 in the OEIS; `agent-reports/kimberling_all.md`).**
  Exact infimum and supremum were computed in ℚ(√D).
  * 58 are proved.
  * 31 hold with the bound exactly equal to a limit that is never attained.
  * 14 are false, plus 2 false only by equality at n = 1.
  * 4 are unbounded because the substitution is not Pisot.
  * Only A284364–A284366 fail beyond the listed data.
  * Several stated constants are typos. The corrected versions are listed.

## C. Proofs of open conjectures (agent-reported)

I checked the A096127 argument line by line. I also confirmed the A001953 inequality numerically for
n ≤ 2·10⁵ at 40 digits. The other proofs are written out in full in `agent-reports/` but have not been
independently reviewed.

* **A096127:** a(n) = n+1 iff n is a prime power. The proof uses digit sums: s_p(n²) ≤ s_p(n)².
* **A001953 / A049473:** Kimberling's ζ(3) inequality, proved with explicit midpoint-rule error bounds.
* **A363482:** every term is 1 or prime, except 49. The proof goes through a closed form via left factorials.
* **A366274:** a(n) < n, using Dusart's explicit bounds.
* **A074882:** a(n) < n whenever n is not a prime power.
* **A062854:** a(n) > n/log n.
* **A397683:** f(m) = 0 exactly for powers of 3 and 7, via Cohen's theorem on consecutive primitive roots.
* **A342070:** the sequence is finite with 32 terms.
* **A373308:** all three conjectures.
* **A115770:** an equality of two carryless-multiplication sets, via a 14-state automaton.
* **Bala's "a(n/2) is an integer":** A061164, A295454, A295468 and A295481.
* **A000139:** the parity conjecture.
* **A215926:** shown **equivalent** to the open problem "every almost perfect number is a power of 2".
* **Dozens of easier proofs**, for example g.f. congruences mod 2 and mod 4 of Paul Hanna's sequences.

## D. Negative results (searched further, nothing found)

See the agent reports. Examples: A366833 to 10¹⁸; A294646 to 10⁸; A171481 to 4·10⁸.

## Caveats

* OEIS b-files in the snapshot are Git-LFS stubs, so all computations were compared against the terms
  printed in each entry.
* `code/agentN/` mirrors each agent's working directory. Paths inside `agent-reports/` refer to
  `/home/user/work/agentN/`, which corresponds to `code/agentN/` here.
