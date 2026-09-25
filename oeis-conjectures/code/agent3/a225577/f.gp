\\ F(m) = min over d|M, d<sqrt(M) of (d+M/d)/2, M=2^m-1
F(m)={my(M=2^m-1,best=(M+1)/2);fordiv(M,d,if(d*d<M,best=min(best,(d+M/d)/2)));best}
for(m=2,64,print(m," ",F(m)," ",factor(2^m-1)))
