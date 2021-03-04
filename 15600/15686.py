from itertools import combinations
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if D[i][j]==1:home.append((i,j))
        if D[i][j]==2:chicken.append((i,j))
ans=float('inf')
for Chicken in combinations(chicken,m):
    k=sum(min(abs(Chi[0]-Home[0])+abs(Chi[1]-Home[1]) for Chi in Chicken) for Home in home)
    ans=min(ans,k)
print(ans)