N,X=map(int,input().split())
D=[*map(int,input().split())]
for i in range(N):
    if D[i]<X:print(D[i],end=" ")