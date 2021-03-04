from collections import deque
S=int(input())
D=[[-1]*(S+1) for _ in range(S+1)]
q=deque();q.append((1,0))
D[1][0]=0
while q:
    a,b=q.popleft()
    if D[a][a]==-1: # 복사
        D[a][a]=D[a][b]+1
        q.append((a,a))
    if a+b<=S and D[a+b][b]==-1: # 붙여넣기
        D[a+b][b]=D[a][b]+1
        q.append((a+b,b))
    if a-1>=0 and D[a-1][b]==-1: # 삭제
        D[a-1][b]=D[a][b]+1
        q.append((a-1,b))
k=-1
for i in range(S+1):
    if D[S][i]!=-1:
        if k==-1 or k>D[S][i]:k=D[S][i]
print(k)