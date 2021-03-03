n=int(input())
m=int(input())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
Max=[0]*(n+1)
V=[0]*(n+1)
for i in range(1,n+1):
    S[i][i]=0
for i in range(m):
    a,b=map(int,input().split())
    S[a][b]=1;S[b][a]=1
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[i][k]+S[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if S[i][j]!=float('inf'):
            Max[i]=max(Max[i],S[i][j])
D=[]
for i in range(1,n+1):
    k=i
    if V[i]==0:
        for j in range(1,n+1):
            if S[i][j]!=float('inf'):
                V[j]=1
                if Max[k]>Max[j]:k=j
        D.append(k)
D.sort()
print(len(D))
print('\n'.join(map(str,D)))