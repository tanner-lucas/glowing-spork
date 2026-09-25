{
unres=List(); maxk=0; cnt=0;
forprime(p=3,48246, if(p%3==2, next); d=#digits(p); found=0;
  for(k=d,1000, if(ispseudoprime(10^k+p), found=k; break));
  cnt++; if(found==0, listput(unres,p), maxk=max(maxk,found)));
print("checked ",cnt," primes p<48247 with p%3!=2; unresolved (no PRP with k<=1000): ",unres,"  max k needed: ",maxk);
}
