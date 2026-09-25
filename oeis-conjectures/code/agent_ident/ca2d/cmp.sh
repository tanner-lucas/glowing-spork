#!/bin/bash
# cmp.sh R1 side1 R2 side2 shift nmin T   : compare seqR1[n] with seqR2[n+shift] for n>=nmin
R1=$1; S1=$2; R2=$3; S2=$4; SH=$5; NMIN=$6; T=$7
./ca $R1 $T > r$R1.txt; ./ca $R2 $T > r$R2.txt
python3 - "$R1" "$S1" "$R2" "$S2" "$SH" "$NMIN" <<'PY'
import sys
R1,S1,R2,S2,SH,NMIN=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]),int(sys.argv[6])
def load(r,side):
    d={}
    for line in open(f"r{r}.txt"):
        p=line.split(); n=int(p[0]); d[n]=p[2] if side=='L' else p[4]
    return d
A=load(R1,S1); B=load(R2,S2)
bad=[n for n in sorted(A) if n>=NMIN and n+SH in B and A[n]!=B[n+SH]]
print(f"Rule {R1}{S1} vs Rule {R2}{S2} shift {SH}: checked n={NMIN}..{max(A)-max(0,SH)}; first mismatches: {bad[:5]}")
if bad:
    n=bad[0]; print(" n=",n,"\n A:",A[n][:200],"\n B:",B[n+SH][:200])
PY
