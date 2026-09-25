from mpmath import mp, mpf, pi, sqrt, e, floor, nint
mp.dps=60
N=3000
cases={
 'A288229':(lambda k: int(floor((k+1)*pi/2)), [1,3,5,9,18,36,72,144,287,570,1132,2250,4473,8892,17676,35137,69847]),
 'A288235':(lambda k: int(floor((k+1)*sqrt(e))), [1,3,5,9,17,30,52,91,160,281,493,865,1518,2664,4675,8204,14397,25265]),
 'A289245':(lambda k: int(floor(-1+(k+1)*(3+sqrt(5))/2)), [1,4,10,25,64,162,408,1027,2584,6500,16351,41132,103468,260272,654709]),
 'A289912':(lambda k: int(nint((k+1)*sqrt(2))), [1,3,5,9,18,35,66,124,234,441,829,1557,2925,5496,10325,19394,36429]),
}
for A,(bf,data) in cases.items():
    b=[bf(k)*(-1)**k for k in range(N+1)]
    b0=b[0]; assert b0==1
    c=[0]*(N+1); c[0]=1
    for n in range(1,N+1):
        c[n]=-sum(b[k]*c[n-k] for k in range(1,n+1))
    assert c[:len(data)]==data,(A,c[:len(data)])
    bad=[n for n in range(N) if c[n+1]<=c[n]]
    print(A,"first non-increase up to",N,":",bad[:5], " ratio c(N)/c(N-1)=%.6f"%(c[N]/c[N-1]))
