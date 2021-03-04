input=__import__('sys').stdin.readline
n,m=map(int,input().split())
k=[*map(int,input().split())]
D=[0]*(n+1)
for i in range(n):
    D[i+1]=D[i]+k[i]
for _ in range(m):
    a,b=map(int,input().split())
    print(D[b]-D[a-1])