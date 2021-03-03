import math
N=int(input())
k=int(math.log(N,2))
print([(N-2**k)*2,N][N-2**k==0])