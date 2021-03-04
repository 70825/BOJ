input=__import__('sys').stdin.readline
n=int(input())
D=[0]+[*map(int,input().split())]
S=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    S[i][i]=1
for i in range(1,n):
    if D[i]==D[i+1]:S[i][i+1]=1
for i in range(3,n+1):
    for j in range(n+2-i):
        if D[j]==D[i+j-1] and S[j+1][i+j-2]==1:S[j][i+j-1]=1
for i in range(int(input())):
    a,b=map(int,input().split())
    print(S[a][b])