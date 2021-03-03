input=__import__('sys').stdin.readline
from heapq import *
n=int(input())
Min_idg=[0]*(n+1)
Max_idg=[0]*(n+1)
Min_adj=[[] for _ in range(n+1)]
Max_adj=[[] for _ in range(n+1)]
Max=[0]*(n+1)
Min=[0]*(n+1)
D=[*input().split()]
for i in range(n):
    if D[i]=='<':
        Min_adj[i].append(i+1);Min_idg[i+1]+=1
        Max_adj[i+1].append(i);Max_idg[i]+=1
    else:
        Min_adj[i+1].append(i);Min_idg[i]+=1
        Max_adj[i].append(i+1);Max_idg[i+1]+=1
q1=[];q2=[]
num1,num2=9,0
for i in range(n+1):
    if Min_idg[i]==0:heappush(q2,i)
    if Max_idg[i]==0:heappush(q1,i)
for i in range(n+1):
    x=heappop(q1)
    y=heappop(q2)
    Max[x]=num1;Min[y]=num2
    num1-=1;num2+=1
    for nx in Max_adj[x]:
        Max_idg[nx]-=1
        if Max_idg[nx]==0:heappush(q1,nx)
    for ny in Min_adj[y][::-1]:
        Min_idg[ny]-=1
        if Min_idg[ny]==0:heappush(q2,ny)
print(''.join(map(str,Max)))
print(''.join(map(str,Min)))