D=sorted([*map(int,input().split())])
print([2*(D[0]+D[1])-1,sum(D)][D[0]+D[1]>D[2]])