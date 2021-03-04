input=__import__('sys').stdin.readline
N,M=map(int,input().split())
D=[[] for i in range(M)]
score=[0]*N
for i in range(N):
    List=sorted([*map(int,input().split())],reverse=True)
    for j in range(M):
        D[j].append(List[j])
for i in range(M):
    k=max(D[i])
    for j in range(N):
        if D[i][j]==k:score[j]+=1
for i in range(N):
    if score[i]==max(score):print(i+1,end=" ")