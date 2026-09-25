import re,sys
def iterate(rules, n_iter):
    # independent implementation: Python re with alternation (leftmost match, alternatives tried in order)
    pat=re.compile("|".join(re.escape(p) for p,_ in rules))
    d=dict(rules)
    w="00"; L=[len(w)]
    for i in range(n_iter):
        w=pat.sub(lambda m: d[m.group(0)], w)
        L.append(len(w))
    return L
for name,rules in [("A289035",[("00","0010"),("01","010"),("10","010")]),("A289239",[("00","0010"),("01","100"),("10","010")]),("A289001",[("00","0010"),("01","001"),("10","010")])]:
    L=iterate(rules,25)
    print(name, L[18:26])
