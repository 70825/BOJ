from itertools import *
N,r=map(int,input().split())
D=[]
for i in range(N):
    D.append(i+1)
D=list(permutations(D,r))
for i in range(len(D)):
    print(' '.join(map(str,D[i])))