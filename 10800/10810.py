n,m=map(int,input().split())
D=[0]*n
for _ in range(m):
    i,j,k=map(int,input().split())
    for z in range(i-1,j):
        D[z]=k
for a in range(n):
    print(D[a],end=" ")