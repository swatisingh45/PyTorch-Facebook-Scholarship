# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n,p  = [int(x) for x in input().split()]
a,b = [int(x) for x in input().split()]
L = []
List1 = [a,b]
for i in range(1,n+1):
    L.append(i)

if( n >= 1 and n<= 16 ):
    if(p>=1 and p<=(n*(n-1)/2)):
        if(a>=1 and a<= n and b>=1 and b<= n):
            [",".join(map(str, comb)) for comb in combinations(L, 2)]

for i in L:
    if(i == List1):
        L.pop(i)

print(len(L))


///////-------------------------

Prime factorization ------------

n = int( sys.argv[1] )
factors = list( primefac.primefac(n) )
print '\n'.join(map(str, factors))

        while True:
            while (l % d) == 0:
                primfac.append(d)
                l //= d

            d += 1

        if l > 1:
            primfac.append(n)
        return primfac







