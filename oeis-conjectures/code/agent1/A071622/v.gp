\\ independent: a(n) = -sum_{k=1..n} (-1)^floor((4/3)^k), exact via integer division
a=0; for(k=1,16954, a -= (-1)^((4^k)\(3^k)); if(k==16954, print("a(16954) = ", a, "   log(16954)^2 = ", log(16954)^2)));
b=0; firstnp=0; for(k=1,30000, b -= (-1)^((4^k)\(3^k)); if(k>2300 && b<=0 && !firstnp, firstnp=k; print("first k>2300 with a(k)<=0: ", k, " a=", b)));
quit;
