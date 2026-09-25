# glowing-spork: computer-assisted discoveries in combinatorics and number theory

The request was to "make a novel scientific discovery". I chose experimental mathematics, because a
result there can be checked completely, both by proof and by computer. Everything here was produced in
one session using a local copy of the whole OEIS, C/GMP, PARI/GP and a team of search agents.

**How significant is this?** These are small results, not breakthroughs. Each one settles a precisely
stated open conjecture, or gives new data, in a place where nobody had recorded it. The strongest are:

1. **A complete solution of Sloane's "Integer Lunar Lander" conjectures (OEIS A360923 and A360925,
   2023).** This includes the closed form, the neighbour-difference conjecture, both of Sloane's
   questions, and new sequences for the 3-D version.
   → [`lunar-lander/`](lunar-lander/README.md)
2. **Two conjectures of Zhi-Wei Sun disproved (OEIS A225577, 2013).** The least m for which 1², …, n²
   are distinct mod 2^m−1 is 49 at n = 2³⁰, where Sun predicts 61. The Fibonacci version fails at
   n = 1485607537.
3. **More than 15 other refuted conjectures, each with a short checkable certificate.** Among them:
   * A066803 (J. Song): a Fermat-number factor divides gcd(2^(2^38)+1, 3^(2^38)+1).
   * A100682 (C. Greathouse): new exceptions at N ≈ 6·10⁸, 1.7·10⁹ and 5.5·10¹⁰.
   * A073631, A362334 (63-digit counterexamples), A103225, A376360, A071622, A072872, A126762,
     A114782, A284364–6 and A220956.

   Also dozens of proofs of open conjectures (many of them easy), and an exact resolution of all 109 of Kimberling's
   morphic-word discrepancy conjectures. → [`oeis-conjectures/`](oeis-conjectures/README.md)
4. **φ(n+k) = φ(n)+φ(k)** (Guy's *Unsolved Problems*, B36): no solution with k < 10¹¹ for any of the 66
   open n < 2000. The previous bound was 10⁸. For n = 3, a solution in two of its possible forms would
   be a counterexample to Lehmer's totient conjecture. → [`totient-homomorphic/`](totient-homomorphic/README.md)

## Verify it yourself

    gp -q oeis-conjectures/verify_counterexamples.gp        # 17 certificates, ~1 s
    cd lunar-lander && gcc -O2 -o bfs2 bfs2.c && ./bfs2 && python3 check2.py && python3 conj1.py
    gcc -O2 -o crashfree lunar-lander/crashfree.c && ./crashfree

## Method in brief

1. Clone the OEIS data mirror and index about 15,000 stated conjectures. Filter them to about 6,500
   that look open and testable.
2. Parallel agents triaged these, implemented each definition exactly (first reproducing the listed
   terms), pushed the searches far beyond the published ranges, and double-checked every violation with
   a second independent implementation.
3. Every result listed as verified in `oeis-conjectures/README.md` was re-checked with independent code.
   Novelty was checked against the full OEIS snapshot (2026-09-24) and by web search.
