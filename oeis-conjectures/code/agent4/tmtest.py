import numpy as np, re, sys
from morphtest import word
L=int(float(sys.argv[1]))
tm=word([0,1],[1,0],1,L)  # parity irrelevant for TM (both start with own letter? 0->01 starts with 0)
w=''.join('01'[x] for x in tm[:L])
def test(name,base,rep,letter,claimed,data):
    w1=base
    for a,b in rep: pass
    # Mathematica StringReplace with list of rules: scans left to right, at each position tries rules in order
    pat=re.compile('|'.join(re.escape(a) for a,b in rep))
    d=dict(rep)
    w1=pat.sub(lambda m:d[m.group(0)],base)
    p=[i+1 for i,ch in enumerate(w1) if ch==letter]
    ok=p[:len(data)]==data
    print(name,'data_ok',ok,'claimed',claimed, ['n=%d:%.6f'%(N,p[N-1]/N) for N in [10**3,10**4,10**5,10**6,len(p)] if N<=len(p)])
test('A285958',w,[('01','0')],'0',4/3,[1,3,4,5,7,8,9,11,12,13,14,16,17,19,20,21,23,24,25,27,28,30,31,32,33])
test('A285973',w,[('10','1')],'0',4,[1,5,8,13,17,21,24,28,32,37,40,45,49,53,58,61,65,69,72,77,81,85,88,92])
test('A286486',w,[('0010','0')],'1',9/5,[2,3,5,8,9,11,12,14,16,17,20,21,23,26,27,29,30,33,34,36,38,39,41,44])
test('A286495',w,[('1011','0')],'1',3,[2,3,5,8,9,14,20,21,23,26,27,33,34,36,41,44,45,50,56,57,59,64,67,68])
test('A284684',w,[('0011','1')],'0',9/4,[1,4,7,8,10,13,15,16,18,22,25,26,28,32,34,35,37,40,43,44,46,49,51,52])
test('A286051',w,[('110','1')],'1',2,[2,3,6,8,10,11,14,16,18,19,22,24,26,28,29,32,34,35,38,40,42,43,46,48])
s=word([1,1],[0,0,1,1],0,L); ws=''.join('01'[x] for x in s)
test('A285516',ws,[('11','1'),('00','0')],'0',(3+5**.5)/2,[1,3,5,7,11,13,17,19,21,23,25,27,31,33,37,39,41,43,45,47,51,53,57,59])
s=word([1,1],[0,1,1,0],0,L); ws=''.join('01'[x] for x in s)
test('A285591',ws,[('00','0'),('11','1')],'1',1+(4/5)**.5,[2,4,6,8,10,12,13,15,17,19,21,23,25,27,29,31,33,35,36,38,40,42,44,46])
