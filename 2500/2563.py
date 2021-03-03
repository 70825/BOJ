D=[[0]*101 for _ in range(101)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            D[i][j]=1
ans=0
for i in range(101):
    for j in range(101):
        ans+=D[i][j]
print(ans)