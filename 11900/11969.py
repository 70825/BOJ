input=__import__('sys').stdin.readline
n,m=map(int,input().split())
pSum=[[0]*3 for _ in range(n+1)]
for i in range(n):
    k=int(input())
    for j in range(3):
        pSum[i+1][j]=pSum[i][j]
    pSum[i+1][k-1]+=1
for i in range(m):
    a,b=map(int,input().split())
    cow=[0,0,0]
    for j in range(3):
        cow[j]=pSum[b][j]-pSum[a-1][j]
    print(*cow)