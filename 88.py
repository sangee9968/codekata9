import math
n,m=map(int,input().split())
#result
print(n*m//math.gcd(n,m))
