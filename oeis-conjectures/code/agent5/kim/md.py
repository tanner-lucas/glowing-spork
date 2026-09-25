import json
rows=json.load(open('rows.json'))
typeB=json.load(open('typeB.json'))
def esc(s): return str(s).replace('|','\\|')
from collections import Counter
cnt=Counter()
for x in rows:
    v=x['verdict']
    k='PROVED' if v.startswith('PROVED') else 'BOUNDARY' if v.startswith('BOUNDARY') else 'NON-PISOT' if v.startswith('NON') else ('FALSE-n=1-equality-only' if 'only at n=1' in v else 'FALSE')
    cnt[k]+=1
L=[]
L.append("# Kimberling-type discrepancy conjectures in the whole OEIS: exact extremes\n")
L.append("Agent 5, 2026-09-25. Code: `/home/user/work/agent5/kim/`. Machine-readable version: `/home/user/work/results/kimberling_all.csv`.\n")
L.append("## Scope\n")
L.append("I searched the whole local OEIS (`idx/oeis.jsonl`) for conjectures of the form `lo < n*r - a(n) < hi` (also `n*s - v(n)`, `n*r - u(n)`, `n*sqrt(k) - a(n)`, `a(n) - n*sqrt(2)`, `n*(1+sqrt(3)) - a(n)`) in entries tied to a morphism, limiting word or `Positions of` sequence. This gives **101 entries**: the coordinator's 86 plus 15 more (A026367, A086398, A283965, A284371, A284507, A284655, A284658, A284895, A284931, A284941, A285276, A285343, A285360, A285374, A285375).")
L.append("Seven fixed-point entries state two conjectures (for u and v), and A284895 has a second, corrected inequality. That makes **109 conjecture instances**. All of them are binary substitutions, or Fibonacci-word transforms `tau(sigma^inf(0))`.\n")
L.append("Not in scope: the relative-error family `lo < m - a(n)/n < hi` (about 80 entries, mostly mappings on 2-letter blocks rather than letter morphisms, with m given only as a decimal). A data-only scan is in the appendix. Also skipped: complementary-equation entries (A298003 etc.), trigonometric ones (A327136/A327138, the first handled in slice5.md), and asymptotic statements.\n")
L.append("## Headline counts (109 instances)\n")
for k,v in cnt.most_common(): L.append(f"- {k}: {v}")
L.append("")
L.append("### Every FALSE verdict (reading = intended: exact density r, u/v = positions)\n")
L.append("| A-number | smallest violating n | exact certificate | in listed data? |\n|---|---|---|---|")
for x in rows:
    if x['verdict'].startswith(('FALSE','NON')):
        m=x['verdict']
        inlist = 'no; brute-force confirmed' if any(s in x['A'] for s in ('A284364','A284365','A284366')) else 'yes'
        L.append(f"| {x['A']} | {esc(m)} | {esc(x['certificate'] or '-')} | {inlist} |")
L.append("")
L.append("### Literal-reading problems (typos or wrong multiplier). The intended reading is analysed in the main table\n")
for x in rows:
    ln=x['literal_note'].split('; literal "u(n)')[0]
    if ln and not ln.startswith('literal "u(n)'):
        L.append(f"- **{x['A']}**: {esc(ln)}; intended reading verdict: {esc(x['verdict'].split(':')[0])}")
L.append("- **A283963, A283966, A284364, A284368, A284369, A284386, A284505** (u/v statements in the fixed-point entries): read literally, `u(n) = # 0's <= n` makes n*r - u(n) grow linearly, so the statement is trivially false. I use u(n), v(n) = position of the n-th 0 (1), which is clearly what was meant; the same statements appear as a(n) in the companion position entries.")
L.append("")
L.append("## Main table (all 109 instances)\n")
L.append("D(n) = n*r - a(n), with r the exact density ratio (1/frequency of the letter). inf and sup are exact values over all n >= 1 (the n=0 term of A045671/A045672 is checked separately in the notes). Verdict key:")
L.append("- PROVED: inf > lo and sup < hi strictly.")
L.append("- BOUNDARY: an extreme equals a bound exactly but D(n) never equals it, so the strict inequality holds.")
L.append("- FALSE: smallest violating n given, with an exact certificate.")
L.append("- NON-PISOT: second eigenvalue has |lambda2| > 1, so D is unbounded.\n")
L.append("| A-number | substitution (sigma; tau), start, word | letter | stated conjecture | exact r | lambda2 | inf D (exact; 35 digits) | sup D (exact; 35 digits) | verdict | notes | brute-force min/max check |")
L.append("|---|---|---|---|---|---|---|---|---|---|---|")
for x in rows:
    L.append(f"| {x['A']} | {esc(x['word'])} | {x['letter']} | {esc(x['stated'])} | {esc(x['r_exact'])} | {x['lambda2']} | {esc(x['inf_exact'])} = {x['inf']} | {esc(x['sup_exact'])} = {x['sup']} | {esc(x['verdict'])} | {esc(x['notes'])} {esc(x['literal_note'])} | {esc(x['bruteforce'])} |")
L.append("")
L.append("## Method (exact, rigorous)\n")
L.append("""1. **Word.** Let w = lim sigma^K(start), with K running over Kimberling's iteration count mod p. Then w is the fixed point of sigma^p beginning with b = the first letter of sigma^K(start). Getting b right matters: using start = 0 as the root for sigma = 0->10, 1->1110 would add non-prefixes and overstate sup for A285374. The coded word is v = tau(w), a(n) is the position of the n-th letter c in v (1-based), and D(n) = n*r - a(n) with r = 1/freq_v(c), computed exactly from the Perron eigenvector in Q(sqrt d). **Every generated sequence reproduces the full listed OEIS data** (column data_ok in the CSV).
2. **Eigen-functional.** h(u) = r*|u|_c - |u| vanishes on the Perron vector, so on a 2-letter alphabet it is a left lambda2-eigenvector: h(tau(sigma(x))) = lambda2 * h(tau(x)) (checked exactly for every case).
3. **Dumont–Thomas.** Take L a multiple of p with mu = lambda2^L > 0 (Pisot case). Every prefix of w is sigma_L^{S-1}(Q_{S-1}) ... sigma_L^0(Q_0), where Q_s is a proper prefix of sigma_L(e_{s+1}) and e_s is the next letter. Hence D(n) = [h(tau(e_0)[:j]) + r - 1] + sum_s mu^s h(tau(Q_s)): a discounted path cost in a finite prefix automaton.
4. **Exact extremes.** Let W(e) = inf over infinite upward paths from e. It solves the Bellman equation W(e) = min over edges e'->e of (cost + mu W(e')), since mu < 1 makes it a contraction. I solve it **exactly in Q(sqrt d) by policy iteration** (value iteration only seeds the policy; optimality is then verified exactly edge by edge). Then inf D = min_e [bottom_min(e) + W(e)], and sup likewise. Values of finite prefixes are values of paths padded with zero-cost root loops, so they are >= inf. Primitivity makes every infinite path a limit of real prefixes, so inf is sharp. When an extreme equals a bound B exactly, attainment needs B - n*r in Z, which I check exactly; only A285075/A285078 attain it, at n = 1.
5. **Smallest violating n.** A depth-first search over the Dumont–Thomas tree in positional order, pruned with exact finite-depth min/max tables, returns the first violating leaf. That leaf is certified by exact evaluation of n*r - a(n) in Q(sqrt d). A strict variant separates "equality" from "strict" violations.
6. **Independent checks.** (a) A separate numeric level-by-level DP (`/home/user/work/agent5/morph/exact2.py`, 700 levels, 60 digits) agrees with the exact Bellman values to < 1e-25 on **all 105 Pisot instances**. (b) A quad-precision brute-force generator (`bfmm.c`) gives running min/max of D over the first 3e7–1e8 positions for every instance, always inside [inf, sup] and close to it. (c) For the FALSE cases not visible in the data (A284364 u/v = A284365/A284366), an independent quad-precision generator (`bf.c`) finds the same first violations n = 8933313 and n = 2977771. This matches agent 1.
""")
L.append("## Appendix: the `m - a(n)/n` family (data-only scan, not rigorous)\n")
L.append("These say `lo < m - a(n)/n < hi`, with m = lim a(n)/n given only to 2–3 decimals. Checked against the listed data only (tolerance equal to the truncation of m):\n")
for i,st,t in typeB:
    if st!='ok-in-data': L.append(f"- {i}: **{st}**: {esc(t)}")
L.append("- All other entries in the family (about 75) have no violation in the listed data. Their bounds are weaker than those in the main table: m - a(n)/n = D(n)/n.")
L.append("  - A288222 states the empty interval `0 < m - a(n)/n < 0` (typo).")
L.append("  - A288225 fails at n=1: m - 2 = 1.61 > 1.")
L.append("  - A289151 gives m = 1.56..., but the data give a(n)/n about 4.5. The stated limit looks wrong; with it the bound fails at n=1.")
open('/home/user/work/results/kimberling_all.md','w').write('\n'.join(L)+'\n')
print(len(L))
