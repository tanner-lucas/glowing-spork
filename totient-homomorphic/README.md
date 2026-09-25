# φ(n+k) = φ(n) + φ(k): extended search and a reduction for n = 3

**Problem** (R. K. Guy, *Unsolved Problems in Number Theory*, B36; OEIS A066426 and A110172). For which
n is there a k ≥ 1 with φ(n+k) = φ(n) + φ(k)? A066426 lists the least such k, with 0 meaning none exists.
A066426 is titled "Conjectured values", and N. J. A. Sloane comments there: "It would be nice to remove
the word 'Conjectured'". A110172 lists the n < 2000 with no solution k < 10⁸ (T. D. Noe, 2005).
By Fernandes (2022) every such n is an odd multiple of 3.

## 1. The search now goes 1000× further (no solutions)

`code/phisearch.c` is a segmented totient sieve that uses only multiplications. It compares
φ(k+n) with φ(k)+φ(n) for every n in the open list, one n at a time, as a vectorisable pass over each
segment.

* **Validation.** For k < 2·10⁶ and all 333 odd multiples of 3 below 2000, the sieve finds exactly the
  same 789 solutions (n, k) as an independent numpy totient sieve (`code/verify_small.py`). It also
  reproduces every A066426 term listed for odd multiples of 3.
* **Result.** I ran every k < 10¹¹ against all 66 values of n < 2000 still open at k = 2·10⁶. The
  list is in `code/junres.txt`: 3, 15, 21, 39, 45, 57, 69, 105, … It found **no solution**.

  This agrees with A110172 below 10⁸ and extends its verification bound from 10⁸ to 10¹¹. It also
  lists the n in 1395 < n < 2000 that the entry's data omits: 1437, 1455, 1461, 1473, 1485, 1491, 1587,
  1641, 1689, 1695, 1821, 1845, 1935, 1977, 1995.

## 2. Why n = 3 is so hard: a reduction to Lehmer-type equations

**Theorem.** Suppose φ(k+3) = φ(k) + 2 with k ≥ 1. Then k = 2pᵃ or k = 2pᵃ − 3 for some prime
p ≡ 3 (mod 4) and some a ≥ 1. Moreover:

* **(i)** If k = 2p (a = 1), then y = 2p+3 is composite and 2φ(y) = y − 1.
* **(ii)** If k = 2·3ᵃ − 3 (p = 3), then y = 2·3ᵃ⁻¹ − 1 is composite, 3 ∤ y, and 2φ(y) = y − 1.
* **(iii)** If k = 2·3ᵃ (p = 3), then y = 2·3ᵃ⁻¹ + 1 satisfies 3 ∤ y and 2φ(y) = y + 1.

In cases (i) and (ii), φ(y) divides y − 1 for a composite y. Such a y would be a counterexample to
**Lehmer's totient conjecture** (1932, open). In case (iii), y would solve 2φ(y) = y + 1 without being
divisible by 3. The known solutions 3, 15, 255, 65535 and 4294967295 (products of consecutive Fermat
primes) are all divisible by 3.

*Proof.* φ(1) = φ(2) = 1, and k = 1, 2 are not solutions, so take k ≥ 3. Then φ(k) and φ(k+3) are
both even, and their difference is 2, which is ≡ 2 (mod 4). So exactly one of them is ≡ 2 (mod 4).

Now φ(m) ≡ 2 (mod 4) exactly when m = 4, m = qᵇ or m = 2qᵇ with q ≡ 3 (mod 4) prime. This holds
because v₂(φ(m)) = Σ_{odd q | m} v₂(q−1) plus (c−1 if 2ᶜ ‖ m with c ≥ 1). So k or k+3 is 4, qᵇ or 2qᵇ.

* k = 4 fails (φ(7) = 6 ≠ 4), and k + 3 = 4 means k = 1.
* If k = qᵇ, then k+3 is even. So φ(k+3) ≤ (k+3)/2 < (2/3)k + 2 ≤ φ(k) + 2, which is impossible.
* If k + 3 = qᵇ, then k is even. So φ(k) ≤ k/2, but φ(k) = φ(qᵇ) − 2 ≥ (2/3)qᵇ − 2. This forces
  qᵇ ≤ 3, i.e. k = 0.
* The remaining possibilities are k = 2qᵇ and k + 3 = 2qᵇ.

For (i): φ(2p) = p − 1, so we need φ(2p+3) = p + 1 = (y−1)/2. If y were prime, then φ(y) = y − 1,
which would force y = 1. So y is composite.

For (ii) and (iii) with a ≥ 2, 3 exactly divides k or k+3, and the equation becomes 2φ(y) = y ∓ 1.
In (ii), y prime would again force y = 1, so y is composite. For a = 1, k = 3 and k = 6 fail by
direct check. ∎

So a solution for n = 3 must come from a thin set: only O(x/log x) candidates below x. The two families
above would settle a 90-year-old open problem. This explains why no solution has turned up. It
also suggests that proving a(3) = 0, which would remove "Conjectured" from the entry, is probably out
of reach.

Heuristically, with P(hit) ≈ c/k over k ≈ 2p, the expected count grows like log log x. So solutions may
exist but be astronomically sparse. No analogous mod-4 obstruction exists for the other open n: they
have φ(n) ≡ 0 (mod 4), and n = 3 is the only power of 3 in the list.
