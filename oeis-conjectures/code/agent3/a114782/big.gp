{
U=[2971, 9811, 15817, 20089, 25609, 28909, 33331, 35311, 35839, 37159, 37357];
foreach(U,p, found=0; for(k=1001,6000, if(ispseudoprime(10^k+p), found=k; break)); print(p," -> smallest k in (1000,6000] with 10^k+p PRP: ",found));
}
