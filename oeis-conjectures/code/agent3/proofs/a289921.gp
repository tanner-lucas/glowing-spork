{
r=9/10; M=300; S=sum(k=0,M,floor(1+(k+1)*r)*(-x)^k)+O(x^(M+1)); G=1/S;
H=(1-x^10)*(1+x)^2/(1-2*x^10-x^11)+O(x^(M+1));
print("closed form equals definition up to x^",M,": ", G==H);
v=Vec(G); print("min coefficient: ", vecmin(v), "  first terms ", v[1..25]);
seq=[1,2,1,0,0,0,0,0,0,0,1,3,3,1,0,0,0,0,0,0,2,7,9,5,1,0,0,0,0,0,4,16,25,19,7,1,0,0,0,0,8,36,66,63,33,9,1,0,0,0,16,80,168,192,129,51,11,1,0,0,32,176,416,552,450,231,73,13,1,0,64,384,1008];
print("matches OEIS data: ", v[1..#seq]==seq);
}
