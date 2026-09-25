# Independent (sympy) verification of the two A362334 counterexamples
from sympy import isprime
from math import prod
def check(n, P1, P2, part):
    k=2*n
    if part==1: lo, hi = k-1, k+1      # compare a(k) with a(k-1)=phi(k-1)+phi(k+1)
    else:       lo, hi = k+1, k+3      # compare a(k) with a(k+1)=phi(k+1)+phi(k+3)
    q1=lo//prod(P1); q2=hi//prod(P2)
    assert prod(P1)*q1==lo and prod(P2)*q2==hi
    s=(k+2)//4; assert 4*s==k+2 and n%2==1
    assert all(isprime(x) for x in [n,s,q1,q2]+P1+P2)
    lhs=(n-1)+2*(s-1)                                   # phi(2n)+phi(4s), n,s odd primes
    rhs=prod(p-1 for p in P1)*(q1-1)+prod(p-1 for p in P2)*(q2-1)
    print('part',part,'a(k)=',lhs,' other=',rhs,' violation:', lhs>rhs if part==1 else lhs>=rhs)
A=[5,7,11,17,23,37,41,47,61,71,73,89,101,103,113,127,137]
B=[3,13,19,29,31,43,53,59,67,79,83,97,107,109,131,139,149]
check(134012348126107206688690603701275719891017841718586793654900333, A, B, 1)
check(539414769491017837931500222298531509788246672344348812944989101, B, A, 2)
