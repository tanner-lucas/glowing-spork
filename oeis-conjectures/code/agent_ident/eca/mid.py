import numpy as np, sys
from eca import run
rule=int(sys.argv[1]); T=int(sys.argv[2])
W=2*T+5; C=T+2
a=np.zeros(W,dtype=np.uint8); a[C]=1; bg=0
lut=np.array([(rule>>i)&1 for i in range(8)],dtype=np.uint8)
mid=[1]; on=[1]
for n in range(T):
    idx=4*np.roll(a,1)+2*a+np.roll(a,-1)
    b=lut[idx]; nbg=lut[7*bg]; b[0]=nbg; b[-1]=nbg; a=b; bg=nbg
    mid.append(int(a[C])); on.append(int(a[C-n-1:C+n+2].sum()))
np.save(f"mid{rule}.npy",np.array(mid,dtype=np.uint8)); np.save(f"on{rule}.npy",np.array(on,dtype=np.int64))
print(''.join(map(str,mid[:60])))
