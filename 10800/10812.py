n,m=map(int,input().split())
D=[i+1 for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    D=D[:a-1]+D[c-1:b]+D[a-1:c-1]+D[b:]
print(*D)