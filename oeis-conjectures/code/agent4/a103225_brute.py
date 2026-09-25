# brute force: Gaussian gcd via Euclid in Z[i]
import sys
def gdivround(a,b):
    # a/b for Gaussian ints (tuples), rounded
    (ar,ai),(br,bi)=a,b
    nb=br*br+bi*bi
    # a*conj(b)
    xr=ar*br+ai*bi; xi=ai*br-ar*bi
    # round division
    def rd(u,v):  # round(u/v) for v>0
        return (2*u+v)//(2*v)
    return (rd(xr,nb),rd(xi,nb))
def gmod(a,b):
    q=gdivround(a,b)
    return (a[0]-(q[0]*b[0]-q[1]*b[1]), a[1]-(q[0]*b[1]+q[1]*b[0]))
def ggcd_norm(a,b):
    while b!=(0,0):
        a,b=b,gmod(a,b)
    return a[0]*a[0]+a[1]*a[1]
def a(n):
    c=0
    for x in range(-n+1,n):
        for y in range(-n+1,n):
            if x*x+y*y<n*n and ggcd_norm((n,0),(x,y))==1:
                c+=1
    return c
if __name__=='__main__':
    N=int(sys.argv[1])
    print(','.join(str(a(n)) for n in range(1,N+1)))
