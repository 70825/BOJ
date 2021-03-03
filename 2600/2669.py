D=[[0]*101 for _ in range(101)]
for _ in range(4):
    a,b,c,d=map(int,input().split())
    for i in range(b,d):
        for j in range(a,c):
            D[i][j]=1
ans=0
for i in range(101):
    ans+=sum(D[i])
print(ans)