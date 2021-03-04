from itertools import *
N=int(input())
D=[]
for i in range(N):
    D.append(i+1)
D=list(permutations(D))
for i in range(len(D)):
    for j in range(N):
        print(D[i][j],end=" ")
    print()